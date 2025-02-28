from typing import Any, Self
from uuid import UUID

# TODO: Exception handling is a major learning area for me. This is a mess.
# Proper structure:
# 1. Define a base exception class (KollektivError)
# 2. Divide into 2 groups - retryable and non-retryable
# 3. Divide each group into MECE sub-groups, for example by domains or services (database, llm, validation, etc)
# 4. Catch all exceptions from 3rd party libraries and services and raise custom exceptions
# 5. Service layer should catch custom exceptions and raise them to the API layer or handle them internally
# 6. API layer catches necessary exceptions and raises HTTP status codes
# 7. There is a global exception handler which catches all missed Exception types and raises HTTP 500
# 8. The goal is to drive down unhandled exceptions to 0


class KollektivError(Exception):
    """Base class for Kollektiv exceptions."""

    def __init__(self, error_message: str | None):
        """Create an exception with an optional error error_message"""
        self.error_message = error_message

    pass


class RetryableError(KollektivError):
    """Base class for retryable errors."""

    def __init__(self, error_message: str, retry_after: int | None = None):
        self.retry_after = retry_after
        super().__init__(error_message)


class NonRetryableError(KollektivError):
    """Base class for non-retryable errors."""

    pass


# General errors
## User-input
class ValidationError(NonRetryableError):
    """Custom validation error raised when some form of input validation fails.
    Raised only when I am not using Pydantic models as a wrapper.
    """

    pass


## App configuration


# API errors
class WebhookError(KollektivError):
    """Base for webhook-related errors."""

    pass


class InvalidWebhookEventError(WebhookError):
    """Invalid webhook event received."""

    pass


# Chat-related errors
class ConversationNotFoundError(KollektivError):
    """Conversation not found."""

    pass


# Content-related errors
class DataSourceError(KollektivError):
    """Exception raised for errors related to Data Source operations."""

    def __init__(self, source_id: UUID, error_message: str, original_exception: Exception | None = None):
        self.source_id = source_id
        self.error_message = error_message
        self.original_exception = original_exception
        super().__init__(f"DataSourceError for source_id={source_id}: {error_message}")


## Firecrawl errors


class CrawlerError(KollektivError):
    """Base exception class for the crawler module."""

    pass


class FireCrawlJobNotFound(CrawlerError, NonRetryableError):
    """Job with given firecrawl ids not found"""

    pass


class EmptyContentError(CrawlerError, RetryableError):
    """Raised when crawled content is empty."""

    def __init__(self, url: str):
        super().__init__(f"Empty content parsed from  {url}. Please ensure crawler settings are correct and try again.")


# Search-related errors
# Infrastructure-related errors
## Supabase


class SupabaseAPIError(NonRetryableError):
    """Raised when a database operation fails."""

    def __init__(
        self,
        error_message: str,
        operation: str,
        entity_type: str | None = None,
        details: dict | None = None,
        cause: Exception | None = None,
    ):
        self.operation = operation
        self.entity_type = entity_type
        self.details = details or {}
        self.cause = cause
        super().__init__(error_message)

    def add_context(self, operation: str, entity_type: str) -> Self:
        """Adds context information to the exception."""
        self.operation = operation or self.operation  # Don't overwrite if already set
        self.entity_type = entity_type or self.entity_type  # Don't overwrite if already set
        return self


class RetryableDatabaseError(RetryableError):  # Changed from SupabaseAPIError
    """Retryable database errors (connection, timeout, etc)."""

    def __init__(self, message: str, operation: str, cause: Exception | None = None):
        self.operation = operation
        self.cause = cause
        super().__init__(message)


class EntityNotFoundError(SupabaseAPIError):
    """Entity not found in database. Only raise when business logic requires it."""

    def __init__(self, entity_type: str, identifier: Any):
        super().__init__(
            error_message=f"{entity_type} with id {identifier} not found", operation="find", entity_type=entity_type
        )


class BulkOperationError(SupabaseAPIError):
    """Raised when a bulk database operation fails."""

    def __init__(self, entity_type: str, operation: str, failed_items: list, error: Exception | None = None):
        self.operation = operation
        self.failed_items = failed_items
        self.original_error = error
        error_message = f"Bulk {operation} failed for {len(failed_items)} items"
        super().__init__(error_message, entity_type=entity_type, operation=operation)


## Vector storage
## Job management
class JobError(NonRetryableError):
    """An application-level job errors. Internal to the kollektiv backend application."""

    def __init__(self, job_id: str, error_message: str):
        self.job_id = job_id
        super().__init__(f"Job {job_id}: {error_message}")


class JobNotFoundError(JobError):
    """Exception raised when a job cannot be found."""

    def __init__(self, job_id: str):
        super().__init__(job_id, "not found")


class JobNotCompletedError(JobError):
    """Exception raised when attempting to access results of an incomplete job."""

    def __init__(self, job_id: str):
        super().__init__(job_id, "job not completed yet")


class JobUpdateError(JobError):
    """Exception raised when a job update fails."""

    def __init__(self, job_id: str, reason: str):
        super().__init__(job_id, f"update failed: {reason}")


class JobValidationError(JobError):
    """Exception raised when job data is invalid."""

    def __init__(self, job_id: str, reason: str):
        super().__init__(job_id, f"validation failed: {reason}")


class JobStateError(JobError):
    """Exception raised when job state transition is invalid."""

    def __init__(self, job_id: str, current_state: str, attempted_state: str):
        super().__init__(job_id, f"invalid state transition from {current_state} to {attempted_state}")


## Queue and workers


class LLMError(KollektivError):
    """Base class for LLM-related errors."""

    pass


class RetryableLLMError(RetryableError, LLMError):
    """Base class for retryable LLM errors."""

    def __init__(self, message: str, original_error: Exception, retry_after: int | None = None):
        super().__init__(f"Temporary error in chat: {message}. Please try again.", retry_after)
        self.original_error = original_error


class NonRetryableLLMError(NonRetryableError, LLMError):
    """Base class for non-retryable LLM errors."""

    def __init__(self, message: str, original_error: Exception):
        super().__init__(f"A non-retryable error occured in Anthropic chat: {message}")
        self.original_error = original_error


class RetryableCrawlerError(RetryableError, CrawlerError):
    """Retryable crawler errors (network, timeout issues)."""

    def __init__(self, message: str, operation: str, cause: Exception | None = None):
        self.operation = operation
        self.cause = cause
        super().__init__(message)
