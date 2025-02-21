from sqlalchemy import Column, BigInteger, String
from app.database import Base

class NamulCustomCategory(Base):
    __tablename__ = "namul_custom_category"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    namul = Column(BigInteger, nullable=False) 
    custom_category = Column(BigInteger, nullable=False)