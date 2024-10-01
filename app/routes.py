import os
from datetime import datetime, timedelta
from functools import wraps
from flask import Flask, request, jsonify
import jwt  # Import the jwt module
from jwt import ExpiredSignatureError, InvalidTokenError  # Import specific exceptions
from app.config import get_db
from app.models import UserModel

import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback_secret_key')  # Use environment variable
db = get_db()


user_model = UserModel(db)

# Token required decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            print("Decoded token:", decoded)  # Log decoded token for debugging
        except ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        except InvalidTokenError as e:
            print(f"Invalid token error: {e}")  # Log the specific error
            return jsonify({'message': 'Invalid token!'}), 403
        return f(*args, **kwargs)
    return decorated

@app.route('/login', methods=['POST'])
def login():
    auth = request.json
    if not auth or 'username' not in auth or 'password' not in auth:
        return jsonify({'message': 'Missing credentials!'}), 400
    
    user = user_model.get_user_by_credentials(auth['username'], auth['password'])
    if user:
        token = jwt.encode({  # Use jwt.encode here
            'user_id': str(user['_id']),
            'exp': datetime.utcnow() + timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials!'}), 401




@app.route('/users', methods=['POST'])
# @token_required
def create_user():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    user_id = user_model.create_user(data)
    return jsonify({"user_id": str(user_id)}), 201

@app.route('/users/<user_id>', methods=['GET'])
@token_required
def get_user(user_id):
    user = user_model.get_user(user_id)
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<user_id>', methods=['PUT'])
@token_required
def update_user(user_id):
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    result = user_model.update_user(user_id, data)
    if result.modified_count:
        return jsonify({"message": "User updated"}), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<user_id>', methods=['DELETE'])
@token_required
def delete_user(user_id):
    result = user_model.delete_user(user_id)
    if result.deleted_count:
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404
@app.route('/users', methods=['GET'])
@token_required  # Optional: protect this endpoint with JWT authentication
def list_users():
    users = user_model.get_all_users()
    return jsonify(users), 200


if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
