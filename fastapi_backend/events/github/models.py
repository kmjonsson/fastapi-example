"""
Models for GitHub webhook events.
"""

from pydantic import BaseModel, ConfigDict


class GithubWebHookHook(BaseModel):
    """Pydantic model representing the 'hook' part of a GitHub webhook event."""

    id: int
    """The unique identifier of the hook."""
    events: list[str]
    """The list of events that trigger the webhook."""

    # Ignore extra fields in the incoming JSON payload
    model_config = ConfigDict(extra="ignore")


class GithubWebHook(BaseModel):
    """Pydantic model representing a GitHub webhook event."""

    hook_id: int
    """The unique identifier of the webhook."""
    hook: GithubWebHookHook
    """The hook details."""

    # Ignore extra fields in the incoming JSON payload
    model_config = ConfigDict(extra="ignore")
