from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.views import namul_category_schema
from app.service import namul_category_service

router = APIRouter(
    prefix="/namuls/category",
    tags=["namuls/category"],
)

@router.post("/", response_model=namul_category_schema.NamulCategoryResponse)
def create_namul_category(namul_category: namul_category_schema.NamulCategoryBase, db: Session = Depends(get_db)):
    return namul_category_service.create_namul_category(db, namul_category)

@router.get("/", response_model=list[namul_category_schema.NamulCategoryResponse])
def read_namul_category(db: Session = Depends(get_db)):
    return namul_category_service.get_namul_category(db)