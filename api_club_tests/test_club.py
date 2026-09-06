import random

import pytest
import requests
from jsonschema import validate

from schemas.club_schema import success_create_club


API_URL = "https://book-club.qa.guru/api/v1"
USERNAME = "123test"
PASSWORD = "123456"
USERNAME_ID = 3525


def get_access_token():
    auth_body = {
        "username": USERNAME,
        "password": PASSWORD
    }

    response = requests.post(
        API_URL + "/auth/token/",
        json=auth_body
    )

    assert response.status_code == 200

    return response.json()["access"]


def get_club_body():
    return {
        "bookTitle": f"Some another book {random.randint(1000, 999999)}",
        "bookAuthors": "Some author",
        "publicationYear": 2020,
        "description": "Some descr",
        "telegramChatLink": "https://t.me/qa.guru"
    }

def test_success_create_club():
    access_token = get_access_token()

    club_body = get_club_body()

    headers = {
        "Authorization": "Bearer " + access_token
    }

    response = requests.post(
        API_URL + "/clubs/",
        headers=headers,
        json=club_body
    )

    print("\nStatus code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    assert response.status_code == 201

    club_response_body = response.json()

    validate(
        club_response_body,
        schema=success_create_club
    )

    assert club_response_body["bookTitle"] == club_body["bookTitle"]
    assert club_response_body["bookAuthors"] == club_body["bookAuthors"]
    assert club_response_body["publicationYear"] == club_body["publicationYear"]
    assert club_response_body["description"] == club_body["description"]
    assert club_response_body["telegramChatLink"] == club_body["telegramChatLink"]

    assert club_response_body["owner"] == USERNAME_ID
    assert USERNAME_ID in club_response_body["members"]
    assert len(club_response_body["reviews"]) == 0
    assert club_response_body["modified"] is None

    # Удаляем созданный клуб после теста
    club_id = club_response_body["id"]

    delete_response = requests.delete(
        API_URL + f"/clubs/{club_id}/",
        headers=headers
    )

    assert delete_response.status_code == 204


def test_create_club_publication_year_as_string():

    access_token = get_access_token()

    club_body = get_club_body()
    club_body["publicationYear"] = "2020"

    headers = {
        "Authorization": "Bearer " + access_token
    }

    response = requests.post(
        API_URL + "/clubs/",
        headers=headers,
        json=club_body
    )

    print("\nStatus code:", response.status_code)
    print("Body:", response.text)

    assert response.status_code == 201

    response_body = response.json()

    assert response_body["publicationYear"] == 2020

    # Удаляем созданный клуб
    club_id = response_body["id"]

    delete_response = requests.delete(
        API_URL + f"/clubs/{club_id}/",
        headers=headers
    )

    assert delete_response.status_code == 204


def test_create_club_without_authorization():
    club_body = get_club_body()

    response = requests.post(
        API_URL + "/clubs/",
        json=club_body
    )

    print("\nStatus code:", response.status_code)
    print("Body:", response.text)

    assert response.status_code == 401

    assert response.json() == {
        "detail": "Authentication credentials were not provided."
    }


def test_create_club_missing_book_title():
    access_token = get_access_token()

    club_body = get_club_body()
    del club_body["bookTitle"]

    headers = {
        "Authorization": "Bearer " + access_token
    }

    response = requests.post(
        API_URL + "/clubs/",
        headers=headers,
        json=club_body
    )

    print("\nStatus code:", response.status_code)
    print("Body:", response.text)

    assert response.status_code == 400

    assert response.json() == {
        "bookTitle": ["This field is required."]
    }


def test_create_club_missing_book_authors():
    access_token = get_access_token()

    club_body = get_club_body()
    del club_body["bookAuthors"]

    headers = {
        "Authorization": "Bearer " + access_token
    }

    response = requests.post(
        API_URL + "/clubs/",
        headers=headers,
        json=club_body
    )

    print("\nStatus code:", response.status_code)
    print("Body:", response.text)

    assert response.status_code == 400

    assert response.json() == {
        "bookAuthors": ["This field is required."]
    }


def test_create_club_missing_publication_year():
    access_token = get_access_token()

    club_body = get_club_body()
    del club_body["publicationYear"]

    headers = {
        "Authorization": "Bearer " + access_token
    }

    response = requests.post(
        API_URL + "/clubs/",
        headers=headers,
        json=club_body
    )

    print("\nStatus code:", response.status_code)
    print("Body:", response.text)

    assert response.status_code == 400

    assert response.json() == {
        "publicationYear": ["This field is required."]
    }


def test_create_club_missing_required_fields():
    access_token = get_access_token()

    club_body = {}

    headers = {
        "Authorization": "Bearer " + access_token
    }

    response = requests.post(
        API_URL + "/clubs/",
        headers=headers,
        json=club_body
    )

    print("\nStatus code:", response.status_code)
    print("Body:", response.text)

    assert response.status_code == 400

    assert response.json() == {
        "bookTitle": ["This field is required."],
        "bookAuthors": ["This field is required."],
        "publicationYear": ["This field is required."],
        "description": ["This field is required."],
        "telegramChatLink": ["This field is required."]
    }


@pytest.mark.parametrize(
    "publication_year",
    [
        2147483648,
        999999999999,
    ]
)
def test_create_club_invalid_publication_year(publication_year):
    access_token = get_access_token()

    club_body = get_club_body()
    club_body["publicationYear"] = publication_year

    headers = {
        "Authorization": "Bearer " + access_token
    }

    response = requests.post(
        API_URL + "/clubs/",
        headers=headers,
        json=club_body
    )

    print("\nPublication year:", publication_year)
    print("Status code:", response.status_code)
    print("Body:", response.text)

    assert response.status_code == 400

    assert "publicationYear" in response.json()


@pytest.mark.parametrize(
    "publication_year",
    [
        None,
        True,
        [],
        {}
    ]
)
def test_create_club_wrong_publication_year_type(publication_year):
    access_token = get_access_token()

    club_body = get_club_body()
    club_body["publicationYear"] = publication_year

    headers = {
        "Authorization": "Bearer " + access_token
    }

    response = requests.post(
        API_URL + "/clubs/",
        headers=headers,
        json=club_body
    )

    print("\nPublication year:", publication_year)
    print("Status code:", response.status_code)
    print("Body:", response.text)

    assert response.status_code == 400

    assert "publicationYear" in response.json()

@pytest.mark.parametrize(
    "request_body, expected_response",
    [
        (
            None,
            {
                "bookTitle": ["This field is required."],
                "bookAuthors": ["This field is required."],
                "publicationYear": ["This field is required."],
                "description": ["This field is required."],
                "telegramChatLink": ["This field is required."]
            }
        ),
        (
            True,
            {
                "nonFieldErrors": [
                    "Invalid data. Expected a dictionary, but got bool."
                ]
            }
        ),
        (
            123,
            {
                "nonFieldErrors": [
                    "Invalid data. Expected a dictionary, but got int."
                ]
            }
        ),
        (
            "text",
            {
                "nonFieldErrors": [
                    "Invalid data. Expected a dictionary, but got str."
                ]
            }
        ),
        (
            [],
            {
                "nonFieldErrors": [
                    "Invalid data. Expected a dictionary, but got list."
                ]
            }
        )
    ]
)
def test_create_club_wrong_body_type(request_body, expected_response):
    access_token = get_access_token()

    headers = {
        "Authorization": "Bearer " + access_token
    }

    response = requests.post(
        API_URL + "/clubs/",
        headers=headers,
        json=request_body
    )

    print("\nRequest body:", request_body)
    print("Status code:", response.status_code)
    print("Body:", response.text)

    assert response.status_code == 400
    assert response.json() == expected_response