from pymongo import MongoClient  
from scripts.config import DBConf

MONGO_URI = DBConf.MONGO_URI
client = None

try:
    client = MongoClient(MONGO_URI)
    print("Connected")
except Exception as e:
    print("deafult: " + str(e))



# client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
# database = []
db = client.interns_b2_23
student_instance = db.anzar_studentdb