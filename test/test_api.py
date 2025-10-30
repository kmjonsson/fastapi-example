"""Tests for item creation and retrieval endpoints."""

from fastapi_backend.api import api

def test_api():
    x = api("items")
    assert x.prefix == "/api/v1/items"

def test_api_2():
    x = api("/items")
    assert x.prefix == "/api/v1/items"
