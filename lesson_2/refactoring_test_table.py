import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class TableElement:
    """Page Element для работы с таблицей"""

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.table = driver.find_element(*locator)

    def get_headers(self):
        """Получить заголовки таблицы"""
        headers = self.table.find_elements(By.CSS_SELECTOR, "thead th")
        return [header.text for header in headers]

    def get_row_data(self, row_index):
        """Получить данные строки по индексу """
        rows = self.table.find_elements(By.CSS_SELECTOR, "tbody tr")
        cells = rows[row_index].find_elements(By.TAG_NAME, "td")
        return [cell.text for cell in cells]

    def get_cell_value(self, row_index, column_index):
        """Получить значение ячейки"""
        rows = self.table.find_elements(By.CSS_SELECTOR, "tbody tr")
        cells = rows[row_index].find_elements(By.TAG_NAME, "td")
        return cells[column_index].text

    def get_rows_count(self):
        """Получить количество строк в таблице"""
        rows = self.table.find_elements(By.CSS_SELECTOR, "tbody tr")
        return len(rows)


@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации WebDriver"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def table(driver):
    """Фикстура для инициализации таблицы"""
    driver.get("https://the-internet.herokuapp.com/tables")
    table_locator = (By.ID, "table1")
    return TableElement(driver, table_locator)


class TestTableValidation:
    """Тесты для валидации данных таблицы"""

    def test_table_headers_and_first_row(self, table):
        """Тест #1: Проверка заголовков и первой строки"""
        headers = table.get_headers()
        first_row = table.get_row_data(0)
        due_value = table.get_cell_value(row_index=2, column_index=3)

        print("\nЗаголовки таблицы:", headers)
        print("Первая строка данных:", first_row)
        print(f"Значение в строке 3, колонке 'Due': {due_value}")

        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Smith" in first_row, "Фамилия 'Smith' должна быть в первой строке"
        assert due_value == "$100.00", f"Ожидалось $100.00, но получено {due_value}"

        print("\n✅ Тест №1 успешно пройден!")

    def test_email_from_last_row(self, table):
        """Тест #2: Проверка Email из последней строки (строка 4, колонка 3)"""
        headers = table.get_headers()
        last_row_index = table.get_rows_count() - 1
        email_value = table.get_cell_value(row_index=last_row_index, column_index=2)

        print("\nЗаголовки таблицы:", headers)
        print(f"Значение в последней строке, колонке 'Email': {email_value}")

        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert email_value == "tconway@earthlink.net", \
            f"Ожидалось tconway@earthlink.net, но получено {email_value}"

        print("\n✅ Тест №2 успешно пройден!")

    def test_website_from_first_row(self, table):
        """Тест #3: Проверка Web site из первой строки (строка 1, колонка 4)"""
        headers = table.get_headers()
        website_value = table.get_cell_value(row_index=0, column_index=4)

        print("\nЗаголовки таблицы:", headers)
        print(f"Значение в строке 1, колонке 'Web site': {website_value}")

        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert website_value == "http://www.jsmith.com", \
            f"Ожидалось http://www.jsmith.com, но получено {website_value}"

        print("\n✅ Тест №3 успешно пройден!")

    def test_actions_and_fourth_row(self, table):
        """Тест #4: Проверка Actions из строки 2 + проверка 4 строки"""
        headers = table.get_headers()
        fourth_row = table.get_row_data(3)
        actions_value = table.get_cell_value(row_index=1, column_index=5)

        print("\nЗаголовки таблицы:", headers)
        print("Четвертая строка данных:", fourth_row)
        print(f"Значение в строке 2, колонке 'Actions': {actions_value}")

        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Conway" in fourth_row, "Фамилия 'Conway' должна быть в четвертой строке"
        assert actions_value == "edit delete", \
            f"Ожидалось 'edit delete', но получено {actions_value}"

        print("\n✅ Тест №4 успешно пройден!")
