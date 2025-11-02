"""Tests for item creation and retrieval endpoints."""


def test_event(client):
    response = client.post(
        "/events/github",
        json={"hook_id": 578418866, "hook": {"id": 578418866, "events": ["push"]}},
    )
    assert response.status_code == 200
