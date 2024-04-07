from fastapi import Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.requests import Request

from database.database import get_session
from .crud import CRUDUser
from .exceptions import exception_student_not_found


async def get_student_by_id(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await CRUDUser.get_by_id(session, user_id)       # поиск пользователя по заданному ID
    if user is None:
        raise exception_student_not_found
    return user