"""Tests for item creation and retrieval endpoints."""

from fastapi_backend.api import create


def test_api():
    x = create("items")
    assert x.prefix == "/api/v1/items"


def test_api_2():
    x = create("/items")
    assert x.prefix == "/api/v1/items"
