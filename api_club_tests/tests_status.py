import requests

from jsonschema import validate
from schemas.status_response_schema import status_response

# Запуст тестов pytest -s api_club_tests/tests_status.py

BASE_URL = 'https://book-club.qa.guru/api/v1/clubs/'

def test_status_response():
    """Проверка успешного ответа и соответствия JSON Schema."""

    response = requests.get(BASE_URL)

    print("\n✅Status code:", response.status_code)

    assert response.status_code == 200

    body = response.json()

    validate(body, schema=status_response)

    print("✅JSON schema validation PASSED")

def test_response_content_type():
    """Проверка, что API возвращает JSON."""

    response = requests.get(BASE_URL)

    print("\nContent-Type:", response.headers.get("Content-Type"))

    assert response.status_code == 200
    assert "application/json" in response.headers.get("Content-Type", "")


def test_response_contains_required_fields():
    """Проверка наличия основных полей в ответе."""

    response = requests.get(BASE_URL)

    assert response.status_code == 200

    body = response.json()

    assert "count" in body
    assert "next" in body
    assert "previous" in body
    assert "results" in body

    print("\n✅Все обязательные поля присутствуют")


def test_results_is_not_empty():
    """Проверка, что список клубов не пустой."""

    response = requests.get(BASE_URL)

    assert response.status_code == 200

    body = response.json()

    assert len(body["results"]) > 0

    print(f"\n✅Количество клубов на странице: {len(body['results'])}")


def test_club_has_required_fields():
    """Проверка структуры первого клуба."""

    response = requests.get(BASE_URL)

    assert response.status_code == 200

    body = response.json()

    first_club = body["results"][0]

    required_fields = [
        "id",
        "bookTitle",
        "bookAuthors",
        "publicationYear",
        "description",
        "telegramChatLink",
        "owner",
        "members",
        "reviews",
        "created",
        "modified"
    ]

    for field in required_fields:
        assert field in first_club, f"Поле '{field}' отсутствует"

    print("\n✅Структура объекта клуба корректная")