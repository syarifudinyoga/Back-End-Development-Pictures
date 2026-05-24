import pytest
from server import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_get_all_pictures(client):
    response = client.get("/pictures")
    assert response.status_code == 200

def test_get_picture_by_id(client):
    response = client.get("/pictures/1")
    assert response.status_code == 200

def test_get_picture_invalid_id(client):
    response = client.get("/pictures/999")
    assert response.status_code in [200, 404]

def test_get_picture_content_type(client):
    response = client.get("/pictures")
    assert response.content_type == "application/json"

def test_get_picture_response_data(client):
    response = client.get("/pictures")
    assert response.json is not None
