"""
Models for GitHub webhook events.
"""

from pydantic import BaseModel, ConfigDict


class GithubWebHookHook(BaseModel):
    """Pydantic model representing the 'hook' part of a GitHub webhook event."""

    id: int
    events: list[str]

    # Ignore extra fields in the incoming JSON payload
    model_config = ConfigDict(extra="ignore")


class GithubWebHook(BaseModel):
    """Pydantic model representing a GitHub webhook event."""

    hook_id: int
    hook: GithubWebHookHook

    # Ignore extra fields in the incoming JSON payload
    model_config = ConfigDict(extra="ignore")
