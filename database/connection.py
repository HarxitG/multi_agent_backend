from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db():
    # Get the URI from .env, fallback to localhost for development
    uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    client = MongoClient(uri)
    db = client["fitness_center"]
    return db
