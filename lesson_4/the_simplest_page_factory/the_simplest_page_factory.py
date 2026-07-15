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
        }

    # Метод, использующий возможности Page Factory
    def login(self, email, password):
        # Элементы инициализируются «на лету» и имеют расширенные методы
        self.username_input.set_text(email)  # Ввод текста + очистка
        self.password_input.set_text(password)

    def click_login(self):
        self.login_button.click()

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