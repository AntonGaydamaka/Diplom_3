import allure

from locators.password_reset_flow_locators import ResetPasswordLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    """
    Класс для работы со страницей сброса пароля.
    """

    @allure.step("Переключение видимости пароля")
    def toggle_password_visibility(self):
        """
        Выполняет переключение видимости пароля (показать/скрыть).
        """
        self.click_on_element(ResetPasswordLocators.TOGGLE_PASSWORD_BUTTON)

    @allure.step("Ожидание появления поля ввода пароля")
    def wait_for_password_input(self):
        """
        Ожидает появления поля ввода пароля.

        :return: True, если поле найдено
        """
        return self.is_element_present(
            ResetPasswordLocators.PASSWORD_INPUT_BEFORE
            )

    @allure.step("Проверка активности поля ввода пароля")
    def is_password_field_active(self):
        """
        Проверяет, что поле ввода пароля активно и доступно для ввода.

        :return: True, если поле активно
        """
        return self.is_element_present(
            ResetPasswordLocators.PASSWORD_INPUT_AFTER
            )
