"""
Database setup and session management for FastAPI application.
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Replace with your actual Database credentials
DATABASE_URL = os.environ.get("DATABASE_STRING", "sqlite:///local.db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""

    pass


def db():
    """Yield a database session.

    Dependency to get DB sessions for FastAPI routes.

    Yields:
        Session: SQLAlchemy Session object.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
