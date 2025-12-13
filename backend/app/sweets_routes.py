from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from . import db, auth, models, schemas

router = APIRouter(
    prefix="/api/sweets",
    tags=["sweets"]
)

@router.post("/", response_model=schemas.SweetResponse, status_code=status.HTTP_201_CREATED)
def create_sweet(
    sweet: schemas.SweetCreate, 
    db: Session = Depends(db.get_db),
    current_user: str = Depends(auth.get_current_user)
):

    db_sweet = models.Sweet(
        name=sweet.name,
        category=sweet.category,
        price=sweet.price,
        quantity=sweet.quantity
    )
    db.add(db_sweet)
    db.commit()
    db.refresh(db_sweet)
    return db_sweet

@router.get("/", response_model=List[schemas.SweetResponse])
def read_sweets(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(db.get_db),
    current_user: str = Depends(auth.get_current_user)
):
    return db.query(models.Sweet).offset(skip).limit(limit).all()

@router.post("/{sweet_id}/purchase")
def purchase_sweet(
    sweet_id: int,
    db: Session = Depends(db.get_db),
    current_user: str = Depends(auth.get_current_user)
):
    sweet = db.query(models.Sweet).filter(models.Sweet.id == sweet_id).first()
    
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    if sweet.quantity <= 0:
        raise HTTPException(status_code=400, detail="Out of stock")
    
    sweet.quantity -= 1
    db.commit()
    db.refresh(sweet)
    
    return {"message": "Purchase successful", "remaining_stock": sweet.quantity}