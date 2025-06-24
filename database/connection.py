from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb://localhost:27017")  # Adjust as needed
    db = client["fitness_center"]
    return db
