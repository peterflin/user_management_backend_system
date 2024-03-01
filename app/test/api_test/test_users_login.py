from fastapi.testclient import TestClient
import sys
sys.path.insert(0, '../../')
from main import app


client = TestClient(app)


def test_user_login_should_success():
    response = client.post("/users/login", data={"username": "peterflin", "password": "abc123"})
    assert response.status_code == 200
    assert response.json()["access_token"] is not None
    assert response.json()["token_type"] == "bearer"
    assert len(response.json()["access_token"]) == 139


def test_user_login_should_fail():
    response = client.post("/users/login", data={"username": "peterflin", "password": "abc1234"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"