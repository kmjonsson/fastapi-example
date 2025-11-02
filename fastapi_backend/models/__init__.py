"""Database models initialization."""

from fastapi_backend.database import Base, engine


def init_models(engine=engine):
    """Initialize database models."""
    Base.metadata.create_all(bind=engine)
