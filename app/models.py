from bson import ObjectId

class UserModel:
    def __init__(self, db):
        self.collection = db['users']

    def create_user(self, data):
        # Store the plain text password (not recommended for production)
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def get_user_by_credentials(self, username, password):
        # Retrieve user and check credentials directly (not recommended for production)
        user = self.collection.find_one({"username": username})
       
        print("Retrieved user:", user)
        # exit()

        if user and user['password'] == password:  # Compare plain text passwords
            return user
        return None

    def get_user(self, user_id):
        return self.collection.find_one({"_id": ObjectId(user_id)})

    def update_user(self, user_id, data):
        return self.collection.update_one({"_id": ObjectId(user_id)}, {"$set": data})

    def delete_user(self, user_id):
        return self.collection.delete_one({"_id": ObjectId(user_id)})

    def get_all_users(self):
        users = list(self.collection.find())  # Retrieve all users
        for user in users:
            user['_id'] = str(user['_id'])  # Convert ObjectId to string for JSON serialization
        return users
