import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

def test_fluent_only_two_fields():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Инициализация браузера

    try:
        # 1. Открытие тестовой страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")

        time.sleep(5)

        # 2. Заполнение полей формы
        driver.find_element(By.ID, "userName").send_keys("  A N ")
        driver.find_element(By.ID, "userEmail").send_keys("makarov@searc.com")
        driver.find_element(By.ID, "currentAddress").send_keys("  D R")
        driver.find_element(By.ID, "permanentAddress").send_keys("  E Y ")

        # Скролл до кнопки и клик
        submit_button = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

        # 3. Настройка Fluent Wait
        # timeout: максимальное время ожидания (0 секунд)
        # poll_frequency: интервал опроса страницы (0.5 секунд)
        # ignored_exceptions: список игнорируемых исключений во время опроса
        fluent_wait = WebDriverWait(
            driver,
            timeout=0,
            poll_frequency=0.5,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        )

        # 4. Ожидание появления блока с результатами (id="output")
        output_block = fluent_wait.until(EC.visibility_of_element_located((By.ID, "output")))

        time.sleep(5)

        # 5. Проверка результата
        print("Тест №4 успешно пройден! Блок с результатами появился.")

        assert output_block.is_displayed()

    finally:
        # Закрытие браузера
        driver.quit()