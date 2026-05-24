import pytest
from server import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200

def test_count(client):
    response = client.get("/count")
    assert response.status_code == 200
