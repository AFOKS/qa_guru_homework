import pytest


def register_user(first_name: str, last_name: str, age: int):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    }


@pytest.mark.parametrize(
    "first_name",
    [
        pytest.param("Иван", id="Ivan"),
        pytest.param("Анна", id="Anna"),
        pytest.param("Игнат",id="Ignat")
    ]
)
@pytest.mark.parametrize(
    "last_name",
    [
        pytest.param("Иванов", id="Ivanov"),
        pytest.param("Захарова", id="Zaharova"),
        pytest.param("Рубин", id="Rubin")
    ]
)
@pytest.mark.parametrize(
    "age",
    [
        pytest.param(18, id="18yo"),
        pytest.param(66, id="66yo"),
        pytest.param(40, id="40yo")
    ]
)
def test_registration_form(first_name, last_name, age):
    user = register_user(first_name, last_name, age)

    assert user["first_name"] == first_name
    assert user["last_name"] == last_name
    assert user["age"] == age