import os

from dotenv import load_dotenv
from openai import OpenAI

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실습용 설정
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cars = [
    {"id": 1, "name": "Sonata", "company": "HYUNDAI", "price": 2500, "year": 2023},
    {"id": 2, "name": "Avante", "company": "HYUNDAI", "price": 2200, "year": 2024},
    {"id": 3, "name": "K5", "company": "KIA", "price": 2900, "year": 2023},
]

class CarCreate(BaseModel):
    name: str
    company: str
    price: int
    year: int

class ChatRequest(BaseModel):
    message: str

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.post("/api/ai/chat")
def ai_chat(request: ChatRequest):
    # 사용자의 질문을 OpenAI API로 보낸다.
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=request.message
    )

    return {
        "message": "AI 응답 생성 성공",
        "data": {
            "question": request.message,
            "answer": response.output_text
        }
    }


@app.get("/")
def home():
    return {
        "message": "FastAPI 서버 실행 중"
    }


@app.get("/cars")
def get_cars():
    # 전체 자동차 목록 반환
    return {
        "message": "자동차 목록 조회 성공",
        "data": cars
    }
    
@app.get("/cars/{car_id}")
def get_car(car_id: int):
    # car_id와 일치하는 자동차 찾기
    for car in cars:
        if car["id"] == car_id:
            return {
                "message": "자동차 상세 조회 성공",
                "data": car
            }

    return {
        "message": "해당 자동차를 찾을 수 없습니다.",
        "data": None
    }

@app.post("/cars")
def create_car(car: CarCreate):
    # 현재 목록 개수를 기준으로 새 id 생성
    new_car = {
        "id": len(cars) + 1,
        "name": car.name,
        "company": car.company,
        "price": car.price,
        "year": car.year
    }

    cars.append(new_car)

    return {
        "message": "자동차 등록 성공",
        "data": new_car
    }
    




