from sqlalchemy.orm import Session
from app.models.namul_model import Namul
from app.models.namul_route_model import NamulRoute
from app.models.namul_custom_category_model import NamulCustomCategory
from app.models.route_model import Route
from app.models.custom_category_model import CustomCategory
from app.views.namul_location_schema import NamulLocationCreate
from sqlalchemy.exc import IntegrityError

def create_namul(db: Session, namul: NamulLocationCreate):
    db_namul = Namul(addr=namul.addr, longitude=namul.longitude, latitude=namul.latitude, category_id=namul.category_id)
    db.add(db_namul)
    try:
        db.commit()
        db.refresh(db_namul)
        db_route = NamulRoute(namul=db_namul.id, route=namul.route_id)
        db.add(db_route)
        db.commit()
        db.refresh(db_route)
        for id in namul.custom_category_id:
            db.add(NamulCustomCategory(namul=db_namul.id, custom_category=id))
        db.commit()
        route = db.query(Route).filter(Route.id == namul.route_id).first()
        custom_category = db.query(CustomCategory.name) \
            .select_from(NamulCustomCategory) \
            .outerjoin(CustomCategory, NamulCustomCategory.custom_category == CustomCategory.id) \
            .filter(NamulCustomCategory.namul == db_namul.id).all()
        return {"route": route.name, "namul": db_namul, "custom_category": custom_category}
    except IntegrityError:
        db.rollback()
        raise ValueError("does not exist.")
    
    