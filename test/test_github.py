"""Tests for item creation and retrieval endpoints."""

from fastapi.testclient import TestClient

from fastapi_backend.database import db, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import pytest

from fastapi_backend.main import app

client = TestClient(app)

def test_event():
    response = client.post(
        "/events/github",
        json={"hook_id": 578418866,"hook": {"id": 578418866,"events": ["push" ]}}
    )
    assert response.status_code == 200
