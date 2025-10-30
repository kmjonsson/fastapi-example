from sqlalchemy.orm import Session
from ..models.item import DatabaseItem, Item

class CrudItem:
    def __init__(self, db: Session):
        self.db = db

    def create(self, item: Item) -> DatabaseItem:
        db_item = DatabaseItem(name=item.name, description=item.description, price=item.price)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
    
    def get(self, item_id: int) -> DatabaseItem:
        return self.db.query(DatabaseItem).filter(DatabaseItem.id == item_id).first()

    def update(self, item_id: int, name: str, description: str, price: int) -> DatabaseItem:
        item = self.get(item_id)
        if item:
            item.name = name
            item.description = description
            item.price = price
            self.db.commit()
            self.db.refresh(item)
        return item
    
    def delete(self, item_id: int) -> DatabaseItem:
        item = self.get(item_id)
        if item:
            self.db.delete(item)
            self.db.commit()
        return item