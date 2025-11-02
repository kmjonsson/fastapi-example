import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Replace with your actual Database credentials
DATABASE_URL = os.environ.get("DATABASE_STRING", "sqlite:///local.db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


# Dependency to get DB session
def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
