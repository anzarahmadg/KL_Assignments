import uvicorn
from fastapi import FastAPI
from scripts.core.services.student_services import student_router as apps

# import mongo client to connect
from pymongo import MongoClient

app = FastAPI()
app.include_router(apps)  # calling the r# outer in the services

if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8000)