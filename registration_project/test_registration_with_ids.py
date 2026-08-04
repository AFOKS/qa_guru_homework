import pytest

# Набор из нескольких тестовых данных

# Имя
@pytest.mark.parametrize(
    "first_name",
    ["Андрей", "Ксения"],
    ids=["first_name_andrey", "first_name_ksenia"]
)

# Фамилия

@pytest.mark.parametrize(
    "last_name",
    ["Аршавин", "Шарапова"],
    ids=["last_name_arshavin", "last_name_sharapova"]
)

# Возраст

@pytest.mark.parametrize(
    "age",
    [18, 25, 40],
    ids=["age_18", "age_35", "age_55"]

)
def test_registration_form(first_name, last_name, age):
    print(f"{first_name} {last_name}, {age}")

    assert len(first_name) > 0
    assert len(last_name) > 0
    assert age >= 18