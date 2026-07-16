import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class Calendar:
    def __init__(self, driver, base_element):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.input_field = base_element

    def select_date(self, day: str, month: str, year: str):

        # Закрываем рекламный баннер, если он появился
        try:
            close_button = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "#fixedban button")
                )
            )
            close_button.click()

            self.wait.until(
                EC.invisibility_of_element(close_button)
            )
        except:
            # Баннер может отсутствовать
            pass

        self.input_field.click()

        # Выбираем месяц
        month_select = Select(
            self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
        )
        month_select.select_by_visible_text(month)

        # Выбираем год
        year_select = Select(
            self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
        )
        year_select.select_by_visible_text(year)

        # День должен быть с ведущим нулем
        day_padded = f"{int(day):03d}"

        self.driver.find_element(
            By.CSS_SELECTOR,
            f".react-datepicker__day--015:not(.react-datepicker__day--outside-month)"
        ).click()


class AutomationPracticeFormPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.get(
            "https://qa-guru.github.io/one-page-form/automation-practice-form.html"
        )
        self.driver.maximize_window()

        self.birthday_calendar = Calendar(
            self.driver,
            self.driver.find_element(By.ID, "dateOfBirthInput")
        )

    def close(self):
        self.driver.quit()


class TestSuite:
    def test_select_birthday_date(self):
        page = AutomationPracticeFormPage()

        try:
            page.birthday_calendar.select_date(
                day="15",
                month="June",
                year="2000"
            )

            assert (
                    page.birthday_calendar.input_field.get_attribute("value")
                    == "15 Jun 2000"
            )
        finally:
            time.sleep(3)
            page.close()
            print("Тест успешно пройдет!!!")

ts = TestSuite()
ts.test_select_birthday_date()
