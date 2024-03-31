from fastapi import HTTPException, status
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Students

# поиск пользователя
async def get_student(session: AsyncSession, student_id: int):
    student = await select(Students).filter(Students.id == student_id)
    student = await session.execute(student)
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден!")
    return student

async def get_students(session: AsyncSession, student_data: dict):
    student = Students(**student_data)
    session.add(student)
    await session.commit()
    return student