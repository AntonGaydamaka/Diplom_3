import allure
import utils.urls as urls

from locators.login_page_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Класс для работы со страницей авторизации.
    """

    @allure.step("Переход по ссылке «Восстановить пароль»")
    def click_reset_password_link(self):
        """
        Выполняет переход по ссылке восстановления пароля и проверяет URL.

        :return: текущий URL после перехода
        """
        self.click_on_element(LoginLocators.RESET_PASSWORD_LINK)
        self.wait_for_url(urls.FORGOT_PASSWORD_URL)
        return self.get_current_url()

    @allure.step("Заполнение поля «Email»")
    def set_email(self, login):
        """
        Заполняет поле электронной почты.

        :param login: адрес электронной почты для авторизации
        """
        email_field = self.find_element_with_wait(LoginLocators.LOGIN_FIELD)
        email_field.clear()
        email_field.send_keys(login)

    @allure.step("Заполнение поля «Пароль»")
    def set_password(self, password):
        """
        Заполняет поле пароля.

        :param password: пароль для авторизации
        """
        password_field = self.find_element_with_wait(
            LoginLocators.PASSWORD_FIELD
            )
        password_field.clear()
        password_field.send_keys(password)

    @allure.step("Клик на кнопку «Войти»")
    def click_login_button(self):
        """
        Выполняет клик по кнопке входа и проверяет переход на главную страницу.

        :return: текущий URL после перехода
        """
        self.click_on_element(LoginLocators.LOGIN_BUTTON)
        self.wait_for_url(urls.MAIN_URL)
        return self.get_current_url()
