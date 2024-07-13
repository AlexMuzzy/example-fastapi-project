from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_item():
    response = client.post(
        "/items",
        json={"name": "Test Item", "description": "This is a test item"},
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Test Item"

def test_get_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"

def test_list_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) == 1