import pytest
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("features/calculator.feature")


@pytest.fixture
def context():
    return {}


@given(parsers.parse("первое число равно {value:d}"))
def first_number(context, value):
    context["a"] = value


@given(parsers.parse("второе число равно {value:d}"))
def second_number(context, value):
    context["b"] = value


@when("пользователь складывает числа")
def add(context):
    context["result"] = context["a"] + context["b"]


@then(parsers.parse("результат должен быть {expected:d}"))
def check(context, expected):
    assert context["result"] == expected