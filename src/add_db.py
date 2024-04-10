from fastapi import APIRouter, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import RedirectResponse, Response

from user.exceptions import exception_user_not_found, exception_auth, exception_unique_field
from database.database import Base, engine, get_session
from user.crud import CRUDUser, CRUDStudent, CRUDGroup, CRUDDepartment
from user.schemas import UserCreate, UserOut, GroupCreate, DepartmentCreate
from database.models import Group
import asyncio

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
    DepartmentCreate(name="Плавания"),
    DepartmentCreate(name="Легкой атлетики")
]



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



async def create_departments(departments, session):
    created_departments = []
    for department in departments:
        new_department = await CRUDDepartment.create(session, department.dict())
        created_departments.append(new_department)
    return created_departments

async def add_department():
    session = get_session()
    async for s in session:
        created_departments = await create_departments(new_departments, s)
        for department in created_departments:
            if department is not None:
                print(f"Добавлена кафедра: {department.name}")

asyncio.run(add_department())