from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


    


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/contact")
async def root():
    return {"Anzar": "Intern at Knowledge Lens"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


"""Calculator"""

@app.get("/addition/{num1}/{num2}")
async def read_item(num1: int, num2: int):
    return {"The sum of two numbers is: ": num1 + num2}

@app.get("/subtract/{num1}/{num2}")
async def read_item(num1: int, num2: int):
    return {"The subtraction of two numbers is: ": num1 - num2}

@app.get("/multiplication/{num1}/{num2}")
async def read_item(num1: int, num2: int):
    return {"The multiplication of two numbers is: ": num1 * num2}

@app.get("/division/{num1}/{num2}")
async def read_item(num1: int, num2: int):
    try:
        return {"The division of two numbers is: ": num1 / num2}
    except:
        return{"Divide by zero exception"}
    
"""CRUD operations using list """
    
student = []

@app.post("/addStudent/{name}")
async def addStudent(name):
    student.append(name)
    return{"Student added successfully!!"}

@app.delete("/deleteStudent/{name}")
async def removeStudent(name):
    if student:
        student.remove(name)
        return{"Student deleted Sucessfully!!"}
    else:
        return{"Student not found"}

# @app.get("/getStudents/")
# async def getStudents():
#     return{"Students":student}



"""CRUD operations using Dictionary"""

dictionaryOfStudent = {}

@app.post("/addStudent/{id}/{name}/")
async def addStudent(id,name):
    dictionaryOfStudent[id]=name
    return{"Student added successfully!!"}

@app.put("/updateStudent/{id}/{name}/")
async def addStudent(id,name):
    d = {id:name}
    dictionaryOfStudent.update(d)
    return{"Student updated successfully!!"}

@app.delete("/deleteStudent/{id}/")
async def deleteStudentByid(id):
    if id:
        dictionaryOfStudent.pop(id)
        return{"Student deleted Sucessfully!! "}
    else:
        return{"No student found "}

@app.get("/getStudents/")
async def getStudents():
    return{"Students":dictionaryOfStudent}

"""CRUD using Models"""

class Student(BaseModel):
    std_id = int
    std_name = str
    std_class = str

student_data = []

@app.post("/student/")
async def addStudent(student:Student):
    student_data.append(student)
    return {"data": "Student Added successfully!!"}
 