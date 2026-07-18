from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class RegistrationPage(BasePage):

    URL = "https://qa-guru.github.io/one-page-form/automation-practice-form.html"

    # -------------------- Locators --------------------

    locators = {
        "first_name": ("ID", "firstName"),
        "last_name": ("ID", "lastName"),
        "user_email": ("ID", "userEmail"),
        "gender_male": ("CSS", "label[for='gender-radio-1']"),
        "gender_female": ("CSS", "label[for='gender-radio-2']"),
        "gender_other": ("CSS", "label[for='gender-radio-3']"),
        "user_number": ("ID", "userNumber"),

        "date_of_birth_input": ("ID", "dateOfBirthInput"),
        "calendar_month_select": ("CLASS_NAME", "react-datepicker__month-select"),
        "calendar_year_select": ("CLASS_NAME", "react-datepicker__year-select"),

        "subjects_input": ("ID", "subjectsInput"),

        "hobby_sports": ("CSS", "label[for='hobbies-checkbox-1']"),
        "hobby_reading": ("CSS", "label[for='hobbies-checkbox-2']"),
        "hobby_music": ("CSS", "label[for='hobbies-checkbox-3']"),

        "upload_picture_btn": ("ID", "uploadPicture"),

        "current_address": ("ID", "currentAddress"),

        "state_input": ("ID", "react-select-3-input"),
        "city_input": ("ID", "react-select-4-input"),

        "submit_button": ("ID", "submit"),

        "modal_title": ("ID", "example-modal-sizes-title-lg"),
        "close_modal": ("ID", "closeLargeModal")
    }

    # --------------------------------------------------

    def open(self):
        self.driver.get(self.URL)

    # --------------------------------------------------

    def close_banner(self):
        """
        Иногда рекламный баннер перекрывает кнопку Submit.
        """

        try:
            banner = self.driver.find_element(By.ID, "fixedban")
            self.driver.execute_script(
                "arguments[0].style.display='none';",
                banner
            )
        except:
            pass

    # --------------------------------------------------

    def fill_personal_info(
            self,
            first_name,
            last_name,
            email,
            gender,
            mobile
    ):

        self.first_name.clear_text()
        self.first_name.set_text(first_name)

        self.last_name.clear_text()
        self.last_name.set_text(last_name)

        self.user_email.clear_text()
        self.user_email.set_text(email)

        gender_map = {
            "Male": self.gender_male,
            "Female": self.gender_female,
            "Other": self.gender_other
        }

        gender_map[gender].click_button()

        self.user_number.clear_text()
        self.user_number.set_text(mobile)

    # --------------------------------------------------

    def select_date_of_birth(self, year, month, day):

        self.date_of_birth_input.click_button()

        self.calendar_year_select.select_element_by_value(year)

        self.calendar_month_select.select_element_by_text(month)

        self.driver.find_element(
            By.XPATH,
            f"//div[contains(@class,'react-datepicker__day') "
            f"and text()='{day}' "
            f"and not(contains(@class,'outside-month'))]"
        ).click()

    # --------------------------------------------------

    def enter_subjects(self, subjects):

        for subject in subjects:
            self.subjects_input.set_text(subject)
            self.subjects_input.send_keys(Keys.ENTER)

    # --------------------------------------------------

    def select_hobbies(self, hobbies):

        hobby_map = {
            "Sports": self.hobby_sports,
            "Reading": self.hobby_reading,
            "Music": self.hobby_music
        }

        for hobby in hobbies:
            hobby_map[hobby].click_button()

    # --------------------------------------------------

    def upload_file(self, file_path):

        self.upload_picture_btn.send_keys(file_path)

    # --------------------------------------------------

    def fill_address_and_location(
            self,
            address,
            state,
            city
    ):

        self.current_address.clear_text()
        self.current_address.set_text(address)

        self.state_input.send_keys(state)
        self.state_input.send_keys(Keys.ENTER)

        self.city_input.send_keys(city)
        self.city_input.send_keys(Keys.ENTER)

    # --------------------------------------------------

    def fill_form(
            self,
            first_name,
            last_name,
            email,
            gender,
            mobile,
            year,
            month,
            day,
            subjects,
            hobbies,
            file_path,
            address,
            state,
            city
    ):

        self.fill_personal_info(
            first_name,
            last_name,
            email,
            gender,
            mobile
        )

        self.select_date_of_birth(
            year,
            month,
            day
        )

        self.enter_subjects(subjects)

        self.select_hobbies(hobbies)

        self.upload_file(file_path)

        self.fill_address_and_location(
            address,
            state,
            city
        )

    # --------------------------------------------------

    def submit_form(self):

        self.close_banner()

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            self.submit_button
        )

        self.submit_button.click_button()

    # --------------------------------------------------

    def get_modal_title(self):

        return self.modal_title.get_text()

    # --------------------------------------------------

    def is_modal_open(self):

        return self.modal_title.is_displayed()

    # --------------------------------------------------

    def close_modal_window(self):

        self.close_modal.click_button()

    # --------------------------------------------------

    def get_modal_results(self):

        rows = self.driver.find_elements(
            By.XPATH,
            "//tbody/tr"
        )

        result = {}

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            result[cells[0].text] = cells[1].text

        return result

    # --------------------------------------------------

    def verify_results(self, expected):

        actual = self.get_modal_results()

        for field, value in expected.items():
            assert actual[field] == value, (
                f"{field}: "
                f"ожидалось '{value}', "
                f"получено '{actual[field]}'"
            )

    # --------------------------------------------------

    def reset_page(self):

        self.driver.refresh()

    # --------------------------------------------------

    def page_title(self):

        return self.driver.title

    # --------------------------------------------------

    def current_url(self):

        return self.driver.current_url

