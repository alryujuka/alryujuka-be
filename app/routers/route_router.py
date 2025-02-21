from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.views import route_schema
from app.service import route_service

router = APIRouter(
    prefix="/route",
    tags=["route"],
)

@router.post("/", response_model=route_schema.RouteResponse)
def create_route(route: route_schema.RouteBase, db: Session = Depends(get_db)):
    return route_service.create_route(db, route)

@router.get("/", response_model=list[route_schema.RouteResponse])
def read_route(db: Session = Depends(get_db)):
    return route_service.get_route(db)