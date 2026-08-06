import allure

@allure.epic("Интернет-магазин")
@allure.feature("Авторизация")
class TestLogin:

    @allure.story("Успешный вход")
    @allure.title("Пользователь входит в систему")
    def test_login(self, user):

        with allure.step("Открываем страницу"):

            print("Открыли страницу авторизации")

        with allure.step("Вводим логин"):

            print(user["login"])

        with allure.step("Вводим пароль"):

            print(user["password"])

        with allure.step("Нажимаем кнопку Войти"):

            print("Пользователь вошел")

        assert True