from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.views import custom_category_schema
from app.service import custom_category_service

router = APIRouter(
    prefix="/custom/category",
    tags=["custom/category"],
)

@router.post("/", response_model=custom_category_schema.CustomCategoryResponse)
def create_custom_category(custom_category: custom_category_schema.CustomCategoryBase, db: Session = Depends(get_db)):
    return custom_category_service.create_custom_category(db, custom_category)

@router.get("/", response_model=list[custom_category_schema.CustomCategoryResponse])
def read_custom_category(db: Session = Depends(get_db)):
    return custom_category_service.get_custom_category(db)