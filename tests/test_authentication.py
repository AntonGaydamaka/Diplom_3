import allure
import utils.urls as urls


class TestLoginPage:
    """
    Тест-кейсы для страницы авторизации
    """

    @allure.feature('Навигация между страницами')
    @allure.story('Переход на страницу восстановления пароля')
    @allure.title(
        'Тест перехода на первую страницу восстановления '
        'пароля по клику на «Восстановить пароль»')
    def test_switch_to_forgot_password(self, login_page):
        """
        Проверяет корректность перехода на страницу восстановления пароля
        """
        current_url = login_page.click_reset_password_link()
        assert current_url == urls.FORGOT_PASSWORD_URL, (
            f"Ожидался URL {urls.FORGOT_PASSWORD_URL}, но был {current_url}"
        )


class TestForgotPasswordPage:
    """
    Тест-кейсы для страницы восстановления пароля
    """

    @allure.feature('Навигация между страницами')
    @allure.story('Переход на страницу сброса пароля')
    @allure.title('Тест перехода на вторую страницу '
                  'восстановления пароля после отправки email')
    def test_switch_to_reset_password(self, forgot_password_page):
        """
        Проверяет корректность перехода на страницу сброса пароля
        """
        email = 'email@mail.ru'
        forgot_password_page.fill_email_link(email)
        current_url = forgot_password_page.click_reset_button()
        assert current_url == urls.RESET_PASSWORD_URL, (
            f"Ожидался URL {urls.RESET_PASSWORD_URL}, но был {current_url}"
        )


class TestResetPasswordPage:
    """
    Тест-кейсы для страницы сброса пароля
    """

    @allure.feature('Функционал полей ввода')
    @allure.story('Работа кнопки «Показать/Скрыть пароль»')
    @allure.title(
        'Тест активации поля ввода пароля'
        'после нажатия кнопки «Показать/Скрыть»')
    def test_password_toggle_functionality(
        self, forgot_password_page, reset_password_page
    ):
        """
        Проверяет работу кнопки переключения видимости пароля
        """
        email = 'mail@mail.ru'
        # Выполняем последовательность действий для
        # перехода на страницу сброса пароля
        forgot_password_page.fill_email_link(email)
        forgot_password_page.click_reset_button()
        reset_password_page.wait_for_password_input()

        # Проверяем работу кнопки переключения
        reset_password_page.toggle_password_visibility()
        assert reset_password_page.is_password_field_active(), (
            "Поле ввода пароля не стало активным после нажатия на кнопку"
        )
