from fastapi import FastAPI
from app.database import engine, Base
from app.routers import user_router, namul_category_router
import os

# 데이터베이스 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 라우터 등록
app.include_router(user_router.router)
app.include_router(namul_category_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with MariaDB!"}

@app.get("/api/test")
def test():
    return {"message": "OK"}

@app.get("/api/env")
def get_env():
    database_url = os.environ.get("DATABASE_URL", "환경 변수 없음")
    return {"DATABASE_URL": database_url}