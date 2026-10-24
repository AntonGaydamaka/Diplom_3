import allure
import utils.urls as urls

from locators.password_reset_flow_locators import ForgotPasswordLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    """
    Класс для работы со страницей восстановления пароля.
    """

    @allure.step("Заполнение поля email")
    def fill_email_link(self, email):
        """
        Заполняет поле ввода email указанным значением.

        :param email: адрес электронной почты для восстановления
        """
        email_field = self.find_element_with_wait(
            ForgotPasswordLocators.EMAIL_FIELD
        )
        email_field.clear()  # Очищаем поле перед вводом
        email_field.send_keys(email)

    @allure.step("Клик на кнопку 'Восстановить'")
    def click_reset_button(self):
        """
        Выполняет клик по кнопке восстановления пароля и проверяет переход.

        :return: текущий URL после перехода
        """
        self.click_on_element(ForgotPasswordLocators.RESET_BUTTON)
        self.wait_for_url(urls.RESET_PASSWORD_URL)
        return self.get_current_url()
