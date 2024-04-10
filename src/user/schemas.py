from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, condecimal, validator
from enum import Enum


class UserType(str, Enum):
    student = "student"
    teacher = "teacher"
    admin = "admin"


class UserBase(BaseModel):
    username: str
    fio: str
    email: EmailStr
    user_type: UserType


class StudentBase(BaseModel):
    group_id: int


class UserCreate(UserBase):
    password: str

    student: Optional[StudentBase] = None


class UserOut(UserBase):
    id: int

class UserUpdate(BaseModel):
    username: str | None = None
    fio: str | None = None
    email: EmailStr | None = None
    user_type: UserType | None = None



class GroupCreate(BaseModel):
    name: str

class GroupOut(GroupCreate):
    id: int


class DepartmentCreate(BaseModel):
    name: str

class DepartmentOut(GroupCreate):
    id: int
