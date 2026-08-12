import pytest
from selenium import webdriver

# Сделал обычные фикстуры, которые импользуют только один набор данных
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



def test_github_desktop(desktop_browser):
    desktop_browser.get("https://github.com/")

    desktop_browser.find_element(
        "link text", "Sign in"
    ).click()


def test_github_mobile(mobile_browser):
    mobile_browser.get("https://github.com/")

    mobile_browser.find_element(
        "link text", "Sign in"
    ).click()