import asyncio  # Импортирование модуля asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import asyncio

# SQL
DATABASE_URL = "sqlite+aiosqlite:///./db.db"
engine = create_async_engine(DATABASE_URL)

# Базовый класс для моделей
Base = declarative_base()

# функция инициализации и возвращения асинхронного сеанса AsyncSession
async def get_session() -> AsyncSession:
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        yield session

# функция создания таблиц базы данных
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

