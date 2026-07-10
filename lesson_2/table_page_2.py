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
        # TODDO: 1) как переписать используя вызов get_row_data ?
        return cells[column_index].text


# Таблица 2. Тест 1
if __name__ == "__main__":
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        # Открытие страницы
        driver.get("https://the-internet.herokuapp.com/tables")

        # Инициализация таблицы как Page Element через её локатор
        table2_locator = (By.ID, "table2")
        table = TableElement(driver, table2_locator)

        # Сбор данных для демонстрации
        headers = table.get_headers()
        second_row = table.get_row_data(1)  # строка 2
        specific_cell = table.get_cell_value(row_index=3, column_index=1)  # Строка 4, Колонка 2 (First Name)

        # Вывод результатов в консоль
        print("Заголовки таблицы:", headers)
        print("Вторая строка данных:", second_row)
        print(f"Значение в строке 4, колонке 'First name': {specific_cell}")

        # Простые проверки (Assertions)
        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Bach" in second_row, "Фамилия 'Bach' должна быть во второй строке"
        assert specific_cell == "Tim", f"Ожидалось Tim, но получено {specific_cell}"

        print("\n✅ Тест №1 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()

# Таблица 2. Тест 2

if __name__ == "__main__":
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        # Открытие страницы
        driver.get("https://the-internet.herokuapp.com/tables")

        # Инициализация таблицы как Page Element через её локатор
        table2_locator = (By.ID, "table2")
        table = TableElement(driver, table2_locator)

        # Сбор данных для демонстрации
        headers = table.get_headers()
        third_row = table.get_row_data(2)  # строка 3
        specific_cell = table.get_cell_value(row_index=0, column_index=4)  # Строка 1, Колонка 4 (Web Site)

        # Вывод результатов в консоль
        print("Заголовки таблицы:", headers)
        print("Третья строка данных:", third_row)
        print(f"Значение в строке 1, колонке 'Web site': {specific_cell}")

        # Простые проверки (Assertions)
        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Doe" in third_row, "Фамилия 'Doe' должна быть в третьей строке"
        assert specific_cell == "http://www.jsmith.com", f"Ожидалось http://www.jsmith.com, но получено {specific_cell}"

        print("\n✅ Тест №2 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()

# Таблица 2. Тест 3

if __name__ == "__main__":
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        # Открытие страницы
        driver.get("https://the-internet.herokuapp.com/tables")

        # Инициализация таблицы как Page Element через её локатор
        table2_locator = (By.ID, "table2")
        table = TableElement(driver, table2_locator)

        # Сбор данных для демонстрации
        headers = table.get_headers()
        four_row = table.get_row_data(3)  # строка 4
        specific_cell = table.get_cell_value(row_index=2, column_index=3)  # Строка 3, Колонка 4 (Due)

        # Вывод результатов в консоль
        print("Заголовки таблицы:", headers)
        print("Четвертая строка данных:", four_row)
        print(f"Значение в строке 3, колонке 'Due': {specific_cell}")

        # Простые проверки (Assertions)
        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Conway" in four_row, "Фамилия 'Conway' должна быть в четвертой строке"
        assert specific_cell == "$100.00", f"$100.00, но получено {specific_cell}"

        print("\n✅ Тест №3 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()

# Таблица 2. Тест 4

if __name__ == "__main__":
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        # Открытие страницы
        driver.get("https://the-internet.herokuapp.com/tables")

        # Инициализация таблицы как Page Element через её локатор
        table2_locator = (By.ID, "table2")
        table = TableElement(driver, table2_locator)

        # Сбор данных для демонстрации
        headers = table.get_headers()
        first_row = table.get_row_data(0)  # строка 1
        specific_cell = table.get_cell_value(row_index=1, column_index=2)  # Строка 2, Колонка 3 (Email)

        # Вывод результатов в консоль
        print("Заголовки таблицы:", headers)
        print("Первая строка данных:", first_row)
        print(f"Значение в строке 2, колонке 'Email': {specific_cell}")

        # Простые проверки (Assertions)
        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Smith" in first_row, "Фамилия 'Smith' должна быть в первой строке"
        assert specific_cell == "fbach@yahoo.com", f"fbach@yahoo.com, но получено {specific_cell}"

        print("\n✅ Тест №4 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()

# Таблица 2. Тест 5

if __name__ == "__main__":
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        # Открытие страницы
        driver.get("https://the-internet.herokuapp.com/tables")

        # Инициализация таблицы как Page Element через её локатор
        table2_locator = (By.ID, "table2")
        table = TableElement(driver, table2_locator)

        # Сбор данных для демонстрации
        headers = table.get_headers()
        third_row = table.get_row_data(3)  # строка 4
        specific_cell = table.get_cell_value(row_index=2, column_index=4)  # Строка 3, Колонка 4 (Web site)

        # Вывод результатов в консоль
        print("Заголовки таблицы:", headers)
        print("Четвертая строка данных:", third_row)
        print(f"Значение в строке 3, колонке 'Web site': {specific_cell}")

        # Простые проверки (Assertions)
        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Conway" in third_row, "Фамилия 'Conway' должна быть в четвертой строке"
        assert specific_cell == "http://www.jdoe.com", f"http://www.jdoe.com, но получено {specific_cell}"

        print("\n✅ Тест №5 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()
