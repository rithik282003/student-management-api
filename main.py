
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas import StudentCreate, StudentResponse
import service

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# POST - Add student
@app.post("/students")
def add_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    return service.add_student(student, db)


# GET - Get all students
@app.get("/students")
def get_students(
    db: Session = Depends(get_db)
):

    return service.get_students(db)


# GET - Get student by ID
@app.get("/students/{student_id}")
def get_student_by_id(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = service.get_student_by_id(student_id, db)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# DELETE - Delete student
@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = service.delete_student(student_id, db)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }
