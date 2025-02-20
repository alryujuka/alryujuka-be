import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# DB 엔진 생성
engine = create_engine("mysql+pymysql://root:root@mariadb:3306/krampoline")
print(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
    
# 데이터베이스 초기화 함수
def init_db():
    # 엔진을 사용하여 테이블을 자동으로 생성합니다.
    Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 데이터베이스 연결 시 테이블 생성
init_db()
