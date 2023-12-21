from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

# Get all students
@router.get("/", response_model=List[schemas.Student])
def read_students(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    # current_user: models.Student = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve students.
    """
    students = crud.student.get_multi(db, skip=skip, limit=limit)
    return students

# Get a student by id
@router.get("/{id}", response_model=schemas.Student)
def read_student_by_id(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.Student = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get a student by id.
    """
    student = crud.student.get_by_id(db, id=id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Create a new student
@router.post("/", response_model=schemas.Student)
def create_student(
    *,
    db: Session = Depends(deps.get_db),
    student_in: schemas.StudentCreate,
    current_user: models.Student = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new student.
    """
    # student = crud.student.get_by_id(db, id=student_in.id)
    # if student:
    #     raise HTTPException(
    #         status_code=400,
    #         detail="The user with this username already exists in the system.",
    #     )
    student = crud.student.create(db, obj_in=student_in)
    return student

# Update a student
@router.put("/{id}", response_model=schemas.Student)
def update_student(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    student_in: schemas.StudentUpdate,
    current_user: models.Student = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a student.
    """
    if not crud.student.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    student = crud.student.get_by_id(db, id=id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student = crud.student.update(db, db_obj=student, obj_in=student_in)
    return student

# Delete a student
@router.delete("/{id}", response_model=schemas.Student)
def delete_student(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.Student = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a student.
    """
    if not crud.student.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    student = crud.student.get_by_id(db, id=id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student = crud.student.remove(db, id=id)
    return student
