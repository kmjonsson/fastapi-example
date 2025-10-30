from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import db
from ..models.item import CreateItem, Item
from ..crud.items import CrudItem

from api import api

api = api('items')

@api.post("/")
async def create_item_endpoint(item : CreateItem, db: Session = Depends(db)) -> Item:
    return CrudItem(db).create(item).to_item()

@api.get("/{item_id}")
async def get_item_endpoint(item_id: int, db: Session = Depends(db)) -> Item:
    item = CrudItem(db).get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item.to_item()

@api.put("/{item_id}")
async def update_item_endpoint(item_id: int, name: str, description: str, price: int, db: Session = Depends(db)) -> Item:
    item = CrudItem(db).update(item_id, name, description, price)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return item.to_item()

@api.delete("/{item_id}")
async def delete_item_endpoint(item_id: int, db: Session = Depends(db)):
    item = CrudItem(db).delete(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
   
    return {"detail": "Item deleted"}