from pydantic import BaseModel

import datetime

class TaskBase(BaseModel):
    title: str
    description : str
    due_date : datetime.datetime

class TaskCreate(TaskBase): # Используется при получении данных от клиента для создания новой задачи.
    pass

class TaskOut(TaskBase): #  Используется для возврата информации о задаче клиенту, включая её уникальный идентификатор.
    id : int
    class Config:
        orm_mode = True
