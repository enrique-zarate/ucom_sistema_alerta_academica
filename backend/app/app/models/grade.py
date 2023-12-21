from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship('Student', back_populates='grades')