from pydantic import BaseModel

class NamulCategoryBase(BaseModel):
    name: str
    code: str

class NamulCategoryResponse(NamulCategoryBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True