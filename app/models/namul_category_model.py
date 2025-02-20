from sqlalchemy import Column, BigInteger, String
from app.database import Base

class NamulCategory(Base):
    __tablename__ = "namul_category"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True) 
    code = Column(String(100), nullable=False, unique=True)