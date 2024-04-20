from fastapi import APIRouter, Request, Depends, status, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from user.dependency import get_correct_user_frontend, get_current_user
from user.crud import CRUDUser, CRUDGroup, CRUDDiscipline, CRUDTheme, CRUDHomework, CRUDHistory
from database.models import User
from database.database import get_session
from .dependency import get_user_or_redirect


router = APIRouter(prefix="", tags=["frontend"])

templates = Jinja2Templates(directory="frontend/template")


@router.get("/auth")
async def get_login(
    request: Request,
    user: User | None = Depends(get_correct_user_frontend),
    not_auth: bool | None = None,
):
    # if user:
    #     return RedirectResponse(url="/", status_code=status.HTTP_301_MOVED_PERMANENTLY)
    return templates.TemplateResponse(
        "auth.html", {"request": request, "not_auth": not_auth}
    )


@router.get("/logout", response_class=RedirectResponse)
async def get_logout():
    response = RedirectResponse(url="/")
    response.delete_cookie("access_token")
    return response


@router.get("/register")
async def get_register(
    request: Request, user: User | None = Depends(get_correct_user_frontend)
):
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/group")
async def add_group(
    request: Request,
    user: User = Depends(get_user_or_redirect),
    name: str = Form(...),
    session: AsyncSession = Depends(get_session),
):
    data = {"name": name}
    group = await CRUDGroup.create(session, data)
    return RedirectResponse(url="/prepod", status_code=301)


@router.post("/homework")
async def add_homework(
    request: Request,
    user: User = Depends(get_user_or_redirect),
    name: str = Form(...),
    session: AsyncSession = Depends(get_session),
):
    data = {"name": name}
    homework = await CRUDHomework.create(session, data)
    return RedirectResponse(url="/prepod", status_code=301)


@router.get("/student")
async def get_user(
    request: Request,
    user: User = Depends(get_user_or_redirect),
    session: AsyncSession = Depends(get_session),
):
    data = await CRUDUser.get_user_fio(session, user.username)


    data = [
        {"id": i, **dct}
        for i, dct in enumerate(data, start=1)
    ]
    print(data)
    users = await CRUDUser.get_all(session)
    groups = await CRUDGroup.get_all(session)
    disciplines = await CRUDDiscipline.get_all(session)

    return templates.TemplateResponse(
        "student/student.html",
        {
            "request": request,
            "user": user,
            "data": data,
            "users": users,
            "groups": groups,
            "disciplines": disciplines,
        },
    )


@router.get("/prepod")
async def get_users(
    request: Request,
    user: User = Depends(get_user_or_redirect),
    session: AsyncSession = Depends(get_session),
):
    data = await CRUDUser.get_user_fio(session, user.username)
    data = data 

    data = [
        {"id": i, **dct}
        for i, dct in enumerate(data, start=1)
    ]
    print(data)
    users = await CRUDUser.get_all(session)
    groups = await CRUDGroup.get_all(session)
    disciplines = await CRUDDiscipline.get_all(session)
    themes = await CRUDTheme.get_all(session)
    homeworks = await CRUDHomework.get_all(session)
    students = await CRUDUser.get_all(session)


    return templates.TemplateResponse(
        "prepod/prepod.html",
        {
            "request": request,
            "user": user,
            "data": data,
            "users": users,
            "groups": groups,
            "disciplines": disciplines,
            "themes": themes,
            "homeworks": homeworks,
            "students": students,
        },
    )


@router.post("/theme")
async def add_theme(
    request: Request,
    user: User = Depends(get_user_or_redirect),
    name: str = Form(...),
    discipline_id: int = Form(...),
    session: AsyncSession = Depends(get_session),
):
    data = {"name": name, "discipline_id": discipline_id}
    theme = await CRUDTheme.create(session, data)
    return RedirectResponse(url="/prepod", status_code=301)

@router.post("/user-group")
async def create_user(
    request: Request,
    user: User = Depends(get_user_or_redirect),
    user_id: int = Form(...),
    group_id: int = Form(...),
    session: AsyncSession = Depends(get_session),
):
    data = {"id": user_id, "group_id": group_id}
    user = await CRUDUser.create(session, data)
    return RedirectResponse(url="/prepod", status_code=301)





@router.post("/theme-homework")
async def theme_homework(
    request: Request,
    user: User = Depends(get_user_or_redirect),
    theme_id: int = Form(...),
    homework_id: int = Form(...),
    user_id: int = Form(...),
    session: AsyncSession = Depends(get_session),
):
    data = {"user_id": user_id, "homework_id": homework_id, "visit_id":1, "theme_id": theme_id}
    history = await CRUDHistory.create(session, data)
    return RedirectResponse(url="/prepod", status_code=301)




@router.get("/")
async def get_index(
    request: Request, user: User | None = Depends(get_correct_user_frontend)
):
    return templates.TemplateResponse("index.html", {"request": request, "user": user})
