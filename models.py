from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Staff(Base):
    __tablename__ = "staff"

    staff_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    department = Column(String)


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    staff_id = Column(Integer, ForeignKey("staff.staff_id"))