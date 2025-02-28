from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from src.api.v0.schemas.base_schemas import ErrorCode, ErrorResponse
from src.infra.logger import get_logger
from src.infra.settings import settings

logger = get_logger()


async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Global exception handler for any unhandled exceptions."""
    logger.critical(f"Unhandled exception at {request.url.path}: {exc}", exc_info=True)

    # Include more details in development mode
    if settings.ENVIRONMENT == "development":
        detail = f"An internal server error occurred: {str(exc)}"
    else:
        detail = "An internal server error occurred, please contact support."

    return JSONResponse(
        status_code=500,
        content=ErrorResponse(code=ErrorCode.SERVER_ERROR, detail=detail).model_dump(),
    )


async def non_retryable_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Catch and log a non-retryable error."""
    error_message = getattr(exc, "error_message", None) or str(exc)
    logger.error(f"Non-retryable error at {request.url.path}: {error_message}", exc_info=True)

    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            code=ErrorCode.SERVER_ERROR,
            detail=f"An internal error occurred while processing your request: {error_message}.",
        ).model_dump(),
    )


async def validation_error_handler(request: Request, exc: ValidationError) -> JSONResponse:
    """Catches and logs all Pydantiv validation errors globally."""
    logger.error(f"Validation error at {request.url.path}: {exc}", exc_info=True)
    return JSONResponse(
        status_code=422,
        content=ErrorResponse(code=ErrorCode.CLIENT_ERROR, detail=str(exc)).model_dump(),
    )
