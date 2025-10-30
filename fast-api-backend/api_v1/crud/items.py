from sqlalchemy.orm import Session
from ..models.item import Item

class CrudItem:
    def __init__(self, db: Session):
        self.db = db

    def get(self, item_id: int):
        return self.db.query(Item).filter(Item.id == item_id).first()

    def create(self, name: str, description: str, price: int):
        db_item = Item(name=name, description=description, price=price)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
    
    def update(self, item_id: int, name: str, description: str, price: int):
        item = self.get(item_id)
        if item:
            item.name = name
            item.description = description
            item.price = price
            self.db.commit()
            self.db.refresh(item)
        return item
    
    def delete(self, item_id: int):
        item = self.get(item_id)
        if item:
            self.db.delete(item)
            self.db.commit()
        return item