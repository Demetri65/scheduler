# tests/integration/test_api.py
import pytest
from fastapi.testclient import TestClient
from calendar_agent.api.v1 import app

client = TestClient(app)

@pytest.mark.integration          # <-- mark it
def test_schedule_endpoint():
    # Supply the API token header so you get 200 instead of 401
    resp = client.post(
        "/v1/schedule",
        headers={"X-API-KEY": "change-me"},   # must match API_TOKEN env var
        json={"prompt": "Ping test"},
    )
    assert resp.status_code == 200
    # Basic sanity check on reply field
    assert "Ping" in resp.json()["reply"]