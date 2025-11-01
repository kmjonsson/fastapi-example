from sqlalchemy.orm import Session
from .models import CreateItem
from fastapi_backend.models.item import DatabaseItem


class CrudItem:
    def __init__(self, db: Session):
        self.db = db

    def list(self) -> list[DatabaseItem]:
        return self.db.query(DatabaseItem).all()

    def create(self, item: CreateItem) -> DatabaseItem:
        db_item = DatabaseItem(**dict(item))
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def get(self, item_id: int) -> DatabaseItem | None:
        return self.db.query(DatabaseItem).filter(DatabaseItem.id == item_id).first()

    def update(self, id: int, new_item: CreateItem) -> DatabaseItem | None:
        item = self.get(id)
        if item:
            item.name = new_item.name
            item.description = new_item.description
            item.price = new_item.price
            self.db.commit()
            self.db.refresh(item)
        return item

    def delete(self, id: int) -> DatabaseItem | None:
        item = self.get(id)
        if item:
            self.db.delete(item)
            self.db.commit()
        return item
