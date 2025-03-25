import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_user(client):
    response = client.post('/users', json={"name": "Alice"})
    assert response.status_code == 201
    assert response.json["message"] == "User created"
