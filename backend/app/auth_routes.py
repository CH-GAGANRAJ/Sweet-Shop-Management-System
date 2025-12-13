from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import app.auth as auth

router = APIRouter(prefix="/api/auth", tags=["auth"])

class RegisterIn(BaseModel):
    username: str
    email: str
    password: str
class LoginIn(BaseModel):
    username: str
    password: str
@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(payload: RegisterIn):
    if payload.email in auth.users:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    hashed = auth.hash_password(payload.password)
    user = {
        "id": len(auth.users) + 1,
        "username": payload.username,
        "email": payload.email,
        "password": hashed
    }
    auth.users[payload.email] = user
    return {"id": user["id"], "username": user["username"], "email": user["email"]}

@router.post("/login")
def login(payload: LoginIn):
    user = auth.find_user_by_username(payload.username)
    if not user:
        user = auth.users.get(payload.username)
    if not user or not auth.verify_password(payload.password, user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = auth.create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}
