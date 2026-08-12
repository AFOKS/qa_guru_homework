import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Добавил ожидания

@pytest.fixture
def desktop_browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)

    yield driver

    driver.quit()


@pytest.fixture
def mobile_browser():
    driver = webdriver.Chrome()
    driver.set_window_size(390, 844)

    yield driver

    driver.quit()

# Добавил ожидания на появления элементов
def test_github_sign_up_desktop(desktop_browser):
    desktop_browser.get("https://github.com/")

    sign_up = WebDriverWait(desktop_browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(normalize-space(), 'Sign up')]")
        )
    )

    sign_up.click()

    WebDriverWait(desktop_browser, 10).until(
        EC.url_contains("/signup")
    )

    assert "/signup" in desktop_browser.current_url


def test_github_sign_up_mobile(mobile_browser):
    mobile_browser.get("https://github.com/")

    # Открываем бургер-меню
    mobile_browser.find_element(
        By.CSS_SELECTOR,
        "button[aria-label='Toggle navigation']"
    ).click()

    # Кликаем Sign up
    mobile_browser.find_element(
        By.XPATH,
        "//a[normalize-space()='Sign up']"
    ).click()

    assert "/signup" in mobile_browser.current_url