from sqlalchemy.orm import Session
from app.models.namul_model import Namul
from app.models.namul_category_model import NamulCategory
from app.views.namul_schema import NamulCreate
from sqlalchemy.exc import IntegrityError

def get_namul(db: Session, namul_id: int):
    return db.query(Namul).filter(Namul.id == namul_id).first()

def get_namul_by_lat_lng(db: Session, lat: float, lng: float):
    return db.query(Namul).filter(
        Namul.latitude.between(lat - 0.001, lat + 0.001),
        Namul.longitude.between(lng - 0.001, lng + 0.001)
        ).first()

def get_namul_by_addr(db: Session, addr: str):
    return db.query(Namul, NamulCategory)\
        .join(NamulCategory, Namul.category_id == NamulCategory.id, isouter=True)\
        .filter(Namul.addr.ilike(f"%{addr}%")).all()

def get_namuls(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Namul, NamulCategory)\
        .join(NamulCategory, Namul.category_id == NamulCategory.id, isouter=True)\
        .offset(skip).limit(limit).all()

def create_namul(db: Session, namul: NamulCreate):
    db_namul = Namul(addr=namul.addr, longitude=namul.longitude, latitude=namul.latitude, category_id=namul.category_id)
    db.add(db_namul)
    try:
        db.commit()
        db.refresh(db_namul)
        return db_namul
    except IntegrityError:
        db.rollback()
        raise ValueError("Category ID does not exist.")