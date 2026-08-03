import os
import time

from pages.automation_practice_form_page import AutomationPracticeFormPage


def test_student_registration_form_max_capabilities(driver):
    """
    Комплексный тест, валидирующий сквозной сценарий заполнения формы
    и корректность отображения данных в результирующем модальном окне.
    """
    # Подготовка тестового файла для демонстрации Upload функционала
    test_filename = "demo_upload.txt"
    with open(test_filename, "w") as f:
        f.write("QA Guru PageFactory Demo File Content")
    abs_file_path = os.path.abspath(test_filename)

    try:
        # Инициализация POM-класса страницы
        page = AutomationPracticeFormPage(driver)
        page.open_url("https://qa-guru.github.io/one-page-form/automation-practice-form.html")

        # Выполнение цепочки бизнес-действий
        page.fill_personal_info(
            first_name="Ivan",
            last_name="Ivanov",
            email="ivanov@university.edu",
            gender="Male",
            mobile="1234567890"
        )



        page.select_date_of_birth(
            year="2000",
            month="January",
            day="15"
        )

        page.enter_subjects([
            "Maths",
            "Computer Science"
        ])

        page.select_hobbies([
            "Sports",
            "Music"
        ])

        page.upload_file(abs_file_path)

        page.fill_address_and_location(
            address="123 University Avenue, Tomsk, Russia",
            state="NCR",
            city="Delhi"
        )
        page.submit_form()

        time.sleep(3)

        # Стадия верификации (Assertions) полученных результатов
        actual_results = page.get_modal_results()
        # Точечные жесткие проверки ключевых полей формы согласно ТЗ
        assert actual_results.get("Student Name") == "Ivan Ivanov", f"Ожидалось имя 'Ivan Ivanov', получено: {actual_results.get('Student Name')}"
        assert actual_results.get("Student Email") == "ivanov@university.edu"
        assert actual_results.get("Gender") == "Male"
        assert actual_results.get("Mobile") == "1234567890"
        assert actual_results.get("Date of Birth") == "15 Jan 2000"
        assert actual_results.get("Subjects") == "Maths, Computer Science"
        assert actual_results.get("Hobbies") == "Sports, Music"
        assert actual_results.get("Picture") == test_filename
        assert actual_results.get("Address") == "123 University Avenue, Tomsk, Russia"
        assert actual_results.get("State and City") == "NCR Delhi"
    finally:
        if os.path.exists(abs_file_path):
            os.remove(abs_file_path)
        pass
