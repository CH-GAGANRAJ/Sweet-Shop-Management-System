from passlib.context import CryptContext
from typing import Dict, Optional
import secrets
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

users: Dict[str, Dict] = {}

def hash_password(password: str) -> str:
    return pwd_ctx.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_ctx.verify(plain_password, hashed_password)

def create_access_token(data: Dict) -> str:
    sub = data.get("sub") or data.get("username") or "user"
    return f"token-{sub}-{secrets.token_hex(8)}"

def find_user_by_username(username: str) -> Optional[Dict]:
    for u in users.values():
        if u["username"] == username:
            return u
    return None

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Simple mock token validation for now since create_access_token just returns a string
    if not token.startswith("token-"):
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Extract username helper (mock implementation)
    try:
        # format: token-{username}-{random}
        parts = token.split("-")
        if len(parts) < 3:
             raise HTTPException(status_code=401, detail="Invalid token")
        username = parts[1]
        return username
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
