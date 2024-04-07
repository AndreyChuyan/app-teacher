from pydantic import BaseModel, EmailStr

class StudentBase(BaseModel):
    Zvan: str | None = None
    Fio: str
    Groups_ID: int

class StudentCreate(StudentBase):
    password: str


class StudentOut(StudentBase):
    Students_ID: int



    class Config:
        # from_attributes = True
        orm_mode = True