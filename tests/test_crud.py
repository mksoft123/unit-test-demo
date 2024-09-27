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
    # Create a user directly (no token needed)
    # user_data = {"name": "TestUser", "password": "testpassword"}
    # client.post('/users', data=json.dumps(user_data), content_type='application/json')
    
    # Now log in to get the token
    login_data = {"username": "John", "password": "password123"}
    response = client.post('/login', data=json.dumps(login_data), content_type='application/json')
    token = response.get_json().get('token')
    
    assert token is not None
    return token
# @pytest.mark.skip(reason="Skipping user creation test temporarily")

def test_create_user(client):
    user_data = {"username": "TeshtUser", "password": "testpuuassword"}
    response = client.post('/users', data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 201
    assert 'user_id' in response.get_json()

def test_get_user(auth_token, client):
    headers = {'Authorization': f'Bearer {auth_token}'}
    
    # Create a user to retrieve
    response = client.post('/users', data=json.dumps({"name": "Doe", "password": "password123"}), headers=headers, content_type='application/json')
    user_id = response.get_json()['user_id']
    
    # Now get the user
    response = client.get(f'/users/{user_id}', headers=headers)
    assert response.status_code == 200
    assert response.get_json()['name'] == 'Doe'

def test_update_user(auth_token, client):
    headers = {'Authorization': f'Bearer {auth_token}'}
    
    # First, create a user
    response = client.post('/users', data=json.dumps({"name": "John", "password": "password123"}), headers=headers, content_type='application/json')
    user_id = response.get_json()['user_id']
    
    # Update the user
    response = client.put(f'/users/{user_id}', data=json.dumps({"name": "John Updated"}), headers=headers, content_type='application/json')
    assert response.status_code == 200
    assert response.get_json()['message'] == 'User updated'

def test_delete_user(auth_token, client):
    headers = {'Authorization': f'Bearer {auth_token}'}
    
    # First, create a user
    response = client.post('/users', data=json.dumps({"name": "John", "password": "password123"}), headers=headers, content_type='application/json')
    user_id = response.get_json()['user_id']
    
    # Delete the user
    response = client.delete(f'/users/{user_id}', headers=headers)
    assert response.status_code == 200
    assert response.get_json()['message'] == 'User deleted'

def test_list_users(auth_token, client):
    headers = {'Authorization': f'Bearer {auth_token}'}
    response = client.get('/users', headers=headers)
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)  # Check that the response is a list
