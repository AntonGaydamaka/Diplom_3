import allure
import utils.urls as urls

from locators.user_profile_locators import AccountLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    """
    Класс для работы со страницей личного кабинета
    """

    @allure.step("Клик на «История заказов»")
    def click_order_history_link(self) -> str:
        """
        Метод для перехода в раздел истории заказов
        :return: текущий URL после перехода
        """
        self.click_on_element(AccountLocators.ORDER_HISTORY_LINK)
        self.wait_for_url(urls.ACCOUNT_ORDER_HISTORY_URL)
        return self.get_current_url()

    @allure.step("Клик на кнопку «Выход»")
    def click_exit_button(self) -> str:
        """
        Метод для выхода из аккаунта
        :return: текущий URL после выхода
        """
        self.click_on_element(AccountLocators.EXIT_BUTTON)
        self.wait_for_url(urls.LOGIN_URL)
        return self.get_current_url()
