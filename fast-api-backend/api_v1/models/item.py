from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: int

class CreateItem(BaseModel):
    name: str
    description: str
    price: int

class DatabaseItem(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(String(255), index=True)
    price = Column(Integer)

    def to_item(self):
        return Item(
            id=self.id,
            name=self.name,
            description=self.description,
            price=self.price
        )

