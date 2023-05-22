from pymongo import MongoClient

# Creating instance of mongo client
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
database = client['interns_b2_23']
Students = database['anzar_studentdb']