from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 설정 (React와 FastAPI가 다른 포트에서 실행되므로 필요)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React 서버 주소
    allow_methods=["*"],
    allow_headers=["*"],
)

class CalculationRequest(BaseModel):
    a: float
    b: float

@app.post("/calculate")
def calculate(data: CalculationRequest):
    result = data.a + data.b
    return {"result": result}
