import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# 1. Реализация Page Element для таблицы
class TableElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    @property
    def element(self):
        return self.driver.find_element(*self.locator)

    def get_headers(self) -> list[str]:
        """Возвращает список заголовков таблицы."""
        header_elements = self.element.find_elements(By.CSS_SELECTOR, "thead th")
        return [header.text for header in header_elements]

    def get_row_data(self, row_index: int) -> list[str]:
        """Возвращает данные конкретной строки по её индексу (начиная с 0)."""
        rows = self.element.find_elements(By.CSS_SELECTOR, "tbody tr")
        cells = rows[row_index].find_elements(By.TAG_NAME, "td")
        return [cell.text for cell in cells]

    def get_cell_value(self, row_index: int, column_index: int) -> str:
        """Возвращает значение конкретной ячейки."""
        rows = self.element.find_elements(By.CSS_SELECTOR, "tbody tr")
        cells = rows[row_index].find_elements(By.TAG_NAME, "td")
        return cells[column_index].text


# 2. Пример использования (Скрипт теста)

if __name__ == "__main__":
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        # Открытие страницы
        driver.get("https://the-internet.herokuapp.com/tables")

        # Инициализация таблицы как Page Element через её локатор
        table1_locator = (By.ID, "table1")
        table = TableElement(driver, table1_locator)

        # Сбор данных для демонстрации
        headers = table.get_headers()
        first_row = table.get_row_data(0)
        specific_cell = table.get_cell_value(row_index=2, column_index=3)  # Строка 3, Колонка 4 (Due)

        # Вывод результатов в консоль
        print("Заголовки таблицы:", headers)
        print("Первая строка данных:", first_row)
        print(f"Значение в строке 3, колонке 'Due': {specific_cell}")

        # Простые проверки (Assertions)
        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Smith" in first_row, "Фамилия 'Smith' должна быть в первой строке"
        assert specific_cell == "$100.00", f"Ожидалось $100.00, но получено {specific_cell}"

        print("\n✅ Тест №1 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()


 # Тест #2  с измененными данными. Выводим значение "Email из последней строки и 3 колонки"

if __name__ == "__main__":
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        # Открытие страницы
        driver.get("https://the-internet.herokuapp.com/tables")

        # Инициализация таблицы как Page Element через её локатор
        table1_locator = (By.ID, "table1")
        table = TableElement(driver, table1_locator)

        # Сбор данных для демонстрации
        headers = table.get_headers()
        first_row = table.get_row_data(0)
        specific_cell = table.get_cell_value(row_index=3, column_index=2)  # Строка 4, Колонка 3 Email)

        # Вывод результатов в консоль
        print("Заголовки таблицы:", headers)
        print("Первая строка данных:", first_row)
        print(f"Значение в строке 4, колонке 'Email': {specific_cell}")

        # Простые проверки (Assertions)
        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Smith" in first_row, "Фамилия 'Smith' должна быть в первой строке"
        assert specific_cell == "tconway@earthlink.net", f"Ожидалось tconway@earthlink.net, но получено {specific_cell}"

        print("\n✅ Тест №2 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()



#  Тест №3 с измененными данными. Выводим значение "Web site" из последней строки и 4 колонки"

if __name__ == "__main__":
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        # Открытие страницы
        driver.get("https://the-internet.herokuapp.com/tables")

        # Инициализация таблицы как Page Element через её локатор
        table1_locator = (By.ID, "table1")
        table = TableElement(driver, table1_locator)

        # Сбор данных для демонстрации
        headers = table.get_headers()
        first_row = table.get_row_data(0)
        specific_cell = table.get_cell_value(row_index=0, column_index=4)  # Строка 1, Колонка 4 (Web site)

        # Вывод результатов в консоль
        print("Заголовки таблицы:", headers)
        print("Первая строка данных:", first_row)
        print(f"Значение в строке 1, колонке 'Web site': {specific_cell}")

        # Простые проверки (Assertions)
        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Smith" in first_row, "Фамилия 'Smith' должна быть в первой строке"
        assert specific_cell == "http://www.jsmith.com", f"Ожидалось http://www.jsmith.com, но получено {specific_cell}"

        print("\n✅ Тест №3 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()


# Тест №4 с измененными данными. Выводим значение "Actions" из строки 2 и 4 колонки"
# Выводим значение строки 4

if __name__ == "__main__":
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        # Открытие страницы
        driver.get("https://the-internet.herokuapp.com/tables")

        # Инициализация таблицы как Page Element через её локатор
        table1_locator = (By.ID, "table1")
        table = TableElement(driver, table1_locator)

        # Сбор данных для демонстрации
        headers = table.get_headers()
        four_row = table.get_row_data(3)
        specific_cell = table.get_cell_value(row_index=1, column_index=5)  # Строка 2, Колонка 5 (Action)

        # Вывод результатов в консоль
        print("Заголовки таблицы:", headers)
        print("Четвертая строка данных:", four_row)
        print(f"Значение в строке 2, колонке 'Actions': {specific_cell}")

        # Простые проверки (Assertions)
        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Conway" in four_row, "Фамилия 'Conway' должна быть в четвертой строке"
        assert specific_cell == "edit delete", f"Ожидалось edit delete, но получено {specific_cell}"

        print("\n✅ Тест №4 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()