from sqlalchemy.orm import Session
from app.models.student import Student
from app.models.grade import Grade
from app.crud.base import CRUDBase

class CRUDGrade(CRUDBase[Grade, None, None]):

    def add_grade(self, db: Session, *, id_student: int, grade: int):
        """Add a grade to a student.

        Args:
            db (Session): The database session.
            id_student (int): The id of the student.
            grade (int): The grade to add.

        Returns:
            Ok message.
        """
        student = db.query(Student).filter(Student.id == id_student).first()
        grade = Grade(grade=grade, student=student)
        db.add(grade)
        db.commit()
        db.refresh(grade)
        return "Ok"

grade = CRUDGrade(Grade)