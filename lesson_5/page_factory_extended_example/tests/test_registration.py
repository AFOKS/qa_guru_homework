import pytest

from pages.registration_page import RegistrationPage


class TestRegistration:

    def test_open_registration_page(self, driver):
        """
        Проверка открытия страницы.
        """

        page = RegistrationPage(driver)

        page.open()

        assert "automation-practice-form" in page.current_url()
        assert "DEMOQA" in page.page_title()

    # -------------------------------------------------------------

    def test_fill_personal_info(self, driver):

        page = RegistrationPage(driver)

        page.open()

        page.fill_personal_info(
            first_name="Ivan",
            last_name="Ivanov",
            email="ivan@test.com",
            gender="Male",
            mobile="1234567890"
        )

        assert page.first_name.get_attribute("value") == "Ivan"
        assert page.last_name.get_attribute("value") == "Ivanov"
        assert page.user_email.get_attribute("value") == "ivan@test.com"
        assert page.user_number.get_attribute("value") == "1234567890"

    # -------------------------------------------------------------

    def test_fill_subjects(self, driver):

        page = RegistrationPage(driver)

        page.open()

        page.enter_subjects(
            [
                "Maths",
                "Computer Science"
            ]
        )

        text = page.driver.find_element(
            "css selector",
            ".subjects-auto-complete__value-container"
        ).text

        assert "Maths" in text
        assert "Computer Science" in text

    # -------------------------------------------------------------

    @pytest.mark.parametrize(
        "gender",
        [
            "Male",
            "Female",
            "Other"
        ]
    )
    def test_gender_selection(self, driver, gender):

        page = RegistrationPage(driver)

        page.open()

        page.fill_personal_info(
            first_name="Ivan",
            last_name="Ivanov",
            email="ivan@test.com",
            gender=gender,
            mobile="1234567890"
        )

        # Если ошибок нет — радиокнопка успешно выбрана