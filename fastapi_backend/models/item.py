"""SQLAlchemy models for items."""

from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column

from fastapi_backend.database import Base


class Item(Base):
    """SQLAlchemy model representing an item."""

    __tablename__ = "items"
    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String(255), index=True)
    description = mapped_column(String(255), index=True)
    price = mapped_column(Integer)
