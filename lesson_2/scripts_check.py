import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


def test_invalid_email():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Инициализация браузера

    try:
        # 1. Открытие тестовой страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")

        time.sleep(5)

        # 2. Заполнение полей формы
        driver.find_element(By.ID, "userName").send_keys("Viktor Messi")
        driver.find_element(By.ID, "userEmail").send_keys("messigoat/@.worldcup.win")
        driver.find_element(By.ID, "currentAddress").send_keys("Argentina")
        driver.find_element(By.ID, "permanentAddress").send_keys("USA")

        # Скролл до кнопки и клик
        submit_button = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

        # 3. Настройка Fluent Wait
        # timeout: максимальное время ожидания (10 секунд)
        # poll_frequency: интервал опроса страницы (0.5 секунды)
        # ignored_exceptions: список игнорируемых исключений во время опроса
        fluent_wait = WebDriverWait(
            driver,
            timeout=10,
            poll_frequency=10,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        )

        # 4. Ожидание появления блока с результатами (id="output")
        output_block = fluent_wait.until(EC.visibility_of_element_located((By.ID, "output")))

        time.sleep(5)

        # 5. Проверка результата

        assert output_block.is_enabled()

        print("Введите верные значения!!")

    finally:
        # Закрытие браузера
        driver.quit()
