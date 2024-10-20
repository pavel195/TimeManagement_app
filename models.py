from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True) # первичный ключ .
    title = Column(String,  index=True) # заголовок задачи.
    description = Column(String, index = True) # описание задачи.
    due_date = Column(DateTime,default = datetime.datetime.utcnow)
