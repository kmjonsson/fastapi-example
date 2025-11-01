from pydantic import BaseModel

class GithubWebHookHook(BaseModel):
    id: int
    events: list[str]

    class Config:
        extra = 'ignore'

class GithubWebHook(BaseModel):
    hook_id: int
    hook: GithubWebHookHook

    class Config:
        extra = 'ignore'