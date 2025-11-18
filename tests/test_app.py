import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Example test for the root endpoint
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Mergington High School" in response.text

# Example test for the activities endpoint
def test_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Example test for signing up a participant
def test_signup():
    response = client.post("/activities/Soccer/signup", params={"email": "test@mergington.edu"})
    assert response.status_code == 200
    assert "message" in response.json()