from sqlalchemy import Column, BigInteger, String, DateTime, ForeignKey, DateTime, Float
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy.orm import relationship

class Namul(Base):
    __tablename__ = "namuls"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    addr = Column(String(255), nullable=False)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    # category_id = Column(BigInteger, ForeignKey("category.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime, server_default=func.now())

    # category = relationship("NamulCategory", back_populates="namuls")
    # likes = relationship("Like", back_populates="namuls", cascade="all, delete")
    # visitors = relationship("Visitor", back_populates="namuls", cascade="all, delete")
    # routes = relationship("NamulRouteType", back_populates="namuls", cascade="all, delete")
    # custom_type = relationship("NamulCustomType", back_populates="namuls", cascade="all, delete")