from fastapi.testclient import TestClient
import random
import sys
sys.path.insert(0, '../')
from main import app


client = TestClient(app)


def test_create_user_should_success():
    register_data = {"name": f"peterflin{random.randint(1000, 10000)}", "email": "peterflin4@gmail.com", "password": "abc123"}
    response = client.post("/users/create_user", json=register_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["result"] == "success"


def test_create_user_should_fail_by_exist_user():
    register_data = {"name": "peterflin", "email": "peterflin@gmail.com", "password": "abc123"}
    response = client.post("/users/create_user", json=register_data)
    assert response.status_code == 400


def test_create_user_should_fail_by_name_string_too_long():
    register_data = {"name": "peterflin123123123123123", "email": "peterflin@gmail.com", "password": "abc123"}
    response = client.post("/users/create_user", json=register_data)
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "string_too_long"


def test_create_user_should_fail_by_name_contains_space():
    register_data = {"name": "peterflin ", "email": "XXXXXXXXXXXXXXXXXXX", "password": "XXXXXX"}
    response = client.post("/users/create_user", json=register_data)
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "string_pattern_mismatch"


def test_create_user_should_fail_by_name_is_empty_string():
    register_data = {"name": "", "email": "XXXXXXXXXXXXXXXXXXX", "password": "XXXXXX"}
    response = client.post("/users/create_user", json=register_data)
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "string_pattern_mismatch"


def test_create_user_should_fail_by_name_contains_special_character():
    register_data = {"name": "peter@123", "email": "XXXXXXXXXXXXXXXXXXX", "password": "XXXXXX"}
    response = client.post("/users/create_user", json=register_data)
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "string_pattern_mismatch"


def test_create_user_should_fail_by_password_string_too_long():
    register_data = {"name": "peterflin", "email": "peterflin@gmail.com", "password": "abc123123123123123123123123"}
    response = client.post("/users/create_user", json=register_data)
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "string_too_long"


def test_create_user_should_fail_by_password_is_empty_string():
    register_data = {"name": "peterflin", "email": "XXXXXXXXXXXXXXXXXXX", "password": ""}
    response = client.post("/users/create_user", json=register_data)
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "string_pattern_mismatch"


def test_create_user_should_fail_by_email_is_empty_string():
    register_data = {"name": "peterflin", "email": "", "password": "abc123"}
    response = client.post("/users/create_user", json=register_data)
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "string_pattern_mismatch"


def test_create_user_should_fail_by_email_validation_fail():
    register_data = {"name": "peterflin", "email": "peterflin@gmail", "password": "abc123"}
    response = client.post("/users/create_user", json=register_data)
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "string_pattern_mismatch"