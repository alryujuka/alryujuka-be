from sqlalchemy.orm import Session
from app.models.custom_category_model import CustomCategory
from app.views.custom_category_schema import CustomCategoryBase
from sqlalchemy import asc

def get_custom_category(db: Session):
    return db.query(CustomCategory).order_by(asc(CustomCategory.id)).all()

def create_custom_category(db: Session, cate: CustomCategoryBase):
    db_custom_category = CustomCategory(name=cate.name, code=cate.code)
    db.add(db_custom_category)
    db.commit()
    db.refresh(db_custom_category)
    return db_custom_category