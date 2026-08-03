from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class AutomationPracticeFormPage(BasePage):

    def open_url(self, url):
        self.driver.get(url)
        return self
    """
    Класс страницы формы. Демонстрирует декларативное описание локаторов
    и инкапсуляцию сложного взаимодействия с веб-элементами.
    """

    def __init__(self, driver):
        super().__init__(driver)


    locators = {
        'first_name': ('ID', 'firstName'),
        'last_name': ('ID', 'lastName'),
        'user_email': ('ID', 'userEmail'),

        'banner_button': ('XPATH', "//div[@id='fixedban']//button[@aria-label='Close']"),

        # Радиокнопки выбора пола (локаторы на кликабельные label)
        'gender_male': ('XPATH', "//label[@for='gender-radio-1']"),
        'gender_female': ('XPATH', "//label[@for='gender-radio-2']"),
        'gender_other': ('XPATH', "//label[@for='gender-radio-3']"),

        'user_number': ('ID', 'userNumber'),

        # Компоненты виджета календаря (DatePicker)
        'date_of_birth_input': ('ID', 'dateOfBirthInput'),
        'calendar_month_select': ('CLASS_NAME', 'react-datepicker__month-select'),
        'calendar_year_select': ('CLASS_NAME', 'react-datepicker__year-select'),
        # Динамический локатор для выбора конкретного дня (использует параметризацию через XPATH)
        'calendar_target_day': ('XPATH',"//span[contains(@class,'react-datepicker__day') and text()='{day}']"),

        # Поле автодополнения (кастомный выпадающий список)
        'subjects_input': ('ID', 'subjectsInput'),
        'subjects_auto_complete_option': ('XPATH', "//div[contains(@class, 'subjects-auto-complete__option')]"),

        # Чекбоксы хобби (локаторы на кликабельные label)
        'hobby_sports': ('XPATH', "//label[@for='hobbies-checkbox-1']"),
        'hobby_reading': ('XPATH', "//label[@for='hobbies-checkbox-2']"),
        'hobby_music': ('XPATH', "//label[@for='hobbies-checkbox-3']"),

        # Загрузка файлов и адресный блок
        'upload_picture_btn': ('ID', 'uploadPicture'),
        'current_address': ('ID', 'currentAddress'),

        # Кастомные выпадающие списки (React-Select) штата и города
        'state_dropdown': ('ID', 'state'),
        'state_input': ('XPATH', "//div[@id='state']//input"),
        'city_dropdown': ('ID', 'city'),
        'city_input': ('XPATH', "//div[@id='city']//input"),

        'submit_button': ('ID', 'submit'),

        # Модальное окно подтверждения результатов отправки
        'modal_title': ('ID', 'example-modal-sizes-title-lg'),
        'modal_table_rows': ('XPATH', "//tbody/tr")
    }

    def _close_commercial_banner(self):
        self.banner_button.click()

    # --------------------------------------------------------------------------
    # Бизнес-методы (Действия на странице)
    # --------------------------------------------------------------------------
    def fill_personal_info(self, first_name: str, last_name: str, email: str, gender: str, mobile: str):
        """Заполнение основных персональных данных и выбор радиокнопок."""

        self._close_commercial_banner()

        self.first_name.set_text(first_name)
        self.last_name.set_text(last_name)
        self.user_email.set_text(email)

        # Выбор радиокнопки на основе переданного текста
        if gender.lower() == 'male':
            self.gender_male.click_button()
        elif gender.lower() == 'female':
            self.gender_female.click_button()
        else:
            self.gender_other.click_button()

        self.user_number.set_text(mobile)

    def select_date_of_birth(self, year: str, month: str, day: str):
        """Работа со сложным виджетом календаря (React DatePicker)."""
        self.date_of_birth_input.click_button()

        # Выбор из стандартных HTML-селектов внутри виджета
        self.calendar_year_select.select_element_by_value(year)
        self.calendar_month_select.select_element_by_text(month)

        print("Year:", self.calendar_year_select.get_attribute("value"))
        print("Month:", self.calendar_month_select.get_attribute("value"))


        # Динамическая замена плейсхолдера в XPATH для выбора дня
        xpath_tuple = self.locators['calendar_target_day']
        dynamic_xpath = xpath_tuple[1].format(day=day)

        # Поиск и клик по динамически сформированному локатору дня
        day_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    self.TYPE_OF_LOCATORS[xpath_tuple[0].lower()],
                    dynamic_xpath
                )
            )
        )

        day_element.click()

    def enter_subjects(self, subjects: list):
        """Работа с полем ввода, поддерживающим автодополнение (React-Select)."""
        for subject in subjects:
            self.subjects_input.set_text(subject)
            # Ожидание появления подсказки и нажатие Enter/клик для фиксации элемента
            self.subjects_input.send_keys(Keys.ENTER)

    def select_hobbies(self, hobbies: list):
        """Выбор нескольких чекбоксов."""
        hobbies_map = {
            'sports': self.hobby_sports,
            'reading': self.hobby_reading,
            'music': self.hobby_music
        }
        for hobby in hobbies:
            hobby_lower = hobby.lower()
            if hobby_lower in hobbies_map:
                print(hobbies_map[hobby_lower])
                hobbies_map[hobby_lower].click_button()

    def upload_file(self, file_path: str):
        """Загрузка файла через прямую передачу абсолютного пути в input[type='file']."""
        # По правилам Selenium, для загрузки файлов используется отправка текста (пути к файлу)
        self.upload_picture_btn.send_keys(file_path)

    def fill_address_and_location(self, address: str, state: str, city: str):
        """Заполнение адреса и работа со сложными кастомными выпадающими списками."""
        self.current_address.set_text(address)

        # Для кастомных выпадающих списков React-Select: скроллим, вводим текст и нажимаем ENTER
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.state_dropdown)
        self.state_input.send_keys(state)
        self.state_input.send_keys(Keys.ENTER)

        self.city_input.send_keys(city)
        self.city_input.send_keys(Keys.ENTER)

    def submit_form(self):
        """Финальная отправка формы кликом по кнопке Submit через JavaScript (защита от перекрытия футером)."""
        self.driver.execute_script("arguments[0].click();", self.submit_button)

    def get_modal_results(self) -> dict:
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "example-modal-sizes-title-lg")
            )
        )

        locator_type, locator_value = self.locators["modal_table_rows"]

        rows = self.driver.find_elements(
            self.TYPE_OF_LOCATORS[locator_type.lower()],
            locator_value
        )

        result_data = {}

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")

            if len(cells) == 2:
                result_data[cells[0].text.strip()] = cells[1].text.strip()

        return result_data