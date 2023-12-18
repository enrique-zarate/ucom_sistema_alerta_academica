from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate


class CRUDStudent(CRUDBase[Student, StudentCreate, StudentUpdate]):
    """CRUD operations for the Student model."""


    def create(self, db: Session, *, obj_in: StudentCreate) -> Student:
        """Create a new student.

        Args:
            db (Session): The database session.
            obj_in (StudentCreate): The input data for creating a student.

        Returns:
            Student: The created student.
        """
        db_obj = Student(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            roles=["student"],
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update (
        self, db: Session, *, db_obj: Student, obj_in: Union[StudentUpdate, Dict[str, Any]]
    ) -> Student:
        """Update a student.

        Args:
            db (Session): The database session.
            db_obj (Student): The student object to update.
            obj_in (Union[StudentUpdate, Dict[str, Any]]): The input data for updating a student.

        Returns:
            Student: The updated student.
        """
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)
    
    def get_by_id(self, db: Session, *, id: int) -> Optional[Student]:
        """Get a student by id.

        Args:
            db (Session): The database session.
            id (int): The id of the student to search for.

        Returns:
            Optional[Student]: The student if found, else None.
        """
        return db.query(Student).filter(Student.id == id).first()

student = CRUDStudent(Student)
