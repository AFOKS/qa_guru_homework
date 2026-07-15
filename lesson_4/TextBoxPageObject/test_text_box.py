import pytest
import time
from text_box_page import TextBoxPage


# --- 1. Позитивные сценарии (Валидные данные) ---> Улучшил тесты так, чтобы покрывали больше кейсов
@pytest.mark.parametrize(
    "name, email, cur_addr, perm_addr",
    [
        # Позитивные
        ("John Doe", "john@example.com", "123 Elm St", "456 Oak St"),
        ("Иван Иванов", "ivan@mail.ru", "ул. Ленина, 1", "ул. Пушкина, 2"),
        ("张伟", "zhang@test.cn", "北京", "上海"),
        ("O'Connor", "oconnor@test.com", "Street", "Street"),
        ("John 😀", "emoji@test.com", "Street 😎", "Home 🚀"),

        # Граничные значения
        ("A", "a@b.cc", "B", "C"),
        ("J" * 255, "long@test.com", "A" * 255, "B" * 255),

        # Проверка пробелов
        (" John ", "space@test.com", "  Street 1  ", "  Street 2  "),

        # Спецсимволы
        ("Jean-Luc Picard", "captain@test.com", "Addr 1/2", "Addr 3 & 4"),
    ]
)
def test_positive_form_submission(driver, name, email, cur_addr, perm_addr):

    page = TextBoxPage(driver)
    page.open()
    page.fill_form(name, email, cur_addr, perm_addr)
    page.submit()
    output = page.get_output_data()

    assert output is not None, "Блок с результатами не отобразился"
    assert output["name"] == name.strip()
    assert output["email"] == email.strip()
    assert output["cur_addr"] == cur_addr.strip()
    assert output["perm_addr"] == perm_addr.strip()


# --- 2. Частичное заполнение обязательных/необязательных полей ---
# Избавился от цикла, добавил больше тестов с разными данными
# Добавил идентификатов тестов, чтобы смотреть какие падают (подсмотрел в гайде)
@pytest.mark.parametrize(
    "name, email, cur_addr, perm_addr",
    [
        # отсутствуют обязательные поля
        ("Only Name", "", "", ""),
        ("", "only@email.com", "", ""),
        ("", "", "", ""),

        # заполнены только необязательные
        ("", "", "Only Current Address", ""),
        ("", "", "", "Only Permanent Address"),

        # только обязательные
        ("John Doe", "john@test.com", "", ""),

        # обязательные + один необязательный
        ("John Doe", "john@test.com", "Street", ""),
        ("John Doe", "john@test.com", "", "Home"),

        # все поля
        ("John Doe", "john@test.com", "Street", "Home"),

        # пробелы
        ("   ", "john@test.com", "", ""),
        ("John Doe", "   ", "", ""),
    ],
    ids=[
        "only_name",
        "only_email",
        "empty_form",
        "only_current_address",
        "only_permanent_address",
        "required_fields_only",
        "required_plus_current_address",
        "required_plus_permanent_address",
        "all_fields",
        "spaces_in_name",
        "spaces_in_email",
    ]
)

def test_partial_form_submission(driver, name, email, cur_addr, perm_addr):
    page = TextBoxPage(driver)
    page.open()
    page.fill_form(name, email, cur_addr, perm_addr)
    page.submit()
    output = page.get_output_data()

    time.sleep(3) # tmp solution

    assert output is not None, "Форма должна отправляться при частичном заполнении"

# --- 3. Негативные сценарии (Невалидный Email) ---> добавил разные сценарии
@pytest.mark.parametrize(
    "invalid_email",
    [
        "plainaddress",          # нет @
        "@no-local-part.com",    # нет локальной части
        "john@",                 # нет домена
        "john@example",          # нет ".com"
        "john.doe@com",          # нет точки перед "com"
        "john@missing-dot",      # нет точки
        "john@@example.com",     # две @
        "john@example..com",     # две точки
        ".john@example.com",     # начинается с точки
        "john.@example.com",     # заканчивается точкой
        "john..doe@example.com", # две точки
        "john example@test.com", # пробел
        "",                      # пустое значение
    ],
)

def test_invalid_email_validation(driver, invalid_email):
    page = TextBoxPage(driver)
    page.open()
    page.fill_form(name="Test", email=invalid_email)
    page.submit()

    # Ожидаем, что блок вывода не появился ИЛИ поле подсвечено ошибкой
    output = page.get_output_data()

    time.sleep(3)  # tmp solution

    assert output is None or page.is_email_error_present(), f"Email '{invalid_email}' не должен быть принят системой"

# --- 4. Избавился от цикла и добавил разных сценариев.
@pytest.mark.parametrize(
    "field_data",
    [
        {"name": "A" * 500},
        {"email": "a" * 250 + "@test.com"}, # тесты с данными в поле email
        {"cur_addr": "A" * 1000},
        {"perm_addr": "A" * 1000},
        {"name": "A" * 256},
        {"email": "A" * 256},
        {"cur_addr": "A" * 1000},
        {"perm_addr": "A" * 1000},
    ]
)
def test_long_input_fields(driver, field_data):
    page = TextBoxPage(driver).open()

    page.fill_form(**field_data)
    time.sleep(3)
    page.submit()

    assert page.get_output_data() is not None


# --- 5. Безопасность и спец-инъекции (XSS, SQL, Эмодзи) ---
# Добавил тетсы с разными сценариями
@pytest.mark.parametrize(
    "security_payload",
    [
        # XSS
        "<script>alert(1)</script>",
        "<img src=x onerror=alert(1)>",

        # HTML
        "<b>Bold</b>",
        "<iframe></iframe>",

        # SQL
        "' OR 1=1 --",
        "'; DROP TABLE users;--",

        # Эмодзи
        "😀😎🚀",
        "👨‍👩‍👧‍👦",
    ],)
def test_security_and_special_inputs(driver, security_payload):
    page = TextBoxPage(driver).open()
    # Заполняем все поля потенциально опасным контентом
    page.fill_form(name=security_payload, cur_addr=security_payload, perm_addr=security_payload)
    page.submit()
    output = page.get_output_data()

    time.sleep(3) # tmp solution

    assert output is not None, "Форма упала при вводе спецсимволов/инъекций"
    # Текст должен отобразиться строго как строка, а не выполниться кодом
    assert output["name"] == security_payload


# --- 6. Пустая форма ---
def test_empty_form_submission(driver):
    page = TextBoxPage(driver).open()
    page.submit()    
    output = page.get_output_data()

    time.sleep(3) # tmp solution

    if output is not None:
        assert output["name"] == ""
        assert output["email"] == ""

# Упало 15 тестов