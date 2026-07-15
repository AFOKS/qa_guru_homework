import pytest
import time
def test_empty_form_submission(driver):
    page = TextBoxPage(driver).open()

    page.submit()

    assert not page.is_output_visible(), (
        "Результат не должен отображаться при отправке пустой формы"
    )
    assert page.is_name_invalid(), (
        "Поле Name должно быть помечено как обязательное"
    )
    assert page.is_email_invalid(), (
        "Поле Email должно быть помечено как обязательное"
    )
