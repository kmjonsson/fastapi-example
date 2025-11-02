"""
Pydantic models for items API v1.
"""

from pydantic import BaseModel

from fastapi_backend.models.item import Item as DatabaseItem


class Item(BaseModel):
    """Pydantic model representing an item."""

    id: int
    """The unique identifier of the item."""
    name: str
    """The name of the item."""
    description: str
    """The description of the item."""
    price: int
    """The price of the item."""

    @staticmethod
    def from_orm(db_item: DatabaseItem) -> "Item":
        """Create an Item instance from a DatabaseItem ORM object.

        Args:
            db_item (DatabaseItem): The DatabaseItem ORM object.

        Returns:
            Item: A new Item instance from db_item.
        """
        return Item(
            id=db_item.id,
            name=db_item.name,
            description=db_item.description,
            price=db_item.price,
        )


class PostItem(BaseModel):
    """Pydantic model for creating or updating an item."""

    name: str
    """The name of the item."""
    description: str
    """The description of the item."""
    price: int
    """The price of the item."""
