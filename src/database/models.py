from datetime import datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
    DateTime,
    Enum,
    Boolean,
)
from sqlalchemy.orm import declarative_base, relationship
import enum
from sqlalchemy import Sequence

from database.database import Base


class UserType(enum.Enum):
    teacher = "teacher"
    student = "student"
    admin = "admin"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    fio = Column(String)  # Убрали уникальность
    email = Column(String, unique=True)
    password = Column(String)
    user_type = Column(Enum(UserType), default=UserType.student)
    group_id = Column(Integer, ForeignKey("group.id"))
    group = relationship("Group", back_populates="user")
    history_user = relationship("History", back_populates="user_history")

    # student = relationship("Student", back_populates="user", uselist=False)

    def __str__(self):
        return f"User: {self.username} Email: {self.email} ID: {self.id}"


# class Student(Base):
#     __tablename__ = "student"

#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    

    
#     user = relationship("User", back_populates="student")

    

class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    user = relationship("User", back_populates="group")
    

class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    discipline_department = relationship("Discipline", back_populates="department_discipline")


class Discipline(Base):
    __tablename__ = "discipline"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    
    department_id = Column(Integer, ForeignKey("department.id"), nullable=False)

    department_discipline = relationship("Department", back_populates="discipline_department")
    theme_discipline = relationship("Theme", back_populates="discipline_theme")


class Theme(Base):
    __tablename__ = "theme"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    discipline_id = Column(Integer, ForeignKey("discipline.id"), nullable=False)

    discipline_theme = relationship("Discipline", back_populates="theme_discipline")
    history_theme = relationship("History", back_populates="theme_history")


class Homework(Base):
    __tablename__ = "homework"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    history_homework = relationship("History", back_populates="homework_history")


class Visit(Base):
    __tablename__ = "visit"

    id = Column(Integer, primary_key=True)
    data = Column(String, nullable=False)
    visit_status = Column(Boolean)

    history_visit = relationship("History", back_populates="visit_history")


class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    homework_id = Column(Integer, ForeignKey("homework.id"), nullable=False)
    visit_id = Column(Integer, ForeignKey("visit.id"), nullable=False)
    theme_id = Column(Integer, ForeignKey("theme.id"), nullable=False)

    user_history = relationship("User", back_populates="history_user")
    homework_history = relationship("Homework", back_populates="history_homework")
    visit_history = relationship("Visit", back_populates="history_visit")
    theme_history = relationship("Theme", back_populates="history_theme")


