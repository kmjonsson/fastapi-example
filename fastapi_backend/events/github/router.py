from fastapi_backend.models.github import GithubEvent

from fastapi import APIRouter

api = APIRouter(prefix="/events/github")


@api.post("/")
async def events_github_endpoint(event: GithubEvent):
    return {"detail": "GitHub event received"}
