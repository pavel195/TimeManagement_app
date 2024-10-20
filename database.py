# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Строка подключения к базе данных PostgreSQL
# Замените 'time_user' и 'password' на ваши реальные данные
DATABASE_URL = "postgresql://time_user:password@localhost:5432/time_management"

# Создаем движок для подключения к базе данных
engine = create_engine(DATABASE_URL)

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей SQLAlchemy
Base = declarative_base()

def get_db():
    """
    Создает новую сессию базы данных для каждого запроса.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
