# routers/tasks.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Task
from schemas import TaskCreate, Task as TaskSchema

router = APIRouter(
    prefix="/tasks",  # Префикс для всех маршрутов в этом роутере
    tags=["tasks"]    # Теги для группировки в документации Swagger
)

@router.post("/", response_model=TaskSchema)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    """
    Создание новой задачи.
    """
    # Проверка, что заголовок задачи не пустой
    if not task.title.strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty")

    # Создаем экземпляр модели Task из данных схемы TaskCreate
    db_task = Task(**task.dict())

    # Добавляем задачу в сессию базы данных
    db.add(db_task)

    # Фиксируем изменения (сохраняем в базе данных)
    db.commit()

    # Обновляем объект db_task, чтобы получить автоматически сгенерированные поля (например, id)
    db.refresh(db_task)

    return db_task  # Возвращаем созданную задачу

@router.get("/", response_model=List[TaskSchema])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка задач с пагинацией.
    """
    # Запрашиваем задачи из базы данных с применением пагинации
    tasks = db.query(Task).offset(skip).limit(limit).all()
    return tasks  # Возвращаем список задач

@router.get("/{task_id}", response_model=TaskSchema)
def read_task(task_id: int, db: Session = Depends(get_db)):
    """
    Получение задачи по ID.
    """
    # Находим задачу по ID
    task = db.query(Task).filter(Task.id == task_id).first()

    # Если задача не найдена, возвращаем ошибку 404
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task  # Возвращаем найденную задачу

@router.put("/{task_id}", response_model=TaskSchema)
def update_task(task_id: int, updated_task: TaskCreate, db: Session = Depends(get_db)):
    """
    Обновление существующей задачи по ID.
    """
    # Находим задачу по ID
    task = db.query(Task).filter(Task.id == task_id).first()

    # Если задача не найдена, возвращаем ошибку 404
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    # Обновляем поля задачи новыми данными
    task.title = updated_task.title
    task.description = updated_task.description
    task.due_date = updated_task.due_date

    # Фиксируем изменения в базе данных
    db.commit()

    # Обновляем объект task, чтобы получить последние данные
    db.refresh(task)

    return task  # Возвращаем обновленную задачу

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Удаление задачи по ID.
    """
    # Находим задачу по ID
    task = db.query(Task).filter(Task.id == task_id).first()

    # Если задача не найдена, возвращаем ошибку 404
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    # Удаляем задачу из базы данных
    db.delete(task)

    # Фиксируем изменения (удаляем из базы данных)
    db.commit()

    return {"message": "Task deleted successfully"}  # Возвращаем сообщение об успешном удалении
