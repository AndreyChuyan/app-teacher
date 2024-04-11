from fastapi import APIRouter, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import RedirectResponse, Response
from sqlalchemy.future import select

from user.auth import hash_password

from user.exceptions import exception_user_not_found, exception_auth, exception_unique_field
from database.database import Base, engine, get_session
from user.crud import CRUDUser, CRUDStudent, CRUDGroup, CRUDDepartment, CRUDDiscipline, CRUDUsers
from user.schemas import UserCreate, UserOut, GroupCreate, DepartmentCreate, DisciplineCreate, ThemeCreate, HomeworkCreate, VisitCreate, HistoryCreate
from database.models import Group, Discipline, Theme, Homework, Visit, History, User
import asyncio

# # Добавление пользователей
new_users = [
    UserCreate(username="user1", fio="Иванов Иван Сергеевич", email="123@mail.ru", user_type = "teacher", password = "test"),
    UserCreate(username="user2", fio="Петров Петр Иванович", email="222@mail.ru", user_type = "student", password = "test"),
    UserCreate(username="user3", fio="Сидоров Сидор Сидорин", email="3333@mail.ru", user_type = "student", password = "test"),
    UserCreate(username="user4", fio="Лапин Лаповский Лапович", email="4444@mail.ru", user_type = "student", password = "test")
    
]



# # Добавление групп
new_groups = [
    GroupCreate(name="Group7"),
    GroupCreate(name="Group8"),
    GroupCreate(name="Group9")
]

# # Добавление кафедр
new_departments = [
    DepartmentCreate(name="Иностранного языка"),
    DepartmentCreate(name="Русского языка"),
    DepartmentCreate(name="Математики"),
    DepartmentCreate(name="Легкой атлетики")
]

# # Добавление дисциплин
new_disciplines = [
    DisciplineCreate(name="Информатика", department_id=1),
    DisciplineCreate(name="Английский язык", department_id=1),
    DisciplineCreate(name="Математический анализ", department_id=2),
    DisciplineCreate(name="Высшая математика", department_id=2)
]

# # Добавление тем
new_themes = [
    ThemeCreate(name="Word", discipline_id=1),
    ThemeCreate(name="Exel", discipline_id=1),
    ThemeCreate(name="Corel", discipline_id=1),
    ThemeCreate(name="Словосочетания", discipline_id=2)
]

# # Добавление ДЗ
new_homeworks = [
    HomeworkCreate(name="изучить Word"),
    HomeworkCreate(name="изучить Exel"),
    HomeworkCreate(name="Corel"),
    HomeworkCreate(name="изучить Corel")
]

# # Добавление Визита
new_visits = [
    VisitCreate(data="25.03.24"),
    VisitCreate(data="26.03.24"),
    VisitCreate(data="27.03.24"),
    VisitCreate(data="28.03.24")
]

# # Добавление Истории
new_history = [
    HistoryCreate(student_id= 1, homework_id= 1, visit_id= 1, theme_id= 1),
    HistoryCreate(student_id= 2, homework_id= 2, visit_id= 2, theme_id= 2),
    HistoryCreate(student_id= 3, homework_id= 2, visit_id= 2, theme_id= 2),
    HistoryCreate(student_id= 2, homework_id= 2, visit_id= 2, theme_id= 2)
]


# Блок добавления студентов
async def create_users(users, session):
    created_list = []
    for date in users:
        existing_user = await session.execute(select(User).filter_by(username=date.username))
        existing_user = existing_user.scalar_one_or_none()
        if not existing_user:
            date.password = hash_password(date.password)
            disc = User(username=date.username, fio=date.fio, email=date.email, password=date.password, user_type=date.user_type)
            session.add(disc)
            await session.commit()
            created_list.append(disc)
    return created_list

async def add_users():
    session = get_session()
    async for s in session:
        created_objects = await create_users(new_users, s)
        for obj in created_objects:
            if obj is not None:
                print(f"Добавлен пользователь с именем: {obj.fio}")

asyncio.run(add_users())










# Блок добавления групп
async def create_groups(groups, session):
    created_groups = []
    for group in groups:
        new_group = await CRUDGroup.create(session, group.dict())
        created_groups.append(new_group)
    return created_groups

async def add_group():
    session = get_session()
    async for s in session:
        created_groups = await create_groups(new_groups, s)
        for group in created_groups:
            if group is not None:
                print(f"Добавлена группа: {group.name}")

asyncio.run(add_group())


# Блок добавления кафедр
async def create_departments(departments, session):
    created_departments = []
    for department in departments:
        new_department = await CRUDDepartment.create(session, department.dict())
        created_departments.append(new_department)
    return created_departments

async def add_department():
    session = get_session()
    async for s in session:
        created_objects = await create_departments(new_departments, s)
        for object in created_objects:
            if object is not None:
                print(f"Добавлена кафедра: {object.name}")

asyncio.run(add_department())


# Блок добавления дисциплин
async def create_discipline(disciplines, session):
    created_list = []
    for disc_data in disciplines:
        existing_discipline = await session.execute(select(Discipline).filter_by(name=disc_data.name))
        existing_discipline = existing_discipline.scalar_one_or_none()
        if not existing_discipline:
            disc = Discipline(name=disc_data.name, department_id=disc_data.department_id)
            session.add(disc)
            await session.commit()
            created_list.append(disc)
    return created_list

async def add_discipline():
    session = get_session()
    async for s in session:
        created_objects = await create_discipline(new_disciplines, s)
        for obj in created_objects:
            if obj is not None:
                print(f"Добавлена дисциплина: {obj.name}")

asyncio.run(add_discipline())

# Блок добавления тем
async def create_theme(themes, session):
    created_list = []
    for data in themes:
        existing_discipline = await session.execute(select(Theme).filter_by(name=data.name))
        existing_discipline = existing_discipline.scalar_one_or_none()
        if not existing_discipline:
            disc = Theme(name=data.name, discipline_id=data.discipline_id)
            session.add(disc)
            await session.commit()
            created_list.append(disc)
    return created_list

async def add_theme():
    session = get_session()
    async for s in session:
        created_objects = await create_theme(new_themes, s)
        for obj in created_objects:
            if obj is not None:
                print(f"Добавлена тема: {obj.name}")

asyncio.run(add_theme())

# Блок добавления ДЗ
async def create_homework(homeworks, session):
    created_list = []
    for data in homeworks:
        existing_discipline = await session.execute(select(Homework).filter_by(name=data.name))
        existing_discipline = existing_discipline.scalar_one_or_none()
        if not existing_discipline:
            disc = Homework(name=data.name)
            session.add(disc)
            await session.commit()
            created_list.append(disc)
    return created_list

async def add_homework():
    session = get_session()
    async for s in session:
        created_objects = await create_homework(new_homeworks, s)
        for obj in created_objects:
            if obj is not None:
                print(f"Добавлена домашка: {obj.name}")

asyncio.run(add_homework())

# Блок добавление визита
async def create_visit(visits, session):
    created_list = []
    for date in visits:
        existing_discipline = await session.execute(select(Visit).filter_by(data=date.data))
        existing_discipline = existing_discipline.scalar_one_or_none()
        if not existing_discipline:
            disc = Visit(data=date.data)
            session.add(disc)
            await session.commit()
            created_list.append(disc)
    return created_list

async def add_visit():
    session = get_session()
    async for s in session:
        created_objects = await create_visit(new_visits, s)
        for obj in created_objects:
            if obj is not None:
                print(f"Добавлена дата: {obj.data}")

asyncio.run(add_visit())

# Блок добавление истории
async def create_history(history, session):
    created_list = []
    for date in history:
        existing_discipline = await session.execute(select(History).filter_by(student_id=date.student_id))
        existing_discipline = existing_discipline.scalar_one_or_none()
        if not existing_discipline:
            disc = History(student_id=date.student_id, homework_id=date.homework_id, visit_id=date.visit_id, theme_id=date.theme_id)
            session.add(disc)
            await session.commit()
            created_list.append(disc)
    return created_list

async def add_history():
    session = get_session()
    async for s in session:
        created_objects = await create_history(new_history, s)
        for obj in created_objects:
            if obj is not None:
                print(f"Добавлена история id: {obj.id}")

asyncio.run(add_history())
