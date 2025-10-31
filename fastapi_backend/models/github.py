from pydantic import BaseModel


class GithubEvent(BaseModel):
    id: int
    name: str
    description: str
    price: int
