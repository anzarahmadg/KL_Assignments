from fastapi import FastAPI
from fastapi import APIRouter
from scripts.services.student_routes import student
app = FastAPI()
app.include_router(student)