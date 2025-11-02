"""
API router creation for FastAPI application.
"""

from fastapi import APIRouter, FastAPI

from .log import log

# Uncomment the following line to disable automatic API documentation
# app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app = FastAPI()


def create(base="", version=1) -> APIRouter:
    """Create and return an APIRouter with the specified base path and version.

    Args:
        base (str): The base path for the API routes. Defaults to "".
        version (int): The version number for the API. Defaults to 1.

    Returns:
        APIRouter: An instance of APIRouter with the specified prefix.
    """
    if base != "" and not base.startswith("/"):
        base = "/" + base
    log.info(f"Registering API v{version} with base path: {base}")
    return APIRouter(prefix=f"/api/v{version}{base}")
