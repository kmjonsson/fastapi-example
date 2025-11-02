"""Tests for item creation and retrieval endpoints."""


def test_create_get(client):
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


def test_list(client):
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


def test_list_two(client):
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


def test_update(client):
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


def test_delete(client):
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


def test_delete_missing(client):
    """Test deleting a missing item."""
    response = client.delete("/api/v1/items/1")
    assert response.status_code == 404


def test_update_missing(client):
    """Test updating a missing item."""
    response = client.put(
        "/api/v1/items/1",
        json={"name": "Test Item", "description": "A test item", "price": 999},
    )
    assert response.status_code == 404


def test_get_missing(client):
    """Test getting a missing item."""
    response = client.get("/api/v1/items/1")
    assert response.status_code == 404
