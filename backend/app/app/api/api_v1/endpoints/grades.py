from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas

from app.api import deps

router = APIRouter()


from pydantic import BaseModel

import logging

# from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

# from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class Grade(BaseModel):
    grade: int


# Add a grade to a student. This is a custom endpoint that only receives a student id and a grade.
@router.post("/{id}/add-grade", response_model=str)
def add_grade_to_student(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    grade: Grade,
) -> Any:
    """
    Add a grade to a student.
    """
    logger.info("id: ", id)
    student = crud.student.get_by_id(db, id=id)
    logger.info("student: ", student)
    print("student: ", student) 
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student = crud.grade.add_grade(db, id_student=id, grade=grade.grade)
    return "Grade added to student"