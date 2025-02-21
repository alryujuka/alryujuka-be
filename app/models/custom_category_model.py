from sqlalchemy import Column, BigInteger, String
from app.database import Base

class CustomCategory(Base):
    __tablename__ = "custom_category"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False) 
    code = Column(String(100), nullable=False)