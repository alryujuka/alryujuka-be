from pydantic import BaseModel

class RouteBase(BaseModel):
    name: str
    code: str

class RouteResponse(RouteBase):
    id: int

    class Config:
        from_attributes = True