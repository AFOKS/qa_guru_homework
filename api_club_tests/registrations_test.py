import uuid

import requests
from jsonschema import validate

from schemas.register_schema import success_registration


API_URL = "https://book-club.qa.guru/api/v1/users/register/"


def test_successful_registration():
    username = f"test_user_{uuid.uuid4().hex[:8]}"
    password = "TestPassword123!"

    request_body = {
        "username": username,
        "password": password
    }

    response = requests.post(API_URL, json=request_body)

    print("\nStatus code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    assert response.status_code == 201

    body = response.json()

    validate(body, schema=success_registration)

    assert body["id"] > 0
    assert body["username"] == username
    assert body["firstName"] == ""
    assert body["lastName"] == ""
    assert body["email"] == ""
    assert body["remoteAddr"]

def test_registration_missing_username():
    request_body = {
        "password": "TestPassword123!"
    }

    response = requests.post(API_URL, json=request_body)

    print("\nStatus code:", response.status_code)
    print("Body:", response.text)

    assert response.status_code == 400

    body = response.json()

    assert "username" in body

def test_registration_missing_password():
    request_body = {
        "username": f"test_user_{uuid.uuid4().hex[:8]}"
    }

    response = requests.post(API_URL, json=request_body)

    print("\nStatus code:", response.status_code)
    print("Body:", response.text)

    assert response.status_code == 400

    body = response.json()

    assert "password" in body

def test_registration_empty_username():
    request_body = {
        "username": "",
        "password": "TestPassword123!"
    }

    response = requests.post(API_URL, json=request_body)

    print("\nStatus code:", response.status_code)
    print("Body:", response.text)

    assert response.status_code == 400

    body = response.json()

    assert "username" in body

def test_registration_empty_password():
    request_body = {
        "username": f"test_user_{uuid.uuid4().hex[:8]}",
        "password": ""
    }

    response = requests.post(API_URL, json=request_body)

    print("\nStatus code:", response.status_code)
    print("Body:", response.text)

    assert response.status_code == 400

    body = response.json()

    assert "password" in body