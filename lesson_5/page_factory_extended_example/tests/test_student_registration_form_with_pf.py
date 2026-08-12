import time

from pages.automation_practice_form_page import AutomationPracticeFormPage


def test_student_registration_form_max_capabilities(driver, upload_file):
    """
    Комплексный тест, валидирующий сквозной сценарий заполнения формы
    и корректность отображения данных в результирующем модальном окне.
    """

    # Инициализация POM-класса страницы
    page = AutomationPracticeFormPage(driver)

    page.open_url(
        "https://qa-guru.github.io/one-page-form/automation-practice-form.html"
    )

    # Заполнение персональной информации
    page.fill_personal_info(
        first_name="Ivan",
        last_name="Ivanov",
        email="ivanov@university.edu",
        gender="Male",
        mobile="1234567890"
    )

    # Дата рождения
    page.select_date_of_birth(
        year="2000",
        month="January",
        day="15"
    )

    # Предметы
    page.enter_subjects([
        "Maths",
        "Computer Science"
    ])

    # Хобби
    page.select_hobbies([
        "Sports",
        "Music"
    ])

    # Загрузка файла
    page.upload_file(upload_file)

    # Адрес и местоположение
    page.fill_address_and_location(
        address="123 University Avenue, Tomsk, Russia",
        state="NCR",
        city="Delhi"
    )

    # Отправка формы
    page.submit_form()

    time.sleep(3)

    # Получение результатов
    actual_results = page.get_modal_results()

    # Проверки
    assert actual_results.get("Student Name") == "Ivan Ivanov", (
        f"Ожидалось имя 'Ivan Ivanov', "
        f"получено: {actual_results.get('Student Name')}"
    )

    assert actual_results.get("Student Email") == "ivanov@university.edu"
    assert actual_results.get("Gender") == "Male"
    assert actual_results.get("Mobile") == "1234567890"
    assert actual_results.get("Date of Birth") == "15 Jan 2000"
    assert actual_results.get("Subjects") == "Maths, Computer Science"
    assert actual_results.get("Hobbies") == "Sports, Music"
    assert actual_results.get("Picture") == "demo_upload.txt"
    assert actual_results.get("Address") == "123 University Avenue, Tomsk, Russia"
    assert actual_results.get("State and City") == "NCR Delhi"

