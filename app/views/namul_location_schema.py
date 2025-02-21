from pydantic import BaseModel
from app.views.namul_category_schema import NamulCategoryResponse

class NamulLocationBase(BaseModel):
    addr: str
    longitude: float
    latitude: float

class NamulLocationCreate(NamulLocationBase):
    category_id: int
    route_id: int
    custom_category_id: list[int]

class NamulLocationResponse(NamulLocationBase):
    category_id: int
    tag: list[str]

    class Config:
        from_attributes = True