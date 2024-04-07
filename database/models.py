from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Boolean, Numeric, DateTime, Enum
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Sequence
from sqlalchemy import join
import enum

# подключаем базу данных
from .database import Base
from .database import engine

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    telephone = Column(String, unique=True)
    password = Column(String)

    def __str__(self):
        return f"User: {self.username} Email: {self.telephone} ID: {self.id}"

class Groups(Base):
    __tablename__ = 'Groups'

    Groups_ID = Column(Integer, Sequence('group_id_seq'), primary_key=True)
    Groups_name = Column(String, unique=True, nullable=False)
    
    students_group = relationship("Students", back_populates="group_students")

class Students(Base):
    __tablename__ = 'Students'

    Students_ID = Column(Integer, Sequence('student_id_seq'), primary_key=True)
    Zvan = Column(String)
    Fio = Column(String, unique=True, nullable=False)
    Password = Column(String)
    Groups_ID = Column(Integer, ForeignKey('Groups.Groups_ID'), nullable=False)
    
    group_students = relationship("Groups", back_populates="students_group")
    history_students = relationship("History", back_populates="students_history")
    
class Department(Base):
    __tablename__ = 'Department'

    Department_ID = Column(Integer, Sequence('Department_id_seq'), primary_key=True)
    Department_name = Column(String, unique=True, nullable=False)
    
    Discipline_Department = relationship("Discipline", back_populates="Department_Discipline")

class Discipline(Base):
    __tablename__ = 'Discipline'

    Discipline_ID = Column(Integer, Sequence('Discipline_id_seq'), primary_key=True)
    Discipline_name = Column(String, unique=True, nullable=False)
    Department_ID = Column(Integer, ForeignKey('Department.Department_ID'), nullable=False)
    
    Department_Discipline = relationship("Department", back_populates="Discipline_Department")
    Theme_Discipline = relationship("Theme", back_populates="Discipline_Theme")

class Theme(Base):
    __tablename__ = 'Theme'

    Theme_ID = Column(Integer, Sequence('Theme_id_seq'), primary_key=True)
    Theme_name = Column(String, nullable=False, unique=True)
    Discipline_ID = Column(Integer, ForeignKey('Discipline.Discipline_ID'), nullable=False)
    
    Discipline_Theme = relationship("Discipline", back_populates="Theme_Discipline")
    History_Theme = relationship("History", back_populates="Theme_History")


class Homework(Base):
    __tablename__ = 'Homework'

    Homework_ID = Column(Integer, Sequence('homework_id_seq'), primary_key=True)
    Homework = Column(String)
    
    history_homework = relationship("History", back_populates="homework_history")    
    
class Visit(Base):
    __tablename__ = 'Visit'

    Visit_ID = Column(Integer, Sequence('visit_id_seq'), primary_key=True)
    Data = Column(String, nullable=False)
    Visit_status = Column(Boolean)
        
    history_visit = relationship("History", back_populates="visit_history")    


class History(Base):
    __tablename__ = 'History'

    History_ID = Column(Integer, Sequence('visit_id_seq'), primary_key=True)
    Students_ID = Column(Integer, ForeignKey('Students.Students_ID'), nullable=False)
    Homework_ID = Column(Integer, ForeignKey('Homework.Homework_ID'), nullable=False)
    Visit_ID = Column(Integer, ForeignKey('Visit.Visit_ID'), nullable=False)
    Theme_ID = Column(Integer, ForeignKey('Theme.Theme_ID'), nullable=False)
    
    students_history = relationship("Students", back_populates="history_students")
    homework_history = relationship("Homework", back_populates="history_homework")
    visit_history = relationship("Visit", back_populates="history_visit")
    Theme_History = relationship("Theme", back_populates="History_Theme")


# # Создание таблиц
# Base.metadata.create_all(engine)