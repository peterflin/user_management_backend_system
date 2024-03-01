from fastapi.testclient import TestClient
import sys
sys.path.insert(0, '../../')
from main import app


client = TestClient(app)


def test_delete_user_should_success():
    login_response = client.post("/users/login", data={"username": "peterflin", "password": "abc123"})
    response = client.delete(
        "/users/delete_user?user_id=41",
        headers={"Authorization": f"Bearer {login_response.json()['access_token']}"}
    )
    print(response.json())
    assert response.status_code == 200
    assert response.json()["result"] == "success"


def test_delete_user_should_fail():
    login_response = client.post("/users/login", data={"username": "peterflin", "password": "abc123"})
    response = client.delete(
        "/users/delete_user?user_id=41",
        headers={"Authorization": f"Bearer {login_response.json()['access_token']}"}
    )
    assert response.status_code == 400
