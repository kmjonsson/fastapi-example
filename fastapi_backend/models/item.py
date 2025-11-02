"""SQLAlchemy models for items."""

from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column

from fastapi_backend.database import Base


class Item(Base):
    """SQLAlchemy model representing an item."""

    __tablename__ = "items"
    id = mapped_column(Integer, primary_key=True, index=True)
    """The unique identifier of the item."""
    name = mapped_column(String(255), index=True)
    """The name of the item."""
    description = mapped_column(String(255), index=True)
    """The description of the item."""
    price = mapped_column(Integer)
    """The price of the item."""
