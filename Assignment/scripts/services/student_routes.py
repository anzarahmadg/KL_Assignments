from scripts.schemas.student_models import Student
from scripts.utils.mongo_util import student_instance
from fastapi import APIRouter
student=APIRouter()
@student.post("/addStudent/")
def add_student(student: Student):
    student_instance.insert_one(student.dict())
    return {"message": "Student added successfully"}


# Get all students from Mongodb
@student.get("/getAllStudents")
async def get_all_students():
    students =  student_instance.find({})
    details = []
    for document in students:
        detail = {'id':document['id'],'name':document['name'],'address':document['address']}
        details.append(detail)
    return {"details":details}

#Get student by Id -------Not Working-------
@student.get("/getStudentById/{id_std}")
async def getStudentById(id_std: int):
    students = student_instance.find_one({"id": id_std})  #find({"id": id})
        # details = []
        # for student in students:
        #     if student['id'] == id_std:
        #         detail = {'id':student['id'],'name':student['name'],'address':student['address']}
        #         details.append(detail)
    return {"student": students}

@student.put("/updateStudent/{std_id}/")
def update_student(std_id: int, student: Student):
    student_instance.update_one({"id": std_id}, {"$set": student.dict()})
    return {"Updated Successfully"}

# Delete a book
@student.delete("/deleteStudent/{std_id}")
def delete_book(std_id: int):
    student_instance.delete_one({"id": std_id})
    return {"deleted Successfully "}