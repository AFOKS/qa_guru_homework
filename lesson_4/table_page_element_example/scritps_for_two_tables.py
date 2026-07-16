import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Реализация Page Element для таблицы
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


# Тест №1 для двух таблиц

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
        table2_locator = (By.ID, "table2")
        table = TableElement(driver, table1_locator)
        table_02 = TableElement(driver, table2_locator)

        # Сбор данных для демонстрации Таблица №1
        headers = table.get_headers()
        first_row = table.get_row_data(0)  # Первоя строка
        specific_cell = table.get_cell_value(row_index=2, column_index=3)  # Строка 3, Колонка 4 (Due)
        # Сбор данных для демонстрации Таблица №2
        headers_2 = table_02.get_headers()
        first_row_2 = table_02.get_row_data(1)  # Вторая строка
        specific_cell_2 = table_02.get_cell_value(row_index=1, column_index=2)  # Строка 2, Колонка 3 (Email)

        # Вывод результатов в консоль для таблицы 1
        print("Данные первой таблицы")
        print("Заголовки таблицы №1:", headers)
        print("Первая строка данных в таблице №1:", first_row)
        print(f"Значение в строке 3, колонке 'Due' в табдлице №1: {specific_cell}")

        # Вывод результатов в консоль для таблицы 2
        print("Данные второй таблицы")
        print("Заголовки таблицы №2:", headers_2)
        print("Первая строка данных таблицы №2:", first_row_2)
        print(f"Значение в строке 3, колонке 'Email' в таблице №2: {specific_cell_2}")

        # Простые проверки (Assertions) для таблицы 1
        assert "Last Name" in headers, "Заголовок 'Last Name' не найден в таблице №1"
        assert "Smith" in first_row, "Фамилия 'Smith' должна быть в первой строке в таблице №1"
        assert specific_cell == "$100.00", f"Ожидалось $100.00, но получено {specific_cell} в таблице №1"

        # Простые проверки (Assertions) для таблицы 2
        assert "Last Name" in headers_2, "Заголовок 'Last Name' не найден в таблице №2"
        assert "Bach" in first_row_2, "Фамилия 'Bach' должна быть во второй строке в таблице №2"
        assert specific_cell_2 == "fbach@yahoo.com", f"Ожидалось fbach@yahoo.com, но получено {specific_cell_2} в таблице №2"

        print("\n✅ Тест №1 для двух таблиц успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()

# Тест №2 для двух таблиц

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
        table2_locator = (By.ID, "table2")
        table = TableElement(driver, table1_locator)
        table_02 = TableElement(driver, table2_locator)

        # Сбор данных для демонстрации Таблица №1
        headers = table.get_headers()
        first_row = table.get_row_data(3)  # 4 строка в таблице №1
        specific_cell = table.get_cell_value(row_index=0, column_index=4)  # Строка 1, Колонка 5 (Web Site)
        # Сбор данных для демонстрации Таблица №2
        headers_2 = table_02.get_headers()
        first_row_2 = table_02.get_row_data(1)  # 2 строка в таблице №2
        specific_cell_2 = table_02.get_cell_value(row_index=3, column_index=4)  # Строка 4, Колонка 5 (Web Site)

        # Вывод результатов в консоль для таблицы 1
        print("Данные первой таблицы")
        print("Заголовки таблицы №1:", headers)
        print("Четвертая строка данных таблицы №1:", first_row)
        print(f"Значение в строке 1, колонке 'Web site' в таблице №1: {specific_cell}")

        # Вывод результатов в консоль для таблицы 2
        print("Данные второй таблицы")
        print("Заголовки таблицы №2:", headers_2)
        print("Вторая строка данных таблицы №2:", first_row_2)
        print(f"Значение в строке 4, колонке 'Web site' в таблице №2: {specific_cell_2}")

        # Простые проверки (Assertions) для таблицы 1
        assert "Last Name" in headers, "Заголовок 'Last Name' не найден в таблице №1"
        assert "Conway" in first_row, "Фамилия 'Conway' должна быть в четвертой строке в таблице №1"
        assert specific_cell == "http://www.jsmith.com", f"Ожидалось http://www.jsmith.com, но получено {specific_cell} в таблице №1"

        # Простые проверки (Assertions) для таблицы 2
        assert "Last Name" in headers_2, "Заголовок 'Last Name' не найден в таблице №2"
        assert "Bach" in first_row_2, "Фамилия 'Bach' должна быть во второй строке в таблице №2"
        assert specific_cell_2 == "http://www.timconway.com", f"Ожидалось http://www.timconway.com, но получено {specific_cell_2} в таблице №2"

        print("\n✅ Тест №2 для двух таблиц успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()

# Тест №3 для двух таблиц

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
        table2_locator = (By.ID, "table2")
        table = TableElement(driver, table1_locator)
        table_02 = TableElement(driver, table2_locator)

        # Сбор данных для демонстрации Таблица №1
        headers = table.get_headers()
        first_row = table.get_row_data(1)  # 2 строка в таблице №1
        specific_cell = table.get_cell_value(row_index=2, column_index=3)  # Строка 3, Колонка 3 (Due)
        # Сбор данных для демонстрации Таблица №2
        headers_2 = table_02.get_headers()
        first_row_2 = table_02.get_row_data(2)  # 3 строка в таблице №2
        specific_cell_2 = table_02.get_cell_value(row_index=1, column_index=5)  # Строка 2, Колонка 6 (Action)

        # Вывод результатов в консоль для таблицы 1
        print("Данные первой таблицы")
        print("Заголовки таблицы №1:", headers)
        print("Вторая строка данных таблицы №1:", first_row)
        print(f"Значение в строке 3, колонке 'Due' в таблице №1: {specific_cell}")

        # Вывод результатов в консоль для таблицы 2
        print("Данные второй таблицы")
        print("Заголовки таблицы №2:", headers_2)
        print("Третья строка данных таблицы №2:", first_row_2)
        print(f"Значение в строке 2, колонке 'Action' в таблице №2: {specific_cell_2}")

        # Простые проверки (Assertions) для таблицы 1
        assert "Last Name" in headers, "Заголовок 'Last Name' не найден в таблице №1"
        assert "Bach" in first_row, "Фамилия 'Bach' должна быть во второй строке в таблице №1"
        assert specific_cell == "$100.00", f"Ожидалось $100.00, но получено {specific_cell} в таблице №1"

        # Простые проверки (Assertions) для таблицы 2
        assert "Last Name" in headers_2, "Заголовок 'Last Name' не найден в таблице №2"
        assert "Doe" in first_row_2, "Фамилия 'Doe' должна быть в третьей строке в таблице №2"
        assert specific_cell_2 == "edit delete", f"Ожидалось edit delete, но получено {specific_cell_2} в таблице №2"

        print("\n✅ Тест №3 для двух таблиц успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()

# Тест №4 для двух таблиц

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
        table2_locator = (By.ID, "table2")
        table = TableElement(driver, table1_locator)
        table_02 = TableElement(driver, table2_locator)

        # Сбор данных для демонстрации Таблица №1
        headers = table.get_headers()
        first_row = table.get_row_data(3)  # 4 строка в таблице №1
        specific_cell = table.get_cell_value(row_index=2, column_index=2)  # Строка 3, Колонка 3 (Email)
        # Сбор данных для демонстрации Таблица №2
        headers_2 = table_02.get_headers()
        first_row_2 = table_02.get_row_data(1)  # 2 строка в таблице №2
        specific_cell_2 = table_02.get_cell_value(row_index=2, column_index=2)  # Строка 3, Колонка 3 (Email)

        # Вывод результатов в консоль для таблицы 1
        print("Данные первой таблицы")
        print("Заголовки таблицы №1:", headers)
        print("Четвертая строка данных таблицы №1:", first_row)
        print(f"Значение в строке 3, колонке 'Email' в таблице №1: {specific_cell}")

        # Вывод результатов в консоль для таблицы 2
        print("Данные второй таблицы")
        print("Заголовки таблицы №2:", headers_2)
        print("Вторая строка данных таблицы №2:", first_row_2)
        print(f"Значение в строке 3, колонке 'Email' в таблице №2: {specific_cell_2}")

        # Простые проверки (Assertions) для таблицы 1
        assert "Last Name" in headers, "Заголовок 'Last Name' не найден в таблице №1"
        assert "Conway" in first_row, "Фамилия 'Conway' должна быть в четвертой строке в таблице №1"
        assert specific_cell == "jdoe@hotmail.com", f"Ожидалось jdoe@hotmail.com, но получено {specific_cell} в таблице №1"

        # Простые проверки (Assertions) для таблицы 2
        assert "Last Name" in headers_2, "Заголовок 'Last Name' не найден в таблице №2"
        assert "Bach" in first_row_2, "Фамилия 'Bach' должна быть во второй строке в таблице №2"
        assert specific_cell_2 == "jdoe@hotmail.com", f"Ожидалось jdoe@hotmail.com, но получено {specific_cell_2} в таблице №2"

        print("\n✅ Тест №4 для двух таблиц успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()

# Тест №5 для двух таблиц

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
        table2_locator = (By.ID, "table2")
        table = TableElement(driver, table1_locator)
        table_02 = TableElement(driver, table2_locator)

        # Сбор данных для демонстрации Таблица №1
        headers = table.get_headers()
        first_row = table.get_row_data(1)  # 2 строка в таблице №1
        specific_cell = table.get_cell_value(row_index=2, column_index=1)  # Строка 3, Колонка 2 (First name)
        # Сбор данных для демонстрации Таблица №2
        headers_2 = table_02.get_headers()
        first_row_2 = table_02.get_row_data(2)  # 3 строка в таблице №2
        specific_cell_2 = table_02.get_cell_value(row_index=3, column_index=4)  # Строка 4, Колонка 5 (Web site)

        # Вывод результатов в консоль для таблицы 1
        print("Данные первой таблицы")
        print("Заголовки таблицы №1:", headers)
        print("Вторая строка данных таблицы №1:", first_row)
        print(f"Значение в строке 3, колонке 'First name' в таблице №1: {specific_cell}")

        # Вывод результатов в консоль для таблицы 2
        print("Данные второй таблицы")
        print("Заголовки таблицы №2:", headers_2)
        print("Третья строка данных таблицы №2:", first_row_2)
        print(f"Значение в строке 3, колонке 'Email' в таблице №2: {specific_cell_2}")

        # Простые проверки (Assertions) для таблицы 1
        assert "Last Name" in headers, "Заголовок 'Last Name' не найден в таблице №1"
        assert "Bach" in first_row, "Фамилия 'Bach' должна быть во второй строке в таблице №1"
        assert specific_cell == "Jason", f"Ожидалось Jason, но получено {specific_cell} в таблице №1"

        # Простые проверки (Assertions) для таблицы 2
        assert "Last Name" in headers_2, "Заголовок 'Last Name' не найден в таблице №2"
        assert "Doe" in first_row_2, "Фамилия 'Doe' должна быть в третьей строке в таблице №2"
        assert specific_cell_2 == "http://www.timconway.com", f"Ожидалось http://www.timconway.com, но получено {specific_cell_2} в таблице №2"

        print("\n✅ Тест №5 для двух таблиц успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()
