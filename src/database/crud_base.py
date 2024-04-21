from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from .database import Base
from .models import User
from sqlalchemy import update


class CRUDBase:
    model: Base = Base

    @classmethod
    async def create(cls, session: AsyncSession, data: dict) -> model | None:
        """Создание нового объект."""
        try:
            obj = cls.model(**data)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj
        except IntegrityError:
            await session.rollback()
            return None




    @classmethod
    async def get_all(cls, session: AsyncSession) -> list[model]:
        """Получение всех объектов."""
        query = select(cls.model)
        result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    async def get_by_id(cls, session: AsyncSession, id: int) -> model | None:
        """Получение объект по ID."""
        query = select(cls.model).filter(cls.model.id == id)
        result = await session.execute(query)
        return result.scalar_one_or_none()


    # @classmethod
    # async def update(
    #     cls, session: AsyncSession, obj: model, update_data: dict
    # ) -> model | None:
    #     """Обновление данных объекта."""
    #     try:
    #         for key, value in update_data.items():
    #             setattr(obj, key, value)
    #         await session.commit()
    #         return obj
    #     except IntegrityError:
    #         await session.rollback()
    #         return None
        
    @classmethod
    async def update(self, session: AsyncSession, user_id: int, update_data: dict):
        user = await session.query(User).filter(User.id == user_id).first()
        if user:
            for key, value in update_data.items():
                setattr(user, key, value)
            session.add(user)
            await session.commit()
            return user
        return None       

    @classmethod
    async def update_user(self, session: AsyncSession, user_id: int, update_data: dict):
        user = await session.execute(select(User).filter(User.id == user_id))
        user = user.scalar()
        if user:
            update_statement = update(User).where(User.id == user_id).values(update_data)
            await session.execute(update_statement)
            await session.commit()
            return True
        return False
    
    @classmethod
    async def delete(cls, session: AsyncSession, obj: model):
        """Удаление объекта."""
        await session.delete(obj)
        await session.commit()

