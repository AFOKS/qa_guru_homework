import random

import requests
from jsonschema import validate
from schemas.club_schema import success_create_club, get_club_schema


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


def test_get_club_by_id():
    access_token = get_access_token()

    headers = {
        "Authorization": "Bearer " + access_token
    }

    # Создаем клуб
    club_body = get_club_body()

    create_response = requests.post(
        API_URL + "/clubs/",
        headers=headers,
        json=club_body
    )

    assert create_response.status_code == 201

    created_club = create_response.json()
    club_id = created_club["id"]

    # Получаем конкретный клуб
    response = requests.get(
        API_URL + f"/clubs/{club_id}/",
        headers=headers
    )

    print("\nStatus code:", response.status_code)
    print("Body:", response.text)

    # Проверяем статус ответа
    assert response.status_code == 200

    # Получаем JSON
    club_response_body = response.json()

    # Проверяем JSON Schema
    validate(
        club_response_body,
        schema=get_club_schema
    )

    # Проверяем id
    assert club_response_body["id"] == club_id

    # Проверяем данные клуба
    assert club_response_body["bookTitle"] == club_body["bookTitle"]
    assert club_response_body["bookAuthors"] == club_body["bookAuthors"]
    assert club_response_body["publicationYear"] == club_body["publicationYear"]
    assert club_response_body["description"] == club_body["description"]
    assert club_response_body["telegramChatLink"] == club_body["telegramChatLink"]

    # Проверяем владельца
    assert club_response_body["owner"] == USERNAME_ID

    # Проверяем, что владелец является участником клуба
    assert USERNAME_ID in club_response_body["members"]

    # При создании клуба отзывов быть не должно
    assert club_response_body["reviews"] == []

    # Удаляем созданный клуб
    delete_response = requests.delete(
        API_URL + f"/clubs/{club_id}/",
        headers=headers
    )

    assert delete_response.status_code == 204

def test_patch_club():
    access_token = get_access_token()

    headers = {
        "Authorization": "Bearer " + access_token
    }

    # Создаем клуб
    club_body = get_club_body()

    create_response = requests.post(
        API_URL + "/clubs/",
        headers=headers,
        json=club_body
    )

    assert create_response.status_code == 201

    created_club = create_response.json()
    club_id = created_club["id"]

    # Данные для изменения
    patch_body = {
        "bookTitle": "Updated book title",
        "bookAuthors": "Updated author",
        "publicationYear": 2025,
        "description": "Updated description",
        "telegramChatLink": "https://t.me/updated_link"
    }

    # Изменяем клуб
    patch_response = requests.patch(
        API_URL + f"/clubs/{club_id}/",
        headers=headers,
        json=patch_body
    )

    print("\nPATCH status code:", patch_response.status_code)
    print("PATCH body:", patch_response.text)

    # Проверяем статус
    assert patch_response.status_code == 200

    # Получаем JSON
    updated_club = patch_response.json()

    # Проверяем JSON Schema
    validate(
        updated_club,
        schema=get_club_schema
    )

    # Проверяем, что id остался прежним
    assert updated_club["id"] == club_id

    # Проверяем измененные данные
    assert updated_club["bookTitle"] == patch_body["bookTitle"]
    assert updated_club["bookAuthors"] == patch_body["bookAuthors"]
    assert updated_club["publicationYear"] == patch_body["publicationYear"]
    assert updated_club["description"] == patch_body["description"]
    assert updated_club["telegramChatLink"] == patch_body["telegramChatLink"]

    # Проверяем владельца
    assert updated_club["owner"] == USERNAME_ID

    # Проверяем, что владелец остался участником клуба
    assert USERNAME_ID in updated_club["members"]

    # Проверяем, что отзывов нет
    assert updated_club["reviews"] == []

    # Дополнительно делаем GET и проверяем,
    # что изменения действительно сохранились
    get_response = requests.get(
        API_URL + f"/clubs/{club_id}/",
        headers=headers
    )

    assert get_response.status_code == 200

    club_after_update = get_response.json()

    assert club_after_update["bookTitle"] == patch_body["bookTitle"]
    assert club_after_update["bookAuthors"] == patch_body["bookAuthors"]
    assert club_after_update["publicationYear"] == patch_body["publicationYear"]
    assert club_after_update["description"] == patch_body["description"]
    assert club_after_update["telegramChatLink"] == patch_body["telegramChatLink"]

    # Удаляем клуб
    delete_response = requests.delete(
        API_URL + f"/clubs/{club_id}/",
        headers=headers
    )

    assert delete_response.status_code == 204