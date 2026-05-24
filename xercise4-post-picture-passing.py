import pytest
from server import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_post_picture_success(client):
    payload = {
        "title": "Nature Picture",
        "url": "https://example.com/nature.jpg"
    }

    response = client.post("/pictures", json=payload)

    assert response.status_code in [200, 201]

def test_post_picture_without_title(client):
    payload = {
        "url": "https://example.com/sample.jpg"
    }

    response = client.post("/pictures", json=payload)

    assert response.status_code in [400, 422]

def test_post_picture_without_url(client):
    payload = {
        "title": "Sample Picture"
    }

    response = client.post("/pictures", json=payload)

    assert response.status_code in [400, 422]

def test_post_picture_content_type(client):
    payload = {
        "title": "Test",
        "url": "https://example.com/test.jpg"
    }

    response = client.post("/pictures", json=payload)

    assert "application/json" in response.content_type
