from pydantic import BaseModel , EmailStr ,Field
from typing import Optional


class Student(BaseModel):
    name: str = "Alina"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0 , lt=10 , default = 5, description="Cgpa of student")

new_student = {'age':'32', 'email': "abc@abc.com"}

student = Student(**new_student)

#new_student: Student = {'name': 32}


#print(type(new_student))
#print(new_student)

print(type(student.age))

print(type(student.email))
print(student.cgpa)

student_dict = dict(student)

print(student_dict)

student_json = student.model_dump_json()

print(student_json)