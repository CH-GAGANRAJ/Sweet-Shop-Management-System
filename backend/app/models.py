from sqlalchemy import Column, Integer, String, Float
from .db import Base

class Sweet(Base):
    __tablename__ = "sweets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, default="General")
    price = Column(Float)
    quantity = Column(Integer)
