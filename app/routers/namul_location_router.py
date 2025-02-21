from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.views import namul_location_schema
from app.service import namul_location_service

router = APIRouter(
    prefix="/location",
    tags=["location"],
)

@router.post("/save", response_model=namul_location_schema.NamulLocationResponse)
def save_location(namul: namul_location_schema.NamulLocationCreate, db: Session = Depends(get_db)):
    result = namul_location_service.create_namul(db, namul)
    tag = []
    route=result.get("route", "")
    if route:
        tag.append(route)
    for item in result["custom_category"]:
        tag.append(item[0])
    return namul_location_schema.NamulLocationResponse(
        addr=result["namul"].addr,
        latitude=result["namul"].latitude,
        longitude=result["namul"].longitude,
        category_id=1,
        tag = tag
    )