from .models import GithubWebHook

from fastapi import APIRouter

from fastapi_backend.log import log

api = APIRouter(prefix="/events/github")


@api.post("/")
async def github_event_endpoint(event: GithubWebHook) -> GithubWebHook:
    log.info(f"Received GitHub event: {event.hook.events}")
    return event
