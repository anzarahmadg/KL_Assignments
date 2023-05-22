from pydantic import BaseModel

# Model for a Student
class Student(BaseModel):
    id: int
    name: str
    address: str
    # phone: int

class Email(BaseModel):
    rec_email: str
    subject: str