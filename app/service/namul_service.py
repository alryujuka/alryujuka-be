from sqlalchemy.orm import Session
from app.models.namul_model import Namul
from app.views.namul_schema import NamulCreate

def get_namul(db: Session, namul_id: int):
    return db.query(Namul).filter(Namul.id == namul_id).first()

def get_namul_by_lat_lng(db: Session, lat: float, lng: float):
    return db.query(Namul).filter(
            Namul.latitude == lat,
            Namul.longitude == lng
        ).first()

def get_namul_by_addr(db: Session, addr: str):
    return db.query(Namul).filter(Namul.addr.ilike(f"%{addr}%")).first()

def get_namuls(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Namul).offset(skip).limit(limit).all()

def create_namul(db: Session, namul: NamulCreate):
    db_namul = Namul(name=namul.name, addr=namul.addr, longitude=namul.longitude, latitude=namul.latitude, category_id=namul.category_id)
    db.add(db_namul)
    db.commit()
    db.refresh(db_namul)
    return db_namul