from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db():
    # Get MongoDB URI from environment variables
    uri = os.getenv("MONGO_URI")
    if not uri:
        raise Exception("MONGO_URI not found in environment variables.")
    
    client = MongoClient(uri)
    return client["fitness_center"]
