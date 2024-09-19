# backend/test_app.py
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={"text": "Hello"})
    assert response.status_code == 200
    assert "label" in response.json()
    assert "score" in response.json()

def test_feedback():
    response = client.post("/feedback", json={"text": "Hello", "feedback": "positive"})
    assert response.status_code == 200
    assert response.json() == {"status": "Feedback received"}

