from passlib.context import CryptContext
from typing import Dict, Optional
import secrets

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

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
