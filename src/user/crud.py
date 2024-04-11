from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from database.models import User, Student, Group, Department, Discipline
from database.crud_base import CRUDBase
from fastapi import HTTPException


class CRUDStudent(CRUDBase):
    model = Student

class CRUDUsers(CRUDBase):
    model = User

class CRUDGroup(CRUDBase):
    model = Group

class CRUDDepartment(CRUDBase):
    model = Department

class CRUDDiscipline(CRUDBase):
    model = Discipline

class CRUDUser(CRUDBase):
    model = User

    @staticmethod
    async def get_user_by_username(session: AsyncSession, username: str) -> User:
        """Получение пользователя по имени пользователя."""
        query = select(User).filter(User.username == username)
        result = await session.execute(query)
        return result.scalar_one_or_none()
