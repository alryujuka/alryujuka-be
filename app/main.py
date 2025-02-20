from fastapi import FastAPI
from app.database import engine, Base
from app.routers import user_router

# 데이터베이스 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 라우터 등록
app.include_router(user_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with MariaDB!"}