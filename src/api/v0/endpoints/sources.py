from collections.abc import AsyncGenerator
from uuid import UUID

from fastapi import APIRouter, HTTPException, status
from sse_starlette.sse import EventSourceResponse

from src.api.dependencies import ContentServiceDep, UserIdDep
from src.api.routes import CURRENT_API_VERSION, Routes
from src.api.v0.schemas.base_schemas import ErrorCode, ErrorResponse
from src.core._exceptions import CrawlerError, EntityNotFoundError, NonRetryableError
from src.infra.logger import get_logger
from src.models.content_models import (
    AddContentSourceRequest,
    AddContentSourceResponse,
    DataSourceStatusResponse,
    DeleteSourceResponse,
    SourceEvent,
    SourceListItemDTO,
    UpdateSourceSettingsRequest,
    UserSourceSettings,
)

logger = get_logger()
router = APIRouter(prefix=f"{CURRENT_API_VERSION}")


@router.post(
    Routes.V0.Sources.SOURCES,
    response_model=AddContentSourceResponse,
    responses={
        201: {"model": AddContentSourceResponse},
        400: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
    status_code=status.HTTP_201_CREATED,
)
async def add_source(
    request: AddContentSourceRequest,
    user_id: UserIdDep,
    content_service: ContentServiceDep,
) -> AddContentSourceResponse:
    """
    Add a new content source.

    Args:
        request: Content source details
        content_service: Injected content service
        user_id: User ID of the user adding the source, extracted from the JWT token

    Returns:
        AddContentSourceResponse: Created content source details

    Raises:
        HTTPException: If source creation fails for any reason
    """
    logger.debug(f"Dumping request for debugging: {request.model_dump()}")
    try:
        response = await content_service.add_source(request, user_id)
        return response
    except (CrawlerError, NonRetryableError) as e:
        raise HTTPException(status_code=500, detail=ErrorResponse(code=ErrorCode.SERVER_ERROR, detail=str(e))) from e


@router.get(
    Routes.V0.Sources.SOURCE_EVENTS,
    response_model=SourceEvent,
    responses={
        200: {"model": SourceEvent},
        404: {"model": ErrorResponse, "description": "Source not found"},
        500: {"model": ErrorResponse, "description": "Internal server error"},
    },
    status_code=status.HTTP_200_OK,
)
async def stream_source_events(source_id: UUID, content_service: ContentServiceDep) -> EventSourceResponse:
    """Returns a stream of events for a source."""
    try:

        async def event_stream() -> AsyncGenerator[str, None]:
            async for event in content_service.stream_source_events(source_id=source_id):
                event_json = event.model_dump_json()
                logger.debug(f"Printing event for debugging: {event_json}")
                yield event_json

        return EventSourceResponse(event_stream(), media_type="text/event-stream")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=ErrorResponse(code=ErrorCode.CLIENT_ERROR, detail=str(e))) from e


@router.get(
    Routes.V0.Sources.SOURCE,
    response_model=DataSourceStatusResponse,
    responses={
        200: {"model": DataSourceStatusResponse},
        404: {"model": ErrorResponse, "description": "Source not found"},
        500: {"model": ErrorResponse, "description": "Internal server error"},
    },
    status_code=status.HTTP_200_OK,
)
async def get_source_status(source_id: UUID, content_service: ContentServiceDep) -> DataSourceStatusResponse:
    """Returns a source status by ID."""
    try:
        response = await content_service.get_source_status(source_id=source_id)
        if response is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=ErrorResponse(code=ErrorCode.NOT_FOUND, detail=f"Source {source_id} not found"),
            )
        return response
    except NonRetryableError as e:
        raise HTTPException(status_code=500, detail=ErrorResponse(code=ErrorCode.SERVER_ERROR, detail=str(e))) from e


@router.get(
    Routes.V0.Sources.SOURCES,
    response_model=list[SourceListItemDTO],
    responses={
        200: {"model": list[SourceListItemDTO]},
        500: {"model": ErrorResponse, "description": "Internal server error"},
    },
    status_code=status.HTTP_200_OK,
)
async def get_sources(content_service: ContentServiceDep, user_id: UserIdDep) -> list[SourceListItemDTO]:
    """Returns a list of all sources that a user has."""
    try:
        return await content_service.get_sources_list(user_id=user_id)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=ErrorResponse(
                code=ErrorCode.SERVER_ERROR,
                detail="An error occurred while trying to get the list of sources. We are working on it already.",
            ),
        ) from e


@router.patch(
    Routes.V0.Sources.SOURCES,
    response_model=UserSourceSettings,
    responses={
        200: {"model": UserSourceSettings},
        400: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
    status_code=status.HTTP_200_OK,
)
async def update_source_settings(
    source_id: UUID,
    request: UpdateSourceSettingsRequest,
    user_id: UserIdDep,
    content_service: ContentServiceDep,
) -> UserSourceSettings:
    """Updates a source settings by ID."""
    try:
        return await content_service.update_source_active_state(
            user_id=user_id, source_id=source_id, is_active=request.is_active
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=ErrorResponse(code=ErrorCode.SERVER_ERROR, detail=str(e))) from e


@router.delete(
    Routes.V0.Sources.SOURCES,
    responses={
        200: {"model": DeleteSourceResponse},
        404: {"model": ErrorResponse, "description": "Source not found"},
        500: {"model": ErrorResponse, "description": "Internal server error"},
    },
    status_code=status.HTTP_200_OK,
)
async def delete_source(source_id: UUID, content_service: ContentServiceDep) -> DeleteSourceResponse:
    """Deletes a source by ID."""
    try:
        return await content_service.delete_source(source_id=source_id)
    except EntityNotFoundError as e:
        raise HTTPException(status_code=404, detail=ErrorResponse(code=ErrorCode.NOT_FOUND, detail=str(e))) from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=ErrorResponse(code=ErrorCode.SERVER_ERROR, detail=str(e))) from e
