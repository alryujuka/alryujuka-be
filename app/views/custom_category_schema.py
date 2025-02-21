from pydantic import BaseModel

class CustomCategoryBase(BaseModel):
    name: str
    code: str

class CustomCategoryResponse(CustomCategoryBase):
    id: int

    class Config:
        from_attributes = True