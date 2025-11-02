"""
GitHub event router for handling webhook events.
"""

from fastapi import APIRouter

from fastapi_backend.log import log

from .models import GithubWebHook

api = APIRouter(prefix="/events/github")


@api.post("/")
async def github_event_endpoint(event: GithubWebHook) -> GithubWebHook:
    """Handle incoming GitHub webhook events.
    Args:
        event (GithubWebHook): The GitHub webhook event data.

    Returns:
        GithubWebHook: The received GitHub webhook event data.
    """
    log.info(f"Received GitHub event: {event.hook.events}")
    return event
