from pydantic import BaseModel
from app.views.namul_category_schema import NamulCategoryResponse

class NamulBase(BaseModel):
    addr: str
    longitude: float
    latitude: float

class NamulCreate(NamulBase):
    category_id: int

class NamulResponse(NamulBase):
    category: NamulCategoryResponse

    class Config:
        from_attributes = True
