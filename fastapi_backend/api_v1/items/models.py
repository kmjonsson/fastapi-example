from pydantic import BaseModel

from fastapi_backend.models.item import DatabaseItem


class Item(BaseModel):
    id: int
    name: str
    description: str
    price: int

    @staticmethod
    def from_orm(db_item: DatabaseItem) -> "Item":
        return Item(
            id=db_item.id,
            name=db_item.name,
            description=db_item.description,
            price=db_item.price,
        )


class CreateItem(BaseModel):
    name: str
    description: str
    price: int
