# schemas.py

from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    """
    Базовая схема задачи с общими полями.
    """
    title: str
    description: str
    due_date: datetime

class TaskCreate(TaskBase):
    """
    Схема для создания новой задачи.
    Наследуется от TaskBase и может содержать дополнительные поля при необходимости.
    """
    pass

class Task(TaskBase):
    """
    Схема для отображения задачи с дополнительными полями.
    """
    id: int
    created_at: datetime

    class Config:
        orm_mode = True  # Включаем поддержку ORM для автоматического преобразования
