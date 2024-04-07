from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, condecimal, validator
from enum import Enum


class UserBase(BaseModel):
    username: str
    telephone: str

class UserCreate(UserBase):
    password: str
    username: str
    
class UserUpdate(UserBase):
    password: Optional[str]
    telephone: Optional[str]
    username: Optional[str]


class UserOut(UserBase):
    id: int
