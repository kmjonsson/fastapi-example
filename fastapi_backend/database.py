from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import os

# Replace with your actual Database credentials
DATABASE_URL = os.environ.get("DATABASE_STRING", "sqlite:///local.db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency to get DB session
def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
