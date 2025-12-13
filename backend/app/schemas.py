from pydantic import BaseModel
from typing import Optional

class SweetBase(BaseModel):
    name: str
    category: Optional[str] = "General"
    price: float
    quantity: int

class SweetCreate(SweetBase):
    pass

class SweetResponse(SweetBase):
    id: int

    class Config:
        from_attributes = True
