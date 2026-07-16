import time
from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory

# Создал тест но авторизацию
# 1. Описываем класс страницы, наследуясь от PageFactory
class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        # Локаторы задаются в виде словаря. Ключ станет именем переменной-элемента.
        self.locators = {
            "username_input": ('name', 'email'),
            "password_input": ('name', 'password'),
            "login_button": ("CSS", "button[data-qa='login-button']"),
            "signup_name": ('name', 'name'),
            "signup_email": ('name', 'email'),
            "signup_button": ("CSS", "button[data-qa='signup-button']")
        }

    # Метод, использующий возможности Page Factory
    def login(self, email, password):
        # Элементы инициализируются «на лету» и имеют расширенные методы
        self.username_input.set_text(email)  # Ввод текста + очистка
        self.password_input.set_text(password)


    def click_login(self):
        self.login_button.click()
    def signup(self, name, email,):
        self.signup_name.set_text(name)
        self.signup_email.set_text(email)
# 2. Основной скрипт теста
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.automationexercise.com/login")
    
    # Инициализация страницы
    login_page = LoginPage(driver)
    
    # Вызов логики
    login_page.login("zxc@test.com", "123456")
    login_page.click_login()
    
    time.sleep(5)
    driver.quit()
    print("Тест на аторизацию успешно пройден!!")

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.automationexercise.com/login")

    # Инициализация страницы
    signup_page = SignupPage(driver)

    # Вызов логики
    signup_page.login("zxcc@test.com", "1234567")
    signup_page.click_login()

    time.sleep(5)
    driver.quit()
    print("Тест на регситрацию успешно пройден!!")