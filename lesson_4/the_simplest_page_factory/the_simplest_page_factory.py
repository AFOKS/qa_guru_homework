import time
from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

        self.locators = {
            "username_input": ("name", "email"),
            "password_input": ("name", "password"),
            "login_button": ("CSS", "button[data-qa='login-button']"),

            "signup_name": ("name", "name"),
            "signup_email": ("CSS", "input[data-qa='signup-email']"),
            "signup_button": ("CSS", "button[data-qa='signup-button']")
        }

    def login(self, email, password):
        self.username_input.set_text(email)
        self.password_input.set_text(password)

    def click_login(self):
        self.login_button.click()

    def signup(self, name, email):
        self.signup_name.set_text(name)
        self.signup_email.set_text(email)

    def click_signup(self):
        self.signup_button.click()


class TestSuite:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.automationexercise.com/login")
        self.page = LoginPage(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    # Тест 1. Успешная авторизация
    def test_login_success(self):
        self.setup()

        self.page.login("zxc@test.com", "123456")
        self.page.click_login()

        print("✅ test_login_success выполнен")

        self.teardown()

    # Тест 2. Авторизация с неверным паролем
    def test_login_wrong_password(self):
        self.setup()

        self.page.login("zxc@test.com", "111111")
        self.page.click_login()

        print("✅ test_login_wrong_password выполнен")

        self.teardown()

    # Тест 3. Авторизация с пустыми полями
    def test_login_empty_fields(self):
        self.setup()

        self.page.login("", "")
        self.page.click_login()

        print("✅ test_login_empty_fields выполнен")

        self.teardown()

    # Тест 4. Переход к регистрации
    def test_signup(self):
        self.setup()

        self.page.signup(
            "Andrey",
            "qabest@test.com"
        )
        self.page.click_signup()

        print("✅ test_signup выполнен")

        self.teardown()


if __name__ == "__main__":

    tests = TestSuite()

    tests.test_login_success()
    tests.test_login_wrong_password()
    tests.test_login_empty_fields()
    tests.test_signup()

