from sqlalchemy.orm import Session
from app.models.namul_model import Namul
from sqlalchemy.exc import IntegrityError

def save_data_to_db(db: Session, place_data: dict):
    for place in place_data:
        addr=place.get("addressDoro", None)
        if addr is None:
            addr=place["addressJibun"]

        db_namul = Namul(addr=addr, longitude=place["longitude"], latitude=place["latitude"], category_id=1)
        db.add(db_namul)
    try:
        db.commit()
        db.refresh(db_namul)
        return db_namul
    except IntegrityError:
        db.rollback()
        raise ValueError("Category ID does not exist.")