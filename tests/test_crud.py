import json
import pytest
from app.routes import app  # Adjust this import if your app is structured differently

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def auth_token(client):
    # Attempt to log in to get the token
    login_data = {"username": "ravi444", "password": "ravi"}
    response = client.post('/login1', data=json.dumps(login_data), content_type='application/json')
    
    assert response.status_code == 200, "Login failed. Check username/password."
    
    token = response.get_json().get('token')
    assert token is not None, "Token not found in response."
    return token

def test_create_user(client):
    user_data = {"username": "ravi", "password": "ravi"}
    response = client.post('/users', data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 201, "Failed to create user."
    assert 'user_id' in response.get_json(), "User ID not found in response."

def test_get_user(auth_token, client):
    headers = {'Authorization': f'Bearer {auth_token}'}
    
    # Create a user to retrieve
    response = client.post('/users', data=json.dumps({"username": "Doe", "password": "ravi"}), headers=headers, content_type='application/json')
    assert response.status_code == 201, "Failed to create user for retrieval."
    
    user_id = response.get_json()['user_id']
    
    # Now get the user
    response = client.get(f'/users/{user_id}', headers=headers)
    assert response.status_code == 200, "Failed to retrieve user."
    assert response.get_json()['username'] == 'Doe', "Retrieved username does not match."

def test_update_user(auth_token, client):
    headers = {'Authorization': f'Bearer {auth_token}'}
    
    # First, create a user
    response = client.post('/users', data=json.dumps({"username": "John", "password": "password123"}), headers=headers, content_type='application/json')
    assert response.status_code == 201, "Failed to create user for update."
    
    user_id = response.get_json()['user_id']
    
    # Update the user
    response = client.put(f'/users/{user_id}', data=json.dumps({"username": "John Updated"}), headers=headers, content_type='application/json')
    assert response.status_code == 200, "Failed to update user."
    assert response.get_json()['message'] == 'User updated', "Update message mismatch."

def test_delete_user(auth_token, client):
    headers = {'Authorization': f'Bearer {auth_token}'}
    
    # First, create a user
    response = client.post('/users', data=json.dumps({"username": "John", "password": "password123"}), headers=headers, content_type='application/json')
    assert response.status_code == 201, "Failed to create user for deletion."
    
    user_id = response.get_json()['user_id']
    
    # Delete the user
    response = client.delete(f'/users/{user_id}', headers=headers)
    assert response.status_code == 200, "Failed to delete user."
    assert response.get_json()['message'] == 'User deleted', "Delete message mismatch."

def test_list_users(auth_token, client):
    headers = {'Authorization': f'Bearer {auth_token}'}
    response = client.get('/users', headers=headers)
    assert response.status_code == 200, "Failed to retrieve users."
    assert isinstance(response.get_json(), list), "Response is not a list."
