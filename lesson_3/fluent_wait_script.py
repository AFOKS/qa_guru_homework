import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException



# Тест №1. Корретное заполнение всех полей

def test_fluent_wait():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Инициализация браузера

    try:
        # 1. Открытие тестовой страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")

        time.sleep(5)

        # 2. Заполнение полей формы
        driver.find_element(By.ID, "userName").send_keys("Иван Иванов")
        driver.find_element(By.ID, "userEmail").send_keys("ivan@example.com")
        driver.find_element(By.ID, "currentAddress").send_keys("ул. Ленина, дом 1")
        driver.find_element(By.ID, "permanentAddress").send_keys("ул. Пушкина, дом 10")

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
            poll_frequency=0.5,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        )

        # 4. Ожидание появления блока с результатами (id="output")
        output_block = fluent_wait.until(EC.visibility_of_element_located((By.ID, "output")))

        time.sleep(5)

        # 5. Проверка результата
        print("Тест №1 успешно пройден! Блок с результатами появился.")
        assert output_block.is_displayed()

    finally:
        # Закрытие браузера
        driver.quit()


# Тест 2. Ожидание и интервал опроса равны 0
# Все поля принимают пустые значения

def test_fluent_zero_wait():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Инициализация браузера

    try:
        # 1. Открытие тестовой страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")

        time.sleep(5)

        # 2. Заполнение полей формы
        driver.find_element(By.ID, "userName").send_keys("")
        driver.find_element(By.ID, "userEmail").send_keys("")
        driver.find_element(By.ID, "currentAddress").send_keys("")
        driver.find_element(By.ID, "permanentAddress").send_keys("")

        # Скролл до кнопки и клик
        submit_button = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

        # 3. Настройка Fluent Wait
        # timeout: максимальное время ожидания (0 секунд)
        # poll_frequency: интервал опроса страницы (0 секунд)
        # ignored_exceptions: список игнорируемых исключений во время опроса
        fluent_wait = WebDriverWait(
            driver,
            timeout=0,
            poll_frequency=0,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        )

        # 4. Ожидание появления блока с результатами (id="output")
        output_block = fluent_wait.until(EC.visibility_of_element_located((By.ID, "output")))

        time.sleep(5)

        # 5. Проверка результата
        print("Тест №2 успешно пройден! Блок с пустыми результатами появился.")
        assert output_block.is_displayed()

    finally:
        # Закрытие браузера
        driver.quit()

# Тест 3. # Все поля принимают специальные символы кроме Email

def test_invalid_characters_except_email():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Инициализация браузера

    try:
        # 1. Открытие тестовой страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")

        time.sleep(5)

        # 2. Заполнение полей формы
        driver.find_element(By.ID, "userName").send_keys("@")
        driver.find_element(By.ID, "userEmail").send_keys("zxc@searc.com")
        driver.find_element(By.ID, "currentAddress").send_keys("$")
        driver.find_element(By.ID, "permanentAddress").send_keys("%")

        # Скролл до кнопки и клик
        submit_button = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

        # 3. Настройка Fluent Wait
        # timeout: максимальное время ожидания (1 секунда)
        # poll_frequency: интервал опроса страницы (0.5 секунд)
        # ignored_exceptions: список игнорируемых исключений во время опроса
        fluent_wait = WebDriverWait(
            driver,
            timeout=1,
            poll_frequency=0.5,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        )

        # 4. Ожидание появления блока с результатами (id="output")
        output_block = fluent_wait.until(EC.visibility_of_element_located((By.ID, "output")))

        time.sleep(5)

        # 5. Проверка результата
        print("Тест №3 успешно пройден! Блок с результатами появился.")

        assert output_block.is_displayed()

    finally:
        # Закрытие браузера
        driver.quit()

# Тест 4. Заполнены только два поля: Имя и Email

def test_fluent_only_two_fields():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Инициализация браузера

    try:
        # 1. Открытие тестовой страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")

        time.sleep(5)

        # 2. Заполнение полей формы
        driver.find_element(By.ID, "userName").send_keys("Ivan Makarov")
        driver.find_element(By.ID, "userEmail").send_keys("makarov@searc.com")
        driver.find_element(By.ID, "currentAddress").send_keys("")
        driver.find_element(By.ID, "permanentAddress").send_keys("")

        # Скролл до кнопки и клик
        submit_button = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

        # 3. Настройка Fluent Wait
        # timeout: максимальное время ожидания (5 секунд)
        # poll_frequency: интервал опроса страницы (0.5 секунд)
        # ignored_exceptions: список игнорируемых исключений во время опроса
        fluent_wait = WebDriverWait(
            driver,
            timeout=5,
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

# Тест №5.Везде, кроме поля Email стоят пробелы перед  и после символов

def test_with_space():
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
        print("Тест №5 успешно пройден! Блок с результатами появился.")

        assert output_block.is_displayed()

    finally:
        # Закрытие браузера
        driver.quit()

test_fluent_wait()
test_fluent_zero_wait()
test_invalid_characters_except_email()
test_fluent_only_two_fields()
test_with_space()