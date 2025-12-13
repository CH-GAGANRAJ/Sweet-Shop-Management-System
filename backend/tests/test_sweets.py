from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_sweet():
    res = client.post("/api/sweets", json={
        "name": "Ladoo",
        "price": 10,
        "quantity": 50
    })
    assert res.status_code == 201
    assert res.json()["name"] == "Ladoo"

def test_list_sweets():
    res = client.get("/api/sweets")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_purchase_sweet():
    res = client.post("/api/sweets/purchase", json={
        "name": "Ladoo",
        "quantity": 5
    })
    assert res.status_code == 200
    assert res.json()["remaining_quantity"] == 45

def test_purchase_insufficient_stock():
    res = client.post("/api/sweets/purchase", json={
        "name": "Ladoo",
        "quantity": 500
    })
    assert res.status_code == 400
