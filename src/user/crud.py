from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from database.models import User, Student, Group, Department, Discipline, Homework, History, Theme, Visit
from database.crud_base import CRUDBase
from fastapi import HTTPException
from sqlalchemy.orm import selectinload


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
    
    @staticmethod
    async def get_user_fio(session: AsyncSession, username: str) -> User:
        """Получение fio по имени пользователя."""
        query = (
            select(User.fio, Group.name, Homework.name, Theme.name, Visit.data)
            .select_from(User)
            .join(Student, User.id == Student.user_id)
            .join(Group, Student.group_id == Group.id)
            .join(History, History.student_id == Student.user_id)
            .join(Homework, Homework.id == History.homework_id)
            .join(Theme, Theme.id == History.theme_id)
            .join(Visit, Visit.id == History.visit_id)
            .where(User.username == username)
        )
        result = await session.execute(query)
        row = result.fetchone()
        # print(row)
        if row:
            result = {
                'fio': row[0],
                'group_name': row[1],
                'homework': row[2],
                'theme': row[3],
                'date': row[4],
            }
            return result
        else:
            return None

    
    