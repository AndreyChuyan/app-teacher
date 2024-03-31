# https://fastapi.tiangolo.com/
# https://github.com/zhanymkanov/fastapi-best-practices
# https://docs.pydantic.dev/latest/
# https://jinja.palletsprojects.com/en/3.1.x/ 
# pip install fastapi[all]
# для запуска
# uvicorn main:app --reload
# документация
# http://127.0.0.1:8000/docs

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi import status

from pydantic import BaseModel
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

# !!!!!!!!!!!!!!!!!!!!!
# ошибка тут!
from database.database import Students

# функция из базы данных
from database.database import create_all, drop_all, get_session

class StudentsI(BaseModel):
    # Students_ID: int
    Zvan: str | None = None
    Fio: str
    Password: str
    Groups_ID: int



# FastAPI
app = FastAPI()

students = [
    {"Students_ID": 1, "Zvan": "curs", "Fio": "Ivanov", "Groups_ID": 1},
    {"Students_ID": 2, "Zvan": "curs", "Fio": "Petrov", "Groups_ID": 2},
    {"Students_ID": 3, "Zvan": "curs", "Fio": "Sidorov", "Groups_ID": 1},
]


# поиск пользователя
async def get_student(student_id: int):
    for student in students:
        if student["Students_ID"] == student_id:
            return student
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден!"
    )
    

# выполнение функции при запросе пути
@app.get("/")
async def read_root():
    return {"message": "My first FastAPI"}

# загрузка пользователей
@app.get("/students/", response_model=list[StudentsI])
async def read_students():
    return students

# поиск студента
@app.get("/students/{student_id}", response_model=StudentsI)
async def find_student(student_id: int):
    user = get_student(student_id)
    return user

# создаем студента
@app.post("/students/", response_model=list[StudentsI])
async def create_student(students_ID: int, fio: str, groups_ID: int, zvan: str = None, session : AsyncSession = Depends(get_session)):
    student = Students(**students.dict())
    session.add(student)
    await session.commit()
    # students.append(student.dict())
    return student.dict()





# обновление студента
@app.put("/students/{student_id}")
async def update_student(students_ID: int, fio: str, groups_ID: int, zvan: str = None):
    global students
    students = [s for s in students if s["Students_ID"] != students_ID]
    student = StudentsI(Students_ID =students_ID, Zvan=zvan, Fio=fio, Groups_ID= groups_ID)
    students.append(student.dict())
    return students

# удаление студента
@app.delete("/students/{student_id}")
async def delete_student(students_ID: int):
    global students
    students = [s for s in students if s["Students_ID"] != students_ID]
    return students

@app.get("/update_table")
async def update_table():
    await drop_all()
    await create_all()
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Table updated"})


