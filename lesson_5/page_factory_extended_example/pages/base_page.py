from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumpagefactory.Pagefactory import PageFactory


class BasePage(PageFactory):
    """
    Базовый класс всех страниц проекта.

    Содержит общие методы работы с браузером,
    ожиданиями и JavaScript.
    """

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(driver, self.timeout)

    # ======================================================
    # Работа с браузером
    # ======================================================

    def open(self, url):
        """Открыть страницу."""
        self.driver.get(url)

    def refresh(self):
        """Обновить страницу."""
        self.driver.refresh()

    def back(self):
        """Вернуться назад."""
        self.driver.back()

    def forward(self):
        """Перейти вперед."""
        self.driver.forward()

    def get_title(self):
        """Получить заголовок страницы."""
        return self.driver.title

    def get_current_url(self):
        """Получить текущий URL."""
        return self.driver.current_url

    # ======================================================
    # JavaScript
    # ======================================================

    def scroll_to_element(self, element):
        """Прокрутить страницу к элементу."""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

    def js_click(self, element):
        """Клик через JavaScript."""
        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # ======================================================
    # Ожидания
    # ======================================================

    def wait_visibility(self, locator):
        """Ожидать появления элемента."""
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator):
        """Ожидать кликабельности элемента."""
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def wait_invisible(self, locator):
        """Ожидать исчезновения элемента."""
        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    # ======================================================
    # Проверки
    # ======================================================

    def is_title_contains(self, text):
        """Проверить, что текст содержится в title."""
        return text in self.driver.title

    def is_url_contains(self, text):
        """Проверить, что текст содержится в URL."""
        return text in self.driver.current_url

    # ======================================================
    # Работа с окнами
    # ======================================================

    def switch_to_last_tab(self):
        """Переключиться на последнюю вкладку."""
        self.driver.switch_to.window(
            self.driver.window_handles[-1]
        )

    def switch_to_first_tab(self):
        """Переключиться на первую вкладку."""
        self.driver.switch_to.window(
            self.driver.window_handles[0]
        )

    # ======================================================
    # Работа с Alert
    # ======================================================

    def accept_alert(self):
        """Подтвердить alert."""
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """Закрыть alert."""
        self.driver.switch_to.alert.dismiss()

    def get_alert_text(self):
        """Получить текст alert."""
        return self.driver.switch_to.alert.text