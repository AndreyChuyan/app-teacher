from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Enum, Boolean
from sqlalchemy.orm import declarative_base, relationship
import enum
from sqlalchemy import Sequence

from database.database import Base


class TransactionType(enum.Enum):
    Buy = "Buy"
    Sell = "Sell"
    Dividend = "Dividend"


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    asset_types = relationship("AssetType", back_populates="user")
    portfolios = relationship("Portfolio", back_populates="user")

    def __str__(self):
        return f"User: {self.username} Email: {self.email} ID: {self.id}"


class AssetType(Base):
    __tablename__ = "asset_type"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="asset_types")
    assets = relationship("Asset", back_populates="asset_type")


class Portfolio(Base):
    __tablename__ = "portfolio"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="portfolios")
    assets = relationship("Asset", back_populates="portfolio")


class Asset(Base):
    __tablename__ = "asset"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Float)
    purchase_price = Column(Float)
    current_price = Column(Float)
    commission = Column(Float)
    portfolio_id = Column(Integer, ForeignKey("portfolio.id"))
    asset_type_id = Column(Integer, ForeignKey("asset_type.id"))
    portfolio = relationship("Portfolio", back_populates="assets")
    asset_type = relationship("AssetType", back_populates="assets")
    transactions = relationship("Transaction", back_populates="asset")


class Transaction(Base):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True)
    type = Column(Enum(TransactionType))
    created_at = Column(DateTime, default=datetime.now)
    quantity = Column(Float)
    price = Column(Float)
    asset_id = Column(Integer, ForeignKey("asset.id"))
    asset = relationship("Asset", back_populates="transactions")

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
