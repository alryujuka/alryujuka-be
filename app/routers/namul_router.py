from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.views import namul_schema, namul_category_schema
from app.service import namul_service
import json


router = APIRouter(
    prefix="/namuls",
    tags=["namuls"],
)

@router.post("/", response_model=namul_schema.NamulResponse)
def create_namul(namul: namul_schema.NamulCreate, db: Session = Depends(get_db)):
    return namul_service.create_namul(db, namul)

@router.get("/{namul_id}", response_model=namul_schema.NamulResponse)
def read_namul_by_id(namul_id: int, db: Session = Depends(get_db)):
    db_namul = namul_service.get_namul(db, namul_id=namul_id)
    if db_namul is None:
        raise HTTPException(status_code=404, detail="namul not found")
    return db_namul

@router.get("/xy/{lng}/{lat}", response_model=namul_schema.NamulResponse)
def read_namul_by_lat_lng(lat: float, lng: float, db: Session = Depends(get_db)):
    db_namul = namul_service.get_namul_by_lat_lng(db, lat=lat, lng=lng)
    if db_namul is None:
        raise HTTPException(status_code=404, detail="namul not found")
    return db_namul

@router.get("/addr/{addr}", response_model=list[namul_schema.NamulResponse])
def read_namul_by_addr(addr: str, db: Session = Depends(get_db)):
    db_namul = namul_service.get_namul_by_addr(db, addr)
    if db_namul is None:
        raise HTTPException(status_code=404, detail="namul not found")
    return [
        namul_schema.NamulResponse(
            id=namul.id,
            addr=namul.addr,
            latitude=namul.latitude,
            longitude=namul.longitude,
            category=namul_category_schema.NamulCategoryResponse(id=category.id, name=category.name, code=category.code) if category else None
        ) for namul, category in db_namul
    ]

@router.get("/", response_model=list[namul_schema.NamulResponse])
def read_namuls(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    #json 문자열 데이터
    employee_string = """[
    {
        "addr": "제주특별자치도 제주시 첨단로 242",
        "longitude": 126.57,
        "latitude": 33.4506,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 남원읍 하례리 산 1-7",
        "longitude": 126.57,
        "latitude": 33.3567,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 월평동 665-1",
        "longitude": 126.58,
        "latitude": 33.4589,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 월평동 산 6",
        "longitude": 126.592,
        "latitude": 33.3972,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 한경면 고산리 3760",
        "longitude": 126.163,
        "latitude": 33.2948,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 삼양일동 555-2",
        "longitude": 126.599,
        "latitude": 33.5175,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 봉개동 산 3",
        "longitude": 126.603,
        "latitude": 33.4653,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 봉개동 산 78-38",
        "longitude": 126.607,
        "latitude": 33.4063,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 남원읍 하례리",
        "longitude": 126.605,
        "latitude": 33.3052,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 상효동 2364",
        "longitude": 126.601,
        "latitude": 33.2953,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 봉개동 165",
        "longitude": 126.616,
        "latitude": 33.4774,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 명림로 584",
        "longitude": 126.617,
        "latitude": 33.4331,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 봉개동 산 78-2",
        "longitude": 126.611,
        "latitude": 33.4198,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 봉개동 234-231",
        "longitude": 126.622,
        "latitude": 33.4588,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 봉개동 산 78-1",
        "longitude": 126.627,
        "latitude": 33.4339,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 조천읍 교래리 산 137-4",
        "longitude": 126.623,
        "latitude": 33.3843,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 남원읍 한남리 산 2-12",
        "longitude": 126.628,
        "latitude": 33.3614,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 남원읍 신례리 산 2-4",
        "longitude": 126.622,
        "latitude": 33.3401,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 조천읍 교래리 산 137-1",
        "longitude": 126.634,
        "latitude": 33.3941,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 남원읍 한남리 산 2-1",
        "longitude": 126.646,
        "latitude": 33.3402,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 조천읍 교래리 산 108",
        "longitude": 126.654,
        "latitude": 33.4538,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 남원읍 한남리 산 15-2",
        "longitude": 126.661,
        "latitude": 33.319,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 한림읍 협재리 산 100-1",
        "longitude": 126.227,
        "latitude": 33.4095,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 한경면 조수리 1277",
        "longitude": 126.223,
        "latitude": 33.3359,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 표선면 가시리 산 158",
        "longitude": 126.664,
        "latitude": 33.3918,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 한경면 조수리 134",
        "longitude": 126.239,
        "latitude": 33.3356,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 남원읍 위미리 산 132-2",
        "longitude": 126.677,
        "latitude": 33.301,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 한경면 저지리 51",
        "longitude": 126.251,
        "latitude": 33.3341,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 조천읍 선흘리 산 154",
        "longitude": 126.685,
        "latitude": 33.4514,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 조천읍 교래리 산 45",
        "longitude": 126.685,
        "latitude": 33.4439,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 조천읍 교래리 산 44",
        "longitude": 126.684,
        "latitude": 33.4392,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 표선면 가시리 산 158-2",
        "longitude": 126.688,
        "latitude": 33.41,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 표선면 가시리 산 158-2",
        "longitude": 126.688,
        "latitude": 33.4021,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 남원읍 수망리 산 188",
        "longitude": 126.692,
        "latitude": 33.3684,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 한림읍 상명리 산 5",
        "longitude": 126.261,
        "latitude": 33.3657,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 대정읍 상모리 3540-2",
        "longitude": 126.259,
        "latitude": 33.2387,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 조천읍 선흘리 산 112",
        "longitude": 126.699,
        "latitude": 33.4678,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 조천읍 선흘리 산 103-1",
        "longitude": 126.709,
        "latitude": 33.4464,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 남원읍 의귀리 531",
        "longitude": 126.715,
        "latitude": 33.3062,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 한림읍 명월리",
        "longitude": 126.279,
        "latitude": 33.3826,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 대정읍 상모리 1593-2",
        "longitude": 126.281,
        "latitude": 33.2065,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 조천읍 선흘리 산 84",
        "longitude": 126.715,
        "latitude": 33.4773,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 조천읍 교래리 산 2",
        "longitude": 126.718,
        "latitude": 33.4422,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 남원읍 수망리 127",
        "longitude": 126.724,
        "latitude": 33.3308,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 한림읍 금악리 2785-1",
        "longitude": 126.291,
        "latitude": 33.3729,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 대정읍 인성리 21-2",
        "longitude": 126.288,
        "latitude": 33.2429,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 표선면 가시리 산 68-9",
        "longitude": 126.73,
        "latitude": 33.3991,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 남원읍 신흥리 산 18",
        "longitude": 126.736,
        "latitude": 33.3489,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 한림읍 금악리 산 1-1",
        "longitude": 126.306,
        "latitude": 33.3546,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 구좌읍 김녕리 2723",
        "longitude": 126.745,
        "latitude": 33.5437,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 구좌읍 송당리 산 84-2",
        "longitude": 126.741,
        "latitude": 33.4596,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 구좌읍 송당리 산 297",
        "longitude": 126.741,
        "latitude": 33.4235,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 표선면 가시리 산 10-5",
        "longitude": 126.746,
        "latitude": 33.3743,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 애월읍 봉성리 3920-35",
        "longitude": 126.308,
        "latitude": 33.4206,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 구좌읍 덕천리 864",
        "longitude": 126.748,
        "latitude": 33.4922,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 구좌읍 덕천리 산 2",
        "longitude": 126.749,
        "latitude": 33.4657,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 구좌읍 송당리 산 140-2",
        "longitude": 126.749,
        "latitude": 33.4431,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 표선면 성읍리 3196",
        "longitude": 126.751,
        "latitude": 33.3966,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 표선면 가시리 산 63",
        "longitude": 126.753,
        "latitude": 33.3887,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 서귀포시 표선면 가시리 산 8",
        "longitude": 126.748,
        "latitude": 33.367,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주특별자치도 제주시 한림읍 금악리 105-1",
        "longitude": 126.324,
        "latitude": 33.3405,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주도",
        "longitude": 1.1,
        "latitude": 2.2,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    },
    {
        "addr": "제주도2",
        "longitude": 1.1,
        "latitude": 2.2,
        "category": {
        "name": "고사리",
        "code": "nav-gosari.svg",
        "id": 1
        }
    }
    ]"""
    json_object = json.loads(employee_string)
    return json_object
    # result = namul_service.get_namuls(db, skip=skip, limit=limit)
    # return [
    #     namul_schema.NamulResponse(
    #         id=namul.id,
    #         addr=namul.addr,
    #         latitude=namul.latitude,
    #         longitude=namul.longitude,
    #         category=namul_category_schema.NamulCategoryResponse(id=category.id, name=category.name, code=category.code) if category else None
    #     ) for namul, category in result
    # ]