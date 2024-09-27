from pymongo import MongoClient

class Config:
    MONGO_URI = "mongodb://root:root@localhost:37017/mydb?authSource=admin"  # MongoDB URI

def get_db():
    client = MongoClient(Config.MONGO_URI)
    db = client.mydb
    return db
