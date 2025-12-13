import pytest
from app import auth

def test_hash_password():
    pwd = "secret"
    hashed = auth.hash_password(pwd)
    assert hashed != pwd
    assert auth.pwd_ctx.verify(pwd, hashed)

def test_verify_password():
    pwd = "secret"
    hashed = auth.hash_password(pwd)
    assert auth.verify_password(pwd, hashed)
    assert not auth.verify_password("wrong", hashed)

def test_create_access_token():
    data = {"sub": "testuser"}
    token = auth.create_access_token(data)
    assert token.startswith("token-testuser-")

def test_find_user_by_username():
    # Setup - manually add a user since it uses an in-memory dict
    auth.users.clear()
    user = {"username": "testuser", "email": "test@example.com"}
    auth.users["test@example.com"] = user
    
    found = auth.find_user_by_username("testuser")
    assert found == user
    
    not_found = auth.find_user_by_username("nonexistent")
    assert not_found is None
