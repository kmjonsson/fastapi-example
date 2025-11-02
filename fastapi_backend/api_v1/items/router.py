"""
API v1 router for items.
"""

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from fastapi_backend.api import create as create_api
from fastapi_backend.database import db

from .crud import CrudItem
from .models import Item, PostItem

api = create_api("items")


@api.get("/")
async def list_item_endpoint(db: Session = Depends(db)) -> list[Item]:
    """List all items.
    Args:
        db (Session): Database session dependency.

    Returns:
        list[Item]: A list of all items.
    """
    return [Item.from_orm(i) for i in CrudItem(db).list()]


@api.post("/")
async def create_item_endpoint(item: PostItem, db: Session = Depends(db)) -> Item:
    """Create a new item.
    Args:
        item (PostItem): The item data to create.
        db (Session): Database session dependency.

    Returns:
        Item: The created item.
    """
    return Item.from_orm(CrudItem(db).create(item))


@api.get("/{item_id}")
async def get_item_endpoint(item_id: int, db: Session = Depends(db)) -> Item:
    """Get an item by its ID.
    Args:
        item_id (int): The ID of the item to retrieve.
        db (Session): Database session dependency.

    Returns:
        Item: The retrieved item.
    """
    item = CrudItem(db).get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item.from_orm(item)


@api.put("/{item_id}")
async def update_item_endpoint(
    item_id: int, new_item: PostItem, db: Session = Depends(db)
) -> Item:
    """Update an existing item by its ID.
    Args:
        item_id (int): The ID of the item to update.
        new_item (PostItem): The new item data.
        db (Session): Database session dependency.

    Returns:
        Item: The updated item.
    """
    item = CrudItem(db).update(item_id, new_item)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return Item.from_orm(item)


@api.delete("/{item_id}")
async def delete_item_endpoint(item_id: int, db: Session = Depends(db)):
    """Delete an item by its ID.
    Args:
        item_id (int): The ID of the item to delete.
        db (Session): Database session dependency.

    Returns:
        dict: A message indicating the result of the deletion.
    """
    item = CrudItem(db).delete(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"detail": "Item deleted"}
