import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

BASE_URL = "https://qa-guru.github.io/one-page-form/text-box.html"

@pytest.fixture
def driver():
    #Фикстура для создания и закрытия драйвера

    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

class TestTextBoxForm:
    TIMEOUT = 3

    def fill_form(self, driver, name, email, current_address, permanent_address):
        #Заполняет все поля формы

        driver.find_element(By.ID, "userName").send_keys(name)
        driver.find_element(By.ID, "userEmail").send_keys(email)
        driver.find_element(By.ID, "currentAddress").send_keys(current_address)
        driver.find_element(By.ID, "permanentAddress").send_keys(permanent_address)

    def submit_form(self, driver):
        #Нажимает кнопку Submit и ждет

        driver.find_element(By.ID, "submit").click()
        time.sleep(self.TIMEOUT)

    def get_result_text(self, driver):
        #Получает текст из блока результатов

        return driver.find_element(By.ID, "output").text

    def test_positive_valid_data(self, driver):
        # Позитивный тест: валидные данные

        self.fill_form(
            driver,
            "Иванов Иван",
            "ivanov@example.com",
            "Улица Копейкина, дом. Коруселькина",
            "Улица Копейкина, дом. Коруселькина"
        )

        self.submit_form(driver)
        result_text = self.get_result_text(driver)

        assert "Иванов Иван" in result_text
        assert "ivanov@example.com" in result_text
        assert "Улица Копейкина, дом. Коруселькина" in result_text

        print("\n✅ Тест №1 успешно пройден!")


def test_fluent_wait():
    self.fill_form(driver, "А", "a@b.com", "1", "2")
    self.submit_form(driver)
    result_text = self.get_result_text(driver)

    assert "A" in result_text
    assert "a@b.com" in result_text
    assert "1" in result_text
    assert "2" in result_text

    print("\n✅ Тест №2 успешно пройден!")




