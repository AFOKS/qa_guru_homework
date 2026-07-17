import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

# Переписал тест для новой страницы
driver = webdriver.Chrome()
driver.get("https://qa-guru.github.io/one-page-form/automation-practice-form.html")
driver.maximize_window()

time.sleep(2)

# Закрываем рекламный баннер, если он перекрывает элементы
driver.execute_script("document.querySelector('#fixedban').style.display='none'")
driver.execute_script("document.querySelector('footer').style.display='none'")

# -------------------------
# First Name
# -------------------------
first_name_label = driver.find_element(By.XPATH, "//*[@id='firstName']")

first_name_input = driver.find_element(
    locate_with(By.TAG_NAME, "input").below(first_name_label)
)

first_name_label.send_keys("Ivan")

time.sleep(2)

# -------------------------
# Email (поле находится выше кнопки Submit)
# -------------------------
submit_btn = driver.find_element(By.ID, "submit")

email_input = driver.find_element(
    locate_with(By.ID, "userEmail").above(submit_btn)
)

email_input.send_keys("ivan@example.com")

time.sleep(2)

# -------------------------
# Клик по Male (слева от Female)
# Кликаем по LABEL, а не INPUT
# -------------------------
female_label = driver.find_element(By.XPATH, "//label[@for='gender-radio-2']")

male_label = driver.find_element(
    locate_with(By.TAG_NAME, "label").to_left_of(female_label)
)

male_label.click()

time.sleep(2)

# -------------------------
# Клик по Female (справа от Male)
# -------------------------
male_label = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")

female_label = driver.find_element(
    locate_with(By.TAG_NAME, "label").to_right_of(male_label)
)

female_label.click()

time.sleep(2)

# -------------------------
# Current Address
# -------------------------
address_label = driver.find_element(By.XPATH, "//label[text()='Current Address']")

address = driver.find_element(
    locate_with(By.TAG_NAME, "textarea").near(address_label)
)

address.send_keys("г. Минск, ул. Академическая")

time.sleep(5)

driver.quit()