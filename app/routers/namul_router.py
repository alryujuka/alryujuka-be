from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.views import namul_schema, namul_category_schema
from app.service import namul_service

router = APIRouter(
    prefix="/namuls",
    tags=["namuls"],
)

@router.post("/", response_model=namul_schema.NamulResponse)
def create_namul(namul: namul_schema.NamulCreate, db: Session = Depends(get_db)):
    return namul_service.create_namul(db, namul)

@router.get("/{namul_id}", response_model=namul_schema.NamulResponse)
def read_namul_by_id(namul_id: int, db: Session = Depends(get_db)):
    db_namul = namul_service.get_namul(db, namul_id=namul_id)
    if db_namul is None:
        raise HTTPException(status_code=404, detail="namul not found")
    return db_namul

@router.get("/xy/{lng}/{lat}", response_model=namul_schema.NamulResponse)
def read_namul_by_lat_lng(lat: float, lng: float, db: Session = Depends(get_db)):
    db_namul = namul_service.get_namul_by_lat_lng(db, lat=lat, lng=lng)
    if db_namul is None:
        raise HTTPException(status_code=404, detail="namul not found")
    return db_namul

@router.get("/addr/{addr}", response_model=list[namul_schema.NamulResponse])
def read_namul_by_addr(addr: str, db: Session = Depends(get_db)):
    db_namul = namul_service.get_namul_by_addr(db, addr)
    if db_namul is None:
        raise HTTPException(status_code=404, detail="namul not found")
    return [
        namul_schema.NamulResponse(
            id=namul.id,
            addr=namul.addr,
            latitude=namul.latitude,
            longitude=namul.longitude,
            category=namul_category_schema.NamulCategoryResponse(id=category.id, name=category.name, code=category.code) if category else None
        ) for namul, category in db_namul
    ]

@router.get("/", response_model=list[namul_schema.NamulResponse])
def read_namuls(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    result =     namul_service.get_namuls(db, skip=skip, limit=limit)
    return [
        namul_schema.NamulResponse(
            id=namul.id,
            addr=namul.addr,
            latitude=namul.latitude,
            longitude=namul.longitude,
            category=namul_category_schema.NamulCategoryResponse(id=category.id, name=category.name, code=category.code) if category else None
        ) for namul, category in result
    ]