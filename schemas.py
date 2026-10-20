from pydantic import BaseModel


class StudentCreate(BaseModel):
    student_id: int
    name: str
    age: int
    staff_id: int


class StudentResponse(BaseModel):
    Id: int
    StudentName: str
    Age: int
    Staffname: str
    department: str