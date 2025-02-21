from fastapi import FastAPI
from app.database import engine, Base
from app.routers import user_router, namul_category_router, namul_router, place_router
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi.responses import RedirectResponse

# 데이터베이스 생성
Base.metadata.create_all(bind=engine)

app = FastAPI(openapi_prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(user_router.router)
app.include_router(namul_category_router.router)
app.include_router(namul_router.router)
app.include_router(place_router.router)

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
