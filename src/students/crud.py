from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound

from database.crud_base import CRUDBase
from fastapi import HTTPException

from database.models import Students

class CRUDUser(CRUDBase):
    model = Students

    @staticmethod
    async def get_user_by_username(session: AsyncSession, username: str) -> Students:
        """Получение пользователя по имени пользователя."""
        query = select(Students).filter(Students.Fio == username)
        result = await session.execute(query)
        return result.scalar_one_or_none()


# # поиск пользователя
# async def get_student(session: AsyncSession, student_id: int):
#     student = await select(Students).filter(Students.id == student_id)
#     student = await session.execute(student)
#     if student is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден!")
#     return student


# async def get_students(session: AsyncSession, student_data: dict):
#     student = Students(**student_data)
#     session.add(student)
#     await session.commit()
#     return student