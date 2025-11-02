from fastapi import APIRouter, FastAPI

from .log import log

# Uncomment the following line to disable automatic API documentation
# app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app = FastAPI()


def create(base="", version=1) -> APIRouter:
    if base != "" and not base.startswith("/"):
        base = "/" + base
    log.info(f"Registering API v{version} with base path: {base}")
    return APIRouter(prefix=f"/api/v{version}{base}")
