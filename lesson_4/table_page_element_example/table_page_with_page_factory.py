import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory


class TablesPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

        self.locators = {
            "table1": (By.ID, "table1"),
            "table2": (By.ID, "table2")
        }

    def get_headers(self, table):
        headers = table.find_elements(By.CSS_SELECTOR, "thead th")
        return [header.text for header in headers]

    def get_row_data(self, table, row_index):
        rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
        cells = rows[row_index].find_elements(By.TAG_NAME, "td")
        return [cell.text for cell in cells]

    def get_cell_value(self, table, row_index, column_index):
        return self.get_row_data(table, row_index)[column_index]

class TestTables:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/tables")

        self.page = TablesPage(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_table1(self):

        self.setup()

        headers = self.page.get_headers(self.page.table1)
        row = self.page.get_row_data(self.page.table1, 0)
        due = self.page.get_cell_value(self.page.table1, 2, 3)

        assert "Last Name" in headers
        assert "Smith" in row
        assert due == "$100.00"

        print("✅ Тест №1 пройден")

        self.teardown()

    def test_table2(self):

        self.setup()

        headers = self.page.get_headers(self.page.table2)
        row = self.page.get_row_data(self.page.table2, 1)
        email = self.page.get_cell_value(self.page.table2, 1, 2)

        assert "Last Name" in headers
        assert "Bach" in row
        assert email == "fbach@yahoo.com"

        print("✅ Тест №2 пройден")

        self.teardown()

    def test_table3(self):

        self.setup()

        row = self.page.get_row_data(self.page.table1, 3)
        website = self.page.get_cell_value(self.page.table2, 3, 4)

        assert "Conway" in row
        assert website == "http://www.timconway.com"

        print("✅ Тест №3 пройден")

        self.teardown()

    def test_table4(self):

        self.setup()

        email = self.page.get_cell_value(self.page.table1, 2, 2)

        assert email == "jdoe@hotmail.com"

        print("✅ Тест №4 пройден")

        self.teardown()

    def test_table5(self):

        self.setup()

        firstname = self.page.get_cell_value(self.page.table1, 2, 1)

        assert firstname == "Jason"

        print("✅ Тест №5 пройден")

        self.teardown()

if __name__ == "__main__":

    tests = TestTables()

    tests.test_table1()
    tests.test_table2()
    tests.test_table3()
    tests.test_table4()
    tests.test_table5()