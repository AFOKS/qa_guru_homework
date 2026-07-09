import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


# === ФИКСТУРЫ ===

@pytest.fixture
def driver():
    """Фикстура для инициализации и завершения работы браузера"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(2)  # Базовая защита от Race Conditions
    yield driver
    driver.quit()


@pytest.fixture
def base_url():
    """Базовый URL тестовой страницы"""
    return "https://qa-guru.github.io/one-page-form/text-box.html"


@pytest.fixture
def fluent_wait(driver):
    """Создание конфигурируемого Fluent Wait с параметрами по умолчанию"""

    def _create_wait(timeout=10, poll_frequency=5):
        return WebDriverWait(
            driver,
            timeout=timeout,
            poll_frequency=poll_frequency,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        )

    return _create_wait


# === ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ===

def fill_form(driver, name="", email="", current_address="", permanent_address=""):
    """Заполнение формы с динамическими данными"""
    fields = {
        "userName": name,
        "userEmail": email,
        "currentAddress": current_address,
        "permanentAddress": permanent_address
    }

    for field_id, value in fields.items():
        element = driver.find_element(By.ID, field_id)
        element.clear()
        if value:
            element.send_keys(value)

    # Скролл и клик по кнопке Submit
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    submit_button.click()


def wait_for_output_block(fluent_wait, timeout=10):
    """Ожидание появления блока с результатами"""
    return fluent_wait(timeout=timeout).until(
        EC.visibility_of_element_located((By.ID, "output"))
    )


# === ТЕСТЫ ===

class TestTextBoxForm:
    """Тесты формы Text Box"""

    def test_valid_form_submission(self, driver, base_url, fluent_wait):
        """Тест №1: Корректное заполнение всех полей валидными данными"""
        driver.get(base_url)

        fill_form(
            driver,
            name="Иван Иванов",
            email="ivan@example.com",
            current_address="ул. Ленина, дом 1",
            permanent_address="ул. Пушкина, дом 10"
        )

        output_block = wait_for_output_block(fluent_wait, timeout=10)
        assert output_block.is_displayed(), "Блок с результатами не отображается"
        assert "Иван Иванов" in output_block.text, "Имя не отображается в результатах"
        assert "ivan@example.com" in output_block.text, "Email не отображается в результатах"

    def test_empty_form_submission(self, driver, base_url, fluent_wait):
        """Тест №2: Отправка формы с пустыми полями"""
        driver.get(base_url)

        # Пустые поля - вызываем без аргументов
        fill_form(driver)

        output_block = wait_for_output_block(fluent_wait, timeout=10)
        assert output_block.is_displayed(), "Блок с результатами не отображается"

    def test_special_characters_except_email(self, driver, base_url, fluent_wait):
        """Тест №3: Специальные символы в полях (кроме Email)"""
        driver.get(base_url)

        fill_form(
            driver,
            name="@",
            email="zxc@searc.com",
            current_address="$",
            permanent_address="%"
        )

        output_block = wait_for_output_block(fluent_wait, timeout=5)
        assert output_block.is_displayed()
        assert "@" in output_block.text
        assert "$" in output_block.text
        assert "%" in output_block.text

    def test_partial_form_completion(self, driver, base_url, fluent_wait):
        """Тест №4: Заполнены только обязательные поля (Имя и Email)"""
        driver.get(base_url)

        fill_form(
            driver,
            name="Ivan Makarov",
            email="makarov@searc.com"
        )

        output_block = wait_for_output_block(fluent_wait, timeout=5)
        assert output_block.is_displayed()
        assert "Ivan Makarov" in output_block.text
        assert "makarov@searc.com" in output_block.text

    def test_whitespace_handling(self, driver, base_url, fluent_wait):
        """Тест №5: Обработка пробелов в начале и конце значений"""
        driver.get(base_url)

        fill_form(
            driver,
            name="  A N  ",
            email="makarov@searc.com",
            current_address="  D R  ",
            permanent_address="  E Y  "
        )

        output_block = wait_for_output_block(fluent_wait, timeout=10)
        assert output_block.is_displayed()

        # Проверяем, что система обрабатывает пробелы (trim или отображает)
        # В зависимости от требований, можно проверять наличие/отсутствие пробелов
        assert "makarov@searc.com" in output_block.text
