from fastapi import FastAPI, APIRouter
from .log import log

app = FastAPI()

def api(base="", version=1):
    if base != "" and not base.startswith("/"):
        base = "/" + base
    log.warning(f"Registering API v{version} with base path: {base}")
    return APIRouter(prefix=f"/api/v{version}{base}")
