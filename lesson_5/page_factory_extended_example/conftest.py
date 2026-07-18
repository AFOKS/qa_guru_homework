import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    """
    Инициализация WebDriver.
    После завершения теста браузер автоматически закрывается.
    """

    chrome_options = Options()

    # Для локальной отладки можно закомментировать следующую строку
    # chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def upload_file():
    """
    Создает временный файл для проверки загрузки файлов.
    После завершения теста файл удаляется автоматически.
    """

    file_name = "demo_upload.txt"

    with open(file_name, "w", encoding="utf-8") as file:
        file.write("QA Guru Selenium PageFactory Demo File")

    absolute_path = os.path.abspath(file_name)

    yield absolute_path

    if os.path.exists(absolute_path):
        os.remove(absolute_path)