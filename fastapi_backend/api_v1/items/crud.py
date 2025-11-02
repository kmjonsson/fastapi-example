"""
CRUD operations for Item model.
"""

from sqlalchemy.orm import Session

from fastapi_backend.models.item import Item as DatabaseItem

from .models import CreateItem


class CrudItem:
    """CRUD operations for Item model."""

    def __init__(self, db: Session):
        """Initialize with a database session."""
        self.db = db

    def list(self) -> list[DatabaseItem]:
        """List all items in the database.

        Returns:
            list[DatabaseItem]: A list of all items.
        """
        return self.db.query(DatabaseItem).all()

    def create(self, item: CreateItem) -> DatabaseItem:
        """Create a new item in the database.

        Args:
            item (CreateItem): The item data to create.

        Returns:
            DatabaseItem: The created item.
        """
        db_item = DatabaseItem(**dict(item))
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def get(self, item_id: int) -> DatabaseItem | None:
        """Get an item by its ID.

        Args:
            item_id (int): The ID of the item to retrieve.

        Returns:
            DatabaseItem | None: The item if found, else None.
        """
        return self.db.query(DatabaseItem).filter(DatabaseItem.id == item_id).first()

    def update(self, id: int, new_item: CreateItem) -> DatabaseItem | None:
        """Update an existing item by its ID.

        Args:
            id (int): The ID of the item to update.
            new_item (CreateItem): The new item data.

        Returns:
            DatabaseItem | None: The updated item if it existed, else None.
        """
        item = self.get(id)
        if item:
            item.name = new_item.name
            item.description = new_item.description
            item.price = new_item.price
            self.db.commit()
            self.db.refresh(item)
        return item

    def delete(self, id: int) -> DatabaseItem | None:
        """
        Delete an item by its ID.

        Args:
            id (int): The ID of the item to delete.

        Returns:
            DatabaseItem | None: The deleted item if it existed, else None.
        """
        item = self.get(id)
        if item:
            self.db.delete(item)
            self.db.commit()
        return item
