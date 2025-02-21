from sqlalchemy import Column, BigInteger, String
from app.database import Base

class NamulRoute(Base):
    __tablename__ = "namul_route"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    namul = Column(BigInteger, nullable=False) 
    route = Column(BigInteger, nullable=False)