from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from fastapi_backend.api import create as create_api
from fastapi_backend.database import db

from .crud import CrudItem
from .models import CreateItem, Item

api = create_api("items")


@api.get("/")
async def list_item_endpoint(db: Session = Depends(db)) -> list[Item]:
    return [Item.from_orm(i) for i in CrudItem(db).list()]


@api.post("/")
async def create_item_endpoint(item: CreateItem, db: Session = Depends(db)) -> Item:
    return Item.from_orm(CrudItem(db).create(item))


@api.get("/{item_id}")
async def get_item_endpoint(item_id: int, db: Session = Depends(db)) -> Item:
    item = CrudItem(db).get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item.from_orm(item)


@api.put("/{item_id}")
async def update_item_endpoint(
    item_id: int, new_item: CreateItem, db: Session = Depends(db)
) -> Item:
    item = CrudItem(db).update(item_id, new_item)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return Item.from_orm(item)


@api.delete("/{item_id}")
async def delete_item_endpoint(item_id: int, db: Session = Depends(db)):
    item = CrudItem(db).delete(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"detail": "Item deleted"}
