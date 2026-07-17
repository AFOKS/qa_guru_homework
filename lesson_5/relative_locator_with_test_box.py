from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import time

driver = webdriver.Chrome()
driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
driver.maximize_window()

try:
    # 2. Открытие страницы
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)  # Пауза, чтобы визуально заметить открытие

    # 3. Поиск элементов и заполнение полей
    # Находим поле Full Name по его ID и вводим текст
    full_name_field = driver.find_element(By.ID, "userName")

    full_name_field.send_keys("Андрей Ажнов")

    # Находим поле Email по его ID и вводим текст
    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("andrey@guru.com")

    # 4. Находим поле Current Address и заполняем форму
    current_address_field = driver.find_element(By.ID, "currentAddress")
    current_address_field.send_keys("Город Москва; улица Ленина, дом 15, квартира 20")

    # 5. Находим поле Permanent Address и заполняем его

    permanent_address_field = driver.find_element(By.ID, "permanentAddress")
    permanent_address_field.send_keys("Город Москва; улица Пушкина, дом 70, квартира 89")

    # Находим кнопку Submit по ее ID и кликаем

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # . Проверка результата
    time.sleep(5)  # Пауза, чтобы увидеть результат отправки

    # Находим блок с отправленными данными
    result_box = driver.find_element(By.ID, "output")

    # Проверяем, что в блоке результата появился введенный текст
    assert "Город Москва; улица Пушкина, дом 70, квартира 89" in result_box.text
    print("Тест успешно пройден!")

finally:
    # 5. Закрытие браузера в любом случае
    driver.quit()