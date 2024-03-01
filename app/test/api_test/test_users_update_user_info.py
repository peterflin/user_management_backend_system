from fastapi.testclient import TestClient
import sys
sys.path.insert(0, '../../')
from main import app


client = TestClient(app)


def test_update_user_info_should_success():
    login_response = client.post("/users/login", data={"username": "peterflin", "password": "abc123"})
    response = client.put(
        "/users/update_user_info?user=2",
        headers={"Authorization": f"Bearer {login_response.json()['access_token']}"},
        json={"user_id": 8, "name": "peterflin145677", "email": "test@gmail.com"}
    )
    response_data = response.json()
    assert response.status_code == 200
    assert response_data['result'] == "success"


def test_update_user_info_should_fail_by_name_format_validation_fail():
    login_response = client.post("/users/login", data={"username": "peterflin", "password": "abc123"})
    response = client.put(
        "/users/update_user_info?",
        headers={"Authorization": f"Bearer {login_response.json()['access_token']}"},
        json={"user_id": 8, "name": "peterflin14567@", "email": "test@gmail.com"}
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "string_pattern_mismatch"


def test_update_user_info_should_fail_by_email_format_validation_fail():
    login_response = client.post("/users/login", data={"username": "peterflin", "password": "abc123"})
    response = client.put(
        "/users/update_user_info?",
        headers={"Authorization": f"Bearer {login_response.json()['access_token']}"},
        json={"user_id": 8, "name": "peterflin145677", "email": "test@gmail"}
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "string_pattern_mismatch"