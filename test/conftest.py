import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi_backend import app
from fastapi_backend.database import Base, db

engine = create_engine("sqlite:////tmp/test.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


# Dependency to get DB session
async def _db():
    new_db = SessionLocal()
    try:
        yield new_db
    finally:
        new_db.close()


app.dependency_overrides[db] = _db


@pytest.fixture()
def client(test_db):
    return TestClient(app)
