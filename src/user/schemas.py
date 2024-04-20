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
    group_id: int

# class StudentCreate(BaseModel):
#     user_id: int
#     group_id: int

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


class DisciplineCreate(BaseModel):
    name: str
    department_id: int
    
class DisciplineOut(DisciplineCreate):
    id: int
    
class ThemeCreate(BaseModel):
    name: str
    discipline_id: int    
    
class HomeworkCreate(BaseModel):
    name: str

class VisitCreate(BaseModel):
    data: str

class HistoryCreate(BaseModel):
    user_id: int
    homework_id: int
    visit_id: int
    theme_id: int
