from typing import Optional

from pydantic import BaseModel, EmailStr

from typing import List


# Shared properties
class StudentBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    full_name: Optional[str] = None


# Properties to receive via API on creation
class StudentCreate(StudentBase):
    email: EmailStr
    is_active: bool = True
    full_name: str

# Properties to receive via API on update
class StudentUpdate(StudentBase):
    pass

class StudentInDBBase(StudentBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class StudentInDB(StudentInDBBase):
    pass


class Student(StudentInDBBase):
    pass