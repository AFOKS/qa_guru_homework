import pytest
from selenium import webdriver


@pytest.fixture(
    params=[
        (1920, 1080),
        (390, 844),
    ]
)
def browser(request):
    driver = webdriver.Chrome()

    width, height = request.param
    driver.set_window_size(width, height)

    yield driver

    driver.quit()


def test_github_desktop(browser):
    width = browser.get_window_size()["width"]

    if width < 1000:
        pytest.skip("Пропускаем desktop-тест для мобильного разрешения")

    browser.get("https://github.com/")

    assert width >= 1000


def test_github_mobile(browser):
    width = browser.get_window_size()["width"]

    if width >= 1000:
        pytest.skip("Пропускаем mobile-тест для desktop-разрешения")

    browser.get("https://github.com/")

    assert width < 1000