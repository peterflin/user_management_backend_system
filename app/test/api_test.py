import requests


BASE_URL = "http://localhost:8000/users"


# def test_create_user():
#     data = {
#         "name": "peterflin",
#         "email": "peterflin@gmail.com",
#         "password": "abc123"
#     }
#     r = requests.post(BASE_URL + "/create_user", json=data)
#     assert r.status_code == 200
#     assert r.json()["result"] == "fail"


def test_login():
    data = {
        "name": "peterflin",
        "password": "abc123"
    }
    r = requests.post(BASE_URL + "/login", json=data)
    assert r.status_code == 200
    assert isinstance(r.json()["access_token"], str)


if __name__ == "__main__":
    test_login()
    print("All tests passed")
