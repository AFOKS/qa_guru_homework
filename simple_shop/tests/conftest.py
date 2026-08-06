import pytest

@pytest.fixture
def user():

    print("\nСоздаем пользователя")

    yield {
        "login": "admin",
        "password": "12345"
    }

    print("Удаляем пользователя")