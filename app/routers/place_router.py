from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.service import place_service
import httpx

router = APIRouter(
    prefix="/places",
    tags=["places"],
)

jejuAPI = "https://open.jejudatahub.net/api/proxy/1Dttb1tab8tD88Dtat11111at1t1atD8/5ep52c3o0565co3_2e9r236t96o_rt63"
async def get_data_from_api(api_url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
    
    if response.status_code == 200:
        return response.json()  # JSON 형태로 반환
    else:
        return {"error": "Failed to fetch data"}
    
@router.get("/{num}")
async def save_place(num: str, db: Session = Depends(get_db)):
    # API에서 데이터 가져오기
    place_data = await get_data_from_api(jejuAPI+"?number="+num)
    
    if "error" in place_data:
        return place_data  # 에러 메시지 반환
    
    # return place_data
    # DB에 저장
    place_service.save_data_to_db(db, place_data["data"])
    
    return {"message": "Place saved successfully"}

