# pip install aiosqlite
import asyncio  # Импортирование модуля asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import asyncio

# SQL
DATABASE_URL = "sqlite+aiosqlite:///./database/db.db"
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
Base = declarative_base()

# функция инициализации и возвращения асинхронного сеанса AsyncSession
async def get_session() -> AsyncSession:
    async with engine.begin() as conn:
        async with AsyncSession(engine, class_=AsyncSession) as session:
            yield session

# функция создания таблиц базы данных
async def create_all():
    async with engine.begin() as conn:
        # await conn.run_sync(Students.metadata.create_all)
        await conn.run_sync(Base.metadata.create_all)

# функция удаления базы данных
async def drop_all():
    async with engine.begin() as conn:
        # await conn.run_sync(Students.metadata.drop_all)
        await conn.run_sync(Base.metadata.drop_all)

