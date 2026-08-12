import pytest
from collections.abc import Generator

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def browser(request) -> Generator[WebDriver, None, None]:
    driver = webdriver.Chrome()

    if request.param == "desktop":
        driver.set_window_size(1920, 1080)

    elif request.param == "mobile":
        driver.set_window_size(390, 844)

    yield driver

    driver.quit()


@pytest.mark.parametrize("browser", ["desktop"], indirect=True)
def test_github_desktop(browser: WebDriver):
    browser.get("https://github.com/")

    sign_up = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(normalize-space(), 'Sign up')]")
        )
    )

    sign_up.click()

    WebDriverWait(browser, 10).until(
        EC.url_contains("/signup")
    )

    assert "/signup" in browser.current_url


@pytest.mark.parametrize("browser", ["mobile"], indirect=True)
def test_github_mobile(browser: WebDriver):
    browser.get("https://github.com/")

    # Открываем бургер-меню
    menu_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[aria-label='Toggle navigation']")
        )
    )

    menu_button.click()

    # Кликаем Sign up
    sign_up = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[normalize-space()='Sign up']")
        )
    )

    sign_up.click()

    WebDriverWait(browser, 10).until(
        EC.url_contains("/signup")
    )

    assert "/signup" in browser.current_url