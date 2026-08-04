import pytest

# Использовал параметризацию - всего получится 27 тестов с разными данными, т.к везде по 3 варианта данных

@pytest.mark.parametrize(
    "first_name",
    [
        pytest.param("Иван", id="Ivan"),
        pytest.param("Жанна", id="Zhanna"),
        pytest.param("Сергей", id="Sergey")

    ]
)
@pytest.mark.parametrize(
    "last_name",
    [
        pytest.param("Иванов", id="Ivanov"),
        pytest.param("Петрова", id="Petrova"),
        pytest.param("Медведев", id="Medvedev"),
    ]
)
@pytest.mark.parametrize(
    "age",
    [
        pytest.param(18, id="18yo"),
        pytest.param(25, id="25yo"),
        pytest.param(40, id="40yo")
    ]
)
def test_registration_form(first_name, last_name, age):
    print(f"{first_name} {last_name}, {age}")

    assert first_name
    assert last_name
    assert age >= 18