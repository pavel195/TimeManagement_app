# main.py

from fastapi import FastAPI
from routers import tasks  # Импортируем маршруты задач
from fastapi.middleware.cors import CORSMiddleware  # Импортируем middleware для CORS

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Разрешаем запросы с этого источника
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешаем все заголовки
)

# Подключаем маршруты задач к приложению
app.include_router(tasks.router)

@app.get("/")
def read_root():
    """
    Маршрут для корневого пути.
    """
    return {"message": "Добро пожаловать в приложение Time Management!"}
