from app.models.grade import Grade
from app.db.base_class import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class Student(Base):

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    is_active = Column(Boolean(), default=True)
    email = Column(String, unique=True, index=True, nullable=False)
    grades = relationship
