from fastapi import APIRouter
from scripts.core.Handler.handler_student import add_student
from scripts.schema.studdent_schema import Student
from scripts.utilities.mongodb import Students
from scripts.schema.studdent_schema import Email
from scripts.core.Handler.mail_handler import send_email

student_router = APIRouter()


# Insert a student
@student_router.post("/addStudent/")
def add_student(student: Student):
    student_dict = student.dict()
    result = Students.insert_one(student_dict)
    return {"id": "Student added successfully"}


# Get all students from Mongodb
@student_router.get("/getAllStudents")
async def get_all_students():
    students = Students.find({})
    details = []
    for document in students:
        detail = {'id': document['id'], 'name': document['name'], 'address': document['address']}
        details.append(detail)
    return {"details": details}


# updating the student record
@student_router.put("/updateStudent/{std_id}")
def update_student(std_id: int, student: Student):
    result = Students.update_one({"id": std_id}, {"$set": student.dict()})
    if result.modified_count == 1:
        return {"message": "Student updated successfully"}
    else:
        return {"error": "Student not found"}


# Delete Student
@student_router.delete("/deleteStudentById/{std_id}")
def delete_student(std_id: int):
    try:
        Students.delete_one({"id": std_id})
        return {"message": "Student deleted successfully"}
    except Exception as e:
        return {"error": "Student not found"}
    
# Send Mail
@student_router.post("/send_email")
def send_item(email: Email):
    return send_email(email)
    # return {"message": "email sent"}