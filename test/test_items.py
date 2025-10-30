"""Tests for item creation and retrieval endpoints."""

from fastapi.testclient import TestClient

from fastapi_backend.database import db, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import pytest

engine = create_engine("sqlite:///test.db")
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


from fastapi_backend.main import app

app.dependency_overrides[db] = _db

client = TestClient(app)


def test_create_get(test_db):
    """Test the creation and retrieval of an item."""
    response = client.post(
        "/api/v1/items",
        json={"name": "Test Item", "description": "A test item", "price": 999},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Test Item",
        "description": "A test item",
        "price": 999,
    }
    response = client.get("/api/v1/items/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Test Item",
        "description": "A test item",
        "price": 999,
    }


def test_list(test_db):
    """Test the creation and retrieval of an item as a list."""
    response = client.post(
        "/api/v1/items",
        json={"name": "Test Item", "description": "A test item", "price": 999},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Test Item",
        "description": "A test item",
        "price": 999,
    }
    response = client.get("/api/v1/items")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Test Item", "description": "A test item", "price": 999}
    ]


def test_list_two(test_db):
    """Test the creation and retrieval of multiple items."""
    response = client.post(
        "/api/v1/items",
        json={"name": "Test Item", "description": "A test item", "price": 999},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Test Item",
        "description": "A test item",
        "price": 999,
    }
    response = client.post(
        "/api/v1/items",
        json={"name": "Test Item", "description": "A test item", "price": 999},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "name": "Test Item",
        "description": "A test item",
        "price": 999,
    }
    response = client.get("/api/v1/items")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Test Item", "description": "A test item", "price": 999},
        {"id": 2, "name": "Test Item", "description": "A test item", "price": 999},
    ]


def test_update(test_db):
    """Test the creation and update of an item."""
    response = client.post(
        "/api/v1/items",
        json={"name": "Test Item", "description": "A test item", "price": 999},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Test Item",
        "description": "A test item",
        "price": 999,
    }
    response = client.put(
        "/api/v1/items/1",
        json={
            "name": "Updated Item",
            "description": "An updated test item",
            "price": 1999,
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Updated Item",
        "description": "An updated test item",
        "price": 1999,
    }
    response = client.get("/api/v1/items/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Updated Item",
        "description": "An updated test item",
        "price": 1999,
    }


def test_delete(test_db):
    """Test the creation and retrieval of an item."""
    response = client.post(
        "/api/v1/items",
        json={"name": "Test Item", "description": "A test item", "price": 999},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Test Item",
        "description": "A test item",
        "price": 999,
    }
    response = client.delete("/api/v1/items/1")
    assert response.status_code == 200


def test_delete_missing(test_db):
    """Test deleting a missing item."""
    response = client.delete("/api/v1/items/1")
    assert response.status_code == 404


def test_update_missing(test_db):
    """Test updating a missing item."""
    response = client.put(
        "/api/v1/items/1",
        json={"name": "Test Item", "description": "A test item", "price": 999},
    )
    assert response.status_code == 404


def test_get_missing(test_db):
    """Test getting a missing item."""
    response = client.get("/api/v1/items/1")
    assert response.status_code == 404
