from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import create_all, drop_all, get_session
from database.models import Students
from students.schemas import StudentCreate, StudentOut
from .dependency import get_student_by_id


router = APIRouter(
    prefix="/students",
    tags=["students"],
)


@router.get("/{user_id}", response_model=StudentOut)
async def get_user(
    user: Students = Depends(get_student_by_id),
    session: AsyncSession = Depends(get_session)
):
    """
    Получение информации о пользователе по ID.
    """
    return user

# # поиск пользователя
# async def get_student(student_id: int):
#     for student in students:
#         if student["Students_ID"] == student_id:
#             return student
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден!"
#     )

# # поиск студента
# @router.get("/{student_id}", response_model=StudentOut)
# async def find_student(student_id: int):
#     user = get_student(student_id)
#     return user    

# # выполнение функции при запросе пути
# @router.get("/")
# async def read_root():
#     return {"message": "My first FastAPI"}

# # загрузка пользователей
# @router.get("/", response_model=list[StudentOut])
# async def read_students():
#     return students

# # создаем студента
# @router.post("/", response_model=list[StudentOut])
# async def create_student(students_ID: int, fio: str, groups_ID: int, zvan: str = None, session : AsyncSession = Depends(get_session)):
#     student = Students(**students.dict())
#     session.add(student)
#     await session.commit()
#     # students.append(student.dict())
#     return student.dict()

# # обновление студента
# @router.put("/{student_id}")
# async def update_student(students_ID: int, fio: str, groups_ID: int, zvan: str = None):
#     global students
#     students = [s for s in students if s["Students_ID"] != students_ID]
#     student = Students(Students_ID =students_ID, Zvan=zvan, Fio=fio, Groups_ID= groups_ID)
#     students.append(student.dict())
#     return students

# # удаление студента
# @router.delete("/{student_id}")
# async def delete_student(students_ID: int):
#     global students
#     students = [s for s in students if s["Students_ID"] != students_ID]
#     return students
