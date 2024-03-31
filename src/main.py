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

from database.database import Students
from students.router import router as student_router




# FastAPI
app = FastAPI()

app.include_router(student_router)




@app.get("/update_table")
async def update_table():
    await drop_all()
    await create_all()
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Table updated"})


