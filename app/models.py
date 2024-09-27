from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel:
    def __init__(self, db):
        self.collection = db['users']

    def create_user(self, data):
        # Hash the password before storing it
        data['password'] = generate_password_hash(data['password'])
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def get_user(self, user_id):
        return self.collection.find_one({"_id": ObjectId(user_id)})

    def update_user(self, user_id, data):
        return self.collection.update_one({"_id": ObjectId(user_id)}, {"$set": data})

    def delete_user(self, user_id):
        return self.collection.delete_one({"_id": ObjectId(user_id)})

    def get_user_by_credentials(self, username, password):
        user = self.collection.find_one({"username": username})  # Adjust the query based on your schema
        if user and check_password_hash(user['password'], password):  # Verify the hashed password
            return user
        return None
    

    def get_all_users(self):
        users = list(self.collection.find())  # Retrieve all users
        for user in users:
            user['_id'] = str(user['_id'])  # Convert ObjectId to string for JSON serialization
        return users

