from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware


# Создаем экземпляр FastAPI
app = FastAPI()

# Настроим CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем запросы с любых источников (будьте осторожны на продакшн)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Модель для проверки данных
class UserData(BaseModel):
    name: str
    email: str

# Эндпоинт для приема данных
@app.post("/submit")
async def submit_data(user_data: UserData):
    return {"name": user_data.name, "email": user_data.email}
