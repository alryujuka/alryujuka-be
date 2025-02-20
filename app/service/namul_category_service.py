from sqlalchemy.orm import Session
from app.models.namul_category_model import NamulCategory
from app.views.namul_category_schema import NamulCategoryBase
from sqlalchemy import asc

def get_namul_category(db: Session):
    return db.query(NamulCategory).order_by(asc(NamulCategory.id)).all()

def create_namul_category(db: Session, namul: NamulCategoryBase):
    db_namul_category = NamulCategory(name=namul.name, code=namul.code)
    db.add(db_namul_category)
    db.commit()
    db.refresh(db_namul_category)
    return db_namul_category