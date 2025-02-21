from sqlalchemy import Column, BigInteger, String
from app.database import Base
from sqlalchemy.orm import relationship

class Route(Base):
    __tablename__ = "route"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False) 
    code = Column(String(100), nullable=False)