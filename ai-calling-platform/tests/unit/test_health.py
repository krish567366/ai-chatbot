import pytest
from fastapi.testclient import TestClient
from app.main import app


def test_healthz():
	client = TestClient(app)
	r = client.get('/healthz')
	assert r.status_code == 200
	assert r.json()['status'] == 'ok'