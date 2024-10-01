import os
from pymongo import MongoClient

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://local-mongo:27017/mydb")  # Default URI if not set


def get_db():
    client = MongoClient(Config.MONGO_URI)
    db = client.mydb
    return db
