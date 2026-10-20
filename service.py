from sqlalchemy.orm import Session

from models import Student, Staff
from schemas import StudentCreate


# POST - Add student
def add_student(student: StudentCreate, db: Session):

    new_student = Student(
        student_id=student.student_id,
        name=student.name,
        age=student.age,
        staff_id=student.staff_id
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# GET - Get all students
def get_students(db: Session):

    result = (
        db.query(
            Student.student_id.label("Id"),
            Student.name.label("StudentName"),
            Student.age.label("Age"),
            Staff.name.label("Staffname"),
            Staff.department.label("department")
        )
        .join(
            Staff,
            Student.staff_id == Staff.staff_id
        )
        .all()
    )

    return [
        {
            "Id":row.Id,
            "StudentName": row.StudentName,
            "Age": row.Age,
            "Staffname": row.Staffname,
            "department": row.department,
           
        }
        for row in result
    ]


# GET - Get student by ID
def get_student_by_id(student_id: int, db: Session):

    result = (
        db.query(
            Student.name.label("StudentName"),
            Student.age.label("Age"),
            Staff.name.label("Staffname"),
            Staff.department.label("department")
        )
        .join(
            Staff,
            Student.staff_id == Staff.staff_id
        )
        .filter(Student.student_id == student_id)
        .first()
    )

    if result is None:
        return None

    return {
        "StudentName": result.StudentName,
        "Age": result.Age,
        "Staffname": result.Staffname,
        "department": result.department
    }


# DELETE - Delete student
def delete_student(student_id: int, db: Session):

    student = (
        db.query(Student)
        .filter(Student.student_id == student_id)
        .first()
    )

    if student is None:
        return None

    db.delete(student)
    db.commit()

    return student