from fastapi.testclient import TestClient
from app.main import app
from app import auth

client = TestClient(app)

def setup_function():
    auth.users.clear()

def test_register_user():
    response = client.post(
        "/api/auth/register",
        json={"username": "newuser", "email": "new@example.com", "password": "password123"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "newuser"
    assert data["email"] == "new@example.com"
    assert "id" in data

def test_register_existing_email():
    user_data = {"username": "user1", "email": "existing@example.com", "password": "pwd"}
    client.post("/api/auth/register", json=user_data)
    
    response = client.post("/api/auth/register", json=user_data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"

def test_login_success():
    client.post(
        "/api/auth/register",
        json={"username": "loginuser", "email": "login@example.com", "password": "securepassword"}
    )
    
    response = client.post(
        "/api/auth/login",
        json={"username": "loginuser", "password": "securepassword"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_password():
    client.post(
        "/api/auth/register",
        json={"username": "wrongpass", "email": "wrong@example.com", "password": "securepassword"}
    )
    
    response = client.post(
        "/api/auth/login",
        json={"username": "wrongpass", "password": "wrongpassword"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"

def test_login_nonexistent_user():
    response = client.post(
        "/api/auth/login",
        json={"username": "ghost", "password": "password"}
    )
    assert response.status_code == 401
