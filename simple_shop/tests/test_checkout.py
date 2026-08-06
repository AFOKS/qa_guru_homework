import pytest
import allure

@allure.feature("Оформление заказа")
class TestCheckout:

    def test_create_order(self):

        with allure.step("Создаем заказ"):

            print("Заказ создан")

        allure.attach(
            "ORDER-12345",
            name="Номер заказа",
            attachment_type=allure.attachment_type.TEXT
        )

        assert True


    @pytest.mark.skip(reason="Оплата еще не реализована")
    def test_payment(self):

        pass