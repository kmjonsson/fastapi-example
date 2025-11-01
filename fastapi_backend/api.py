from fastapi import FastAPI, APIRouter
from .log import log

app = FastAPI()


def create(base="", version=1) -> APIRouter:
    if base != "" and not base.startswith("/"):
        base = "/" + base
    log.info(f"Registering API v{version} with base path: {base}")
    return APIRouter(prefix=f"/api/v{version}{base}")
