from sqlalchemy import create_engine # для создания подключения к базе данных.
from sqlalchemy.ext.declarative import declarative_base # для создания базового класса для моделей.
from sqlalchemy.orm import sessionmaker # для создания объектов сессии, которые позволяют взаимодействовать с базой данных.

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5433/time_management"


engine = create_engine(SQLALCHEMY_DATABASE_URL) # создает объект движка SQLAlchemy, который выполняет SQL-запросы.

SessionLocal = sessionmaker(bind=engine) # создается фабрика сессий, которая будет использовать движок для создания новых объектов сессии.

Base = declarative_base() #  базовый класс, от которого будут наследоваться все модели (таблицы)

def get_db(): # получение сессии базы данных
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
