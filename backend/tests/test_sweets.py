from fastapi.testclient import TestClient
from app.main import app
from app import auth, db, models
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup test DB
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_sweets.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[db.get_db] = override_get_db

# Mock auth so tests don't fail properly authenticated routes
def override_get_current_user():
    return "testuser"

app.dependency_overrides[auth.get_current_user] = override_get_current_user

client = TestClient(app)

@pytest.fixture(autouse=True)
def run_around_tests():
    models.Base.metadata.create_all(bind=engine)
    yield
    models.Base.metadata.drop_all(bind=engine)

def test_add_sweet():
    res = client.post("/api/sweets/", json={
        "name": "Ladoo",
        "price": 10.0,
        "quantity": 50,
        "category": "Traditional"
    })
    assert res.status_code == 201
    assert res.json()["name"] == "Ladoo"
    assert "id" in res.json()

def test_list_sweets():
    # Helper to add sweet first
    client.post("/api/sweets/", json={
        "name": "Jalebi",
        "price": 15.0,
        "quantity": 20
    })
    res = client.get("/api/sweets/")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
    assert len(res.json()) >= 1

def test_purchase_sweet():
    # 1. Add sweet
    create_res = client.post("/api/sweets/", json={
        "name": "Barfi",
        "price": 20.0,
        "quantity": 10
    })
    sweet_id = create_res.json()["id"]

    # 2. Purchase sweet (using correct URL with ID)
    res = client.post(f"/api/sweets/{sweet_id}/purchase")
    assert res.status_code == 200
    assert res.json()["remaining_stock"] == 9

def test_purchase_insufficient_stock():
    # 1. Add sweet with 0 quantity
    create_res = client.post("/api/sweets/", json={
        "name": "EmptyLadoo",
        "price": 10.0,
        "quantity": 0
    })
    sweet_id = create_res.json()["id"]

    # 2. Try to purchase
    res = client.post(f"/api/sweets/{sweet_id}/purchase")
    assert res.status_code == 400
    assert res.json()["detail"] == "Out of stock"
