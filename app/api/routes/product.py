from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.product_schema import ProductCreate, ProductResponse
from app.models.product import Product

router = APIRouter(prefix="/product", tags=["Product"])

@router.get("/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.post("/", response_model=ProductResponse)
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    obj = Product(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj