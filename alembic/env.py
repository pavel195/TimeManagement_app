from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Импортируйте ваш engine и Base
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Добавляем корень проекта в путь

from database import engine, Base  # Предполагается, что database.py находится в корне проекта

# Этот файл конфигурации Alembic использует файл .ini для настроек.
# Возьмите конфигурацию из alembic.ini и установите переменные.
config = context.config

# Устанавливаем переменные соединения из объекта engine, если они не заданы в alembic.ini
# В данном случае мы не используем sqlalchemy.url из alembic.ini

# Настройка логирования из файла конфигурации alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Добавляем модель (метаданные) для автогенерации миграций
target_metadata = Base.metadata

# Включаем поддержку 'autogenerate'
def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = engine.url
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
