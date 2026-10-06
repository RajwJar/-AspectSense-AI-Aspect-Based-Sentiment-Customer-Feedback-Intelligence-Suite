"""
Unit tests for FastAPI REST Endpoints
"""

import pytest
from fastapi.testclient import TestClient
from code.api.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "AspectSense AI Engine"
    assert "version" in data


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_aspects_endpoint(client):
    response = client.get("/api/v1/aspects")
    assert response.status_code == 200
    data = response.json()
    assert "aspect_categories" in data


def test_analyze_endpoint(client):
    payload = {
        "review_text": "Great noise cancellation, but ear pads make ears sweat.",
        "domain": "Audio & Headphones",
        "include_llm_diagnostics": True
    }
    response = client.post("/api/v1/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "overall_assessment" in data
    assert "aspect_analysis" in data
    assert data["pipeline_status"] == "SUCCESS"


def test_analyze_empty_text(client):
    payload = {"review_text": "   "}
    response = client.post("/api/v1/analyze", json=payload)
    assert response.status_code == 400
