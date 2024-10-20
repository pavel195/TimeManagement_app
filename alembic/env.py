from logging.config import fileConfig
import sys
import os

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Добавляем путь к корню проекта
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Импортируем SQLALCHEMY_DATABASE_URL и Base из database.py
from database import SQLALCHEMY_DATABASE_URL, Base
import models  # Импортируем ваши модели

# Этот файл конфигурации Alembic использует файл .ini для настроек.
config = context.config

# Устанавливаем строку подключения к базе данных
config.set_main_option('sqlalchemy.url', SQLALCHEMY_DATABASE_URL)

# Настройка логирования из файла конфигурации alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Добавляем модель (метаданные) для автогенерации миграций
target_metadata = Base.metadata

def run_migrations_offline():
    """Запуск миграций в оффлайн режиме."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Запуск миграций в онлайн режиме."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
