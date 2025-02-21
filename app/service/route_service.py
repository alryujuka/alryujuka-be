from sqlalchemy.orm import Session
from app.models.route_model import Route
from app.views.route_schema import RouteBase
from sqlalchemy import asc

def get_route(db: Session):
    return db.query(Route).order_by(asc(Route.id)).all()

def create_route(db: Session, route: RouteBase):
    db_route_category = Route(name=route.name, code=route.code)
    db.add(db_route_category)
    db.commit()
    db.refresh(db_route_category)
    return db_route_category