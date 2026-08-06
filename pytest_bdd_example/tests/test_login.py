import pytest
from pytest_bdd import scenarios, given, when, then

# Загружаем все сценарии из feature-файла
scenarios("features/login.feature")


@pytest.fixture
def login_state():
    return {
        "logged_in": False
    }


@given("пользователь находится на странице авторизации")
def open_login_page():
    print("Страница авторизации открыта")


@when("пользователь вводит правильный логин и пароль")
def login(login_state):
    login_state["logged_in"] = True


@then("пользователь успешно входит в систему")
def success(login_state):
    assert login_state["logged_in"] is True