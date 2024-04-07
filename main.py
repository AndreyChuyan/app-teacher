

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi import status

from pydantic import BaseModel
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

# from database.database import Students
from students.router import router as student_router
from database.models import Groups, Students, Department, Discipline, Theme, Homework, Visit, History
from database.database import create_tables, get_session


from user.router import router as user_router


# FastAPI
app = FastAPI()

# app.include_router(student_router)
app.include_router(user_router)


@app.get("/create_tables")
async def create_all_tables():
    '''Создадим базу данных'''
    await create_tables()
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Table updated"})


