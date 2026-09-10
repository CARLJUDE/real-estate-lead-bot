"""Health check endpoint."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    """
    Simple health check.

    Returns 200 when the API process is running.
    Database connectivity checks can be added later.
    """
    return {
        "status": "ok",
        "service": "real-estate-lead-bot",
    }
