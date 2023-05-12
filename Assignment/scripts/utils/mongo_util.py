from pymongo import MongoClient  

client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
database = []
db = client.interns_b2_23
student_instance = db.anzar_studentdb