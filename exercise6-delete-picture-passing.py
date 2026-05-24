import pytest
from server import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_update_picture(client):
    payload = {
        "title": "Updated Picture",
        "url": "https://example.com/updated.jpg"
    }

    response = client.put("/pictures/1", json=payload)

    assert response.status_code in [200, 204]

def test_update_picture_invalid_id(client):
    payload = {
        "title": "Invalid Update",
        "url": "https://example.com/invalid.jpg"
    }

    response = client.put("/pictures/999", json=payload)

    assert response.status_code in [404, 400]

def test_delete_picture(client):
    response = client.delete("/pictures/1")

    assert response.status_code in [200, 204]

def test_delete_picture_invalid_id(client):
    response = client.delete("/pictures/999")

    assert response.status_code in [404, 400]
