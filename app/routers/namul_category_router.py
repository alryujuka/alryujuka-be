from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.views import namul_category_schema
from app.service import namul_category_service
import json

router = APIRouter(
    prefix="/namuls/category",
    tags=["namuls/category"],
)

@router.post("/", response_model=namul_category_schema.NamulCategoryResponse)
def create_namul_category(namul_category: namul_category_schema.NamulCategoryBase, db: Session = Depends(get_db)):
    employee_string = """[
    {
      "name": "고사리",
      "code": "nav-gosari.svg",
      "id": 1
    },
    {
      "name": "두릅",
      "code": "nav-durup.svg",
      "id": 2
    },
    {
      "name": "꿩마농",
      "code": "nav-kkungmanung.svg",
      "id": 3
    },
    {
      "name": "취나물",
      "code": "nav-gosari.svg",
      "id": 4
    },
    {
      "name": "냉이",
      "code": "nav-gosari.svg",
      "id": 5
    },
    {
      "name": "근거리",
      "code": "",
      "id": 6
    },
    {
      "name": "찜",
      "code": "",
      "id": 7
    }
    ]"""
    return json.loads(employee_string)
    # return namul_category_service.create_namul_category(db, namul_category)

@router.get("/", response_model=list[namul_category_schema.NamulCategoryResponse])
def read_namul_category(db: Session = Depends(get_db)):
    return namul_category_service.get_namul_category(db)