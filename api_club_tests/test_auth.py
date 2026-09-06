import pytest
import requests
from jsonschema import validate

from schemas.auth_schema import (
    success_auth,
    wrong_credentials_auth,
    missing_password_auth,
    missing_username_auth,
    missing_username_password_auth,
    unsupported_media_type,
)

API_URL = "https://book-club.qa.guru/api/v1/auth/token/"

USERNAME = "test12"
PASSWORD = "123456"


def test_successful_auth():
    request_body = {
        "username": USERNAME,
        "password": PASSWORD
    }

    response = requests.post(API_URL, json=request_body)

    print("\nStatus code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    assert response.status_code == 200

    body = response.json()

    validate(body, schema=success_auth)

    access_token = body["access"]
    refresh_token = body["refresh"]

    assert access_token
    assert refresh_token

    assert len(access_token.split(".")) == 3
    assert len(refresh_token.split(".")) == 3

    assert access_token != refresh_token


def test_wrong_credentials_auth():
    request_body = {
        "username": USERNAME,
        "password": "wrong"
    }

    response = requests.post(API_URL, json=request_body)

    print("\nStatus code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    assert response.status_code == 401

    body = response.json()

    validate(body, schema=wrong_credentials_auth)

    assert body["detail"] == "Invalid username or password."


def test_missing_password_auth():
    request_body = {
        "username": USERNAME
    }

    response = requests.post(API_URL, json=request_body)

    print("\nStatus code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    assert response.status_code == 400

    body = response.json()

    validate(body, schema=missing_password_auth)

    assert body["password"] == ["This field is required."]


def test_unsupported_media_type():
    request_body = {
        "username": USERNAME,
        "password": PASSWORD
    }

    response = requests.post(
        API_URL,
        data=request_body,
        headers={
            "Content-Type": "image/png"
        }
    )

    print("\nStatus code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    assert response.status_code == 415

    body = response.json()

    validate(body, schema=unsupported_media_type)

    assert "Unsupported media type" in body["detail"]



def test_wrong_content_type_auth():
    request_body = {"username": USERNAME, "password": PASSWORD}
    headers = {"content-type": "image/png"}

    response = requests.post(API_URL, headers=headers, json=request_body)

    print("\nStatus code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    assert response.status_code == 415

    body = response.json()
    validate(body, schema=unsupported_media_type)

    assert body["detail"] == "Unsupported media type \"image/png\" in request."


def test_missing_username_auth():
    request_body = {
        "password": PASSWORD
    }

    response = requests.post(API_URL, json=request_body)

    print("\nStatus code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    assert response.status_code == 400

    body = response.json()

    validate(body, schema=missing_username_auth)

    assert body["username"] == ["This field is required."]


def test_missing_username_and_password_auth():
    request_body = {}

    response = requests.post(API_URL, json=request_body)

    print("\nStatus code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    assert response.status_code == 400

    body = response.json()

    validate(body, schema=missing_username_password_auth)

    assert body["username"] == ["This field is required."]
    assert body["password"] == ["This field is required."]


@pytest.mark.parametrize(
    "request_body",
    [
        None,
        True,
        123,
        "text",
        [],
    ]
)
def test_wrong_body_type(request_body):
    response = requests.post(
        API_URL,
        json=request_body
    )

    print("\nRequest body:", request_body)
    print("Status code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    assert response.status_code in [400, 415]

