from fastapi import FastAPI

app = FastAPI()

students = []

@app.post("/students")
def add_student(student_id: int, name: str, age: int, department: str):
    student = {
        "student_id": student_id,
        "name": name,
        "age": age,
        "department": department
    }

    students.append(student)

    return {
        "message": "Student added successfully!",
        "student": student
    }

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["student_id"] == student_id:
            return student

    return {"message": "Student not found!"}


@app.get("/students")
def get_student():
    return students


@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    name: str,
    age: int,
    department: str
):
    for student in students:
        if student["student_id"] == student_id:
            student["name"] = name
            student["age"] = age
            student["department"] = department

            return {
                "message": "Student updated successfully!",
                "student": student
            }

    return {"message": "Student not found!"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)

            return {
                "message": "Student deleted successfully!"
            }

    return {"message": "Student not found!"}
