from typing import Any, TypeVar
from uuid import UUID

from src.core._exceptions import RetryableDatabaseError
from src.infra.decorators import supabase_operation, tenacity_retry_wrapper
from src.infra.external.supabase_manager import SupabaseManager
from src.infra.logger import get_logger
from src.models.base_models import SupabaseModel

logger = get_logger()
T = TypeVar("T", bound=SupabaseModel)  # define a generic type for the repository


class DataRepository:
    """Repository that handles all database operations.

    This repository provides a clean data access layer that:
    - Executes raw database operations (CRUD)
    - Handles database-specific implementation details
    - Maps database results to domain models
    - Isolates database-specific code from business logic

    Soft Delete Behavior:
    By default, all query methods (find, find_by_id) will exclude soft-deleted records
    (those with is_deleted=True). To include deleted records, pass include_deleted=True.

    Examples:
        # Save a source
        source = DataSource(source_type=DataSourceType.WEB, ...)
        saved = await repo.save(source)

        # Query jobs by status
        jobs = await repo.find(
            Job,
            filters={"status": JobStatus.PENDING}
        )

        # Complex JSONB queries
        sources = await repo.find(
            DataSource,
            filters={
                "metadata->url": "https://...",
                "status": SourceStatus.COMPLETED
            }
        )

        # Pagination and ordering
        requests = await repo.find(
            AddContentSourceRequest,
            order_by="created_at.desc",
            limit=10
        )

        # Include soft-deleted records
        deleted_sources = await repo.find(
            DataSource,
            include_deleted=True
        )
    """

    def __init__(self, supabase_manager: SupabaseManager) -> None:
        self.supabase_manager = supabase_manager
        logger.info("✓ Initialized data repository successfully")

    @tenacity_retry_wrapper(exceptions=(RetryableDatabaseError,))
    @supabase_operation
    async def save(self, entity: T | list[T]) -> T | list[T]:
        """Save or update an entity in the database.

        This method handles both insert and update operations through upsert.
        The operation is determined by the presence of the primary key value.

        Args:
            entity: Single entity or list of entities to save

        Returns:
            T | list[T]: Saved entity/entities with updated fields

        Examples:
            # Save new source
            source = DataSource(source_type=DataSourceType.WEB, ...)
            saved = await repo.save(source)

            # Update existing job
            job.status = JobStatus.COMPLETED
            updated = await repo.save(job)
        """
        # Get client
        client = await self.supabase_manager.get_async_client()

        # Handle both single and batch cases
        entities = [entity] if not isinstance(entity, list) else entity
        if not entities:
            return []

        # All entities must be same type
        entity_type = type(entities[0])
        data = [e.model_dump(mode="json", by_alias=True, serialize_as_any=True) for e in entities]

        # Single transaction for all entities
        result = await (
            client.schema(entity_type._db_config["schema"])
            .table(entity_type._db_config["table"])
            .upsert(data, on_conflict=entity_type._db_config["primary_key"])
            .execute()
        )

        # Return in same format as input
        saved = [entity_type.model_validate(item) for item in result.data]
        return saved if isinstance(entity, list) else saved[0]

    @tenacity_retry_wrapper(exceptions=(RetryableDatabaseError,))
    @supabase_operation
    async def find_by_id(self, model_class: type[T], id: UUID, include_deleted: bool = False) -> T | None:
        """Retrieve a single entity by its primary key.

        Args:
            model_class: The model class to query
            id: Primary key value
            include_deleted: Whether to include soft-deleted records (default: False)

        Returns:
            Entity instance or None if not found

        Examples:
            source = await repo.find_by_id(DataSource, source_id)
            job = await repo.find_by_id(Job, job_id)

            # Include soft-deleted records
            deleted_source = await repo.find_by_id(DataSource, source_id, include_deleted=True)
        """
        result = await self.find(
            model_class=model_class,
            filters={model_class._db_config["primary_key"]: str(id)},
            include_deleted=include_deleted,
        )
        if result:
            return model_class.model_validate(result[0])
        return None

    @tenacity_retry_wrapper(exceptions=(RetryableDatabaseError,))
    @supabase_operation
    async def find(
        self,
        model_class: type[T],
        filters: dict[str, Any] | None = None,
        include_deleted: bool = False,
        order_by: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> list[T]:
        """Execute a query with filters and pagination.

        Args:
            model_class: The model class to query
            filters: Field:value pairs supporting:
                - Simple equality: {"status": "pending"}
                - JSONB paths: {"metadata->url": "https://..."}
                - Nested JSONB: {"details->config->limit": 10}
            include_deleted: Whether to include soft-deleted records (default: False)
            order_by: Field and direction (field.asc/desc)
            limit: Maximum records to return
            offset: Number of records to skip

        Returns:
            List of model instances

        Examples:
            # Get pending jobs
            jobs = await repo.find(
                Job,
                filters={"status": JobStatus.PENDING}
            )

            # Get sources with pagination
            sources = await repo.find(
                DataSource,
                filters={"status": SourceStatus.COMPLETED},
                order_by="created_at.desc",
                limit=10,
                offset=20
            )

            # Query by JSONB field
            requests = await repo.find(
                AddContentSourceRequest,
                filters={"request_config->url": "https://..."}
            )

            # Include soft-deleted records
            sources = await repo.find(
                DataSource,
                include_deleted=True
            )
        """
        # Get client first
        client = await self.supabase_manager.get_async_client()

        # Build query
        query = client.schema(model_class._db_config["schema"]).table(model_class._db_config["table"]).select("*")

        # Initialize processed_filters
        processed_filters = {}

        # Apply soft delete filter if applicable
        if hasattr(model_class, "is_deleted") and not include_deleted:
            processed_filters["is_deleted"] = False

        # Process user-provided filters
        if filters:
            for field, value in filters.items():
                if isinstance(value, UUID):
                    processed_filters[field] = str(value)
                elif isinstance(value, list) and all(isinstance(x, UUID) for x in value):
                    processed_filters[field] = [str(x) for x in value]
                else:
                    processed_filters[field] = value

            # Use processed values in query with correct operators
            for field, value in processed_filters.items():
                if isinstance(value, list):
                    query = query.in_(field, value)  # Use in_ for lists
                else:
                    query = query.eq(field, value)  # Use eq for single values

        if order_by:
            query = query.order(order_by)

        if limit:
            query = query.limit(limit)

        if offset:
            query = query.offset(offset)

        # Debugging: Log the query and filters
        logger.debug(f"Executing query with filters: {processed_filters}")

        result = await query.execute()
        # Unpack API response
        return [model_class.model_validate(item) for item in result.data]

    @tenacity_retry_wrapper(exceptions=(RetryableDatabaseError,))
    @supabase_operation
    async def delete(self, model_class: type[T], id: UUID, hard_delete: bool = False) -> None:
        """Delete an entity from the database.

        By default, this performs a soft delete by setting is_deleted=True.
        If the model doesn't have an is_deleted field or hard_delete=True is specified,
        it will perform a hard delete (permanently removing the record).

        Args:
            model_class: The model class to delete
            id: Primary key value of the entity to delete
            hard_delete: Whether to perform a hard delete (default: False)

        Examples:
            # Soft delete a source
            await repo.delete(DataSource, source_id)

            # Hard delete a source
            await repo.delete(DataSource, source_id, hard_delete=True)
        """
        # Get client
        client = await self.supabase_manager.get_async_client()

        # Check if model supports soft delete
        supports_soft_delete = hasattr(model_class, "is_deleted")

        if supports_soft_delete and not hard_delete:
            # Perform soft delete by updating is_deleted=True
            entity = await self.find_by_id(model_class, id, include_deleted=True)
            if entity:
                entity.is_deleted = True
                await self.save(entity)
                logger.info(f"Soft deleted {model_class.__name__} with id {id}")
        else:
            # Perform hard delete
            await (
                client.schema(model_class._db_config["schema"])
                .table(model_class._db_config["table"])
                .delete()
                .eq(model_class._db_config["primary_key"], str(id))
                .execute()
            )
            logger.info(f"Hard deleted {model_class.__name__} with id {id}")
