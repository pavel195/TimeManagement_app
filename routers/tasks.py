from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Task
from schemas import TaskCreate , TaskOut
from typing import List

router = APIRouter(
    prefix='/tasks',
    tags = ['tasks']
)


# Создается новый объект задачи (db_task) на основе данных из task.
# Объект добавляется в сессию базы данных.
# Сессия коммитится, чтобы сохранить изменения в базе данных.
# Объект задачи обновляется с помощью метода refresh(), чтобы получить актуальные данные (например, ID).
# Возвращается созданный объект задачи в формате, определенном в модели TaskOut.
@router.post('/',response_model=TaskOut)
def create_task(task : TaskCreate, db : Session = Depends(get_db)):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

@router.get('/',response_model=List[TaskOut])
def read_tasks(skip : int = 0 , limit : int = 10, db : Session = Depends(get_db)):
    tasks = db.query(Task).offset(skip).limit(limit).all()
    return tasks

