import allure
import utils.urls as urls

from locators.order_feed_locators import FeedLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FeedPage(BasePage):
    """
    Класс для работы со страницей ленты заказов.
    """

    @allure.step("Клик на кнопку «Конструктор»")
    def click_constructor_button(self):
        """
        Выполняет клик по кнопке конструктора.
        """
        self.click_on_element(FeedLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Поиск заказа в ленте заказов "
                 "по ID {order_id} и клик по нему")
    def find_and_click_order_by_id(self, order_id):
        """
        Находит и кликает по заказу по его ID.

        :param order_id: ID заказа для поиска
        """
        locator = (
            By.XPATH,
            FeedLocators.ORDER_FEED_ITEM_BY_ID[1].format(order_id=order_id)
        )
        return self.click_on_element(locator)

    @allure.step("Дождаться появления всплывающего окна с деталями заказа")
    def wait_for_popup_order_details_window(self):
        """
        Ожидает появления окна с деталями заказа.
        """
        return self.is_element_present(FeedLocators.POPUP_ORDER_DETAILS_WINDOW)

    @allure.step("Ожидание появления ID "
                 "заказа '{expected_order_id}' в разделе 'В работе'")
    def wait_for_order_id_in_ready_list(self, expected_order_id):
        """
        Ожидает появления указанного ID заказа в списке 'В работе'.

        :param expected_order_id: ожидаемый ID заказа
        """
        self.wait_for_text_to_be(
            locator=FeedLocators.ORDER_READY_ID,
            expected_text=f'0{expected_order_id}',
            timeout=10
        )

    @allure.step("Получение ID заказа из раздела 'В работе'")
    def get_order_id_from_list_ready(self):
        """
        Получает ID заказа из списка 'В работе'.

        :return: ID заказа
        """
        element = self.find_element_with_wait(FeedLocators.ORDER_READY_ID)
        order_id = element.text.strip()
        return order_id

    @allure.step(
            "Зафиксировать количество заказов "
            "в разделе 'Выполнено за все время'"
            )
    def get_number_orders_all_time(self):
        """
        Получает количество заказов за все время.

        :return: количество заказов
        """
        self.wait_for_text_to_change(
            locator=FeedLocators.ORDER_COUNTER_ALL_TIME,
            initial_text=None,
            timeout=10
        )
        order_counter_text = self.get_text_from_element(
            FeedLocators.ORDER_COUNTER_ALL_TIME
        )
        return int(order_counter_text)

    @allure.step(
            "Зафиксировать количество заказов "
            "в разделе 'Выполнено за сегодня'"
            )
    def get_number_orders_today(self):
        """
        Получает количество заказов за сегодня.

        :return: количество заказов
        """
        self.wait_for_text_to_change(
            locator=FeedLocators.ORDER_COUNTER_TODAY,
            initial_text=None,
            timeout=10
        )
        order_counter_text = self.get_text_from_element(
            FeedLocators.ORDER_COUNTER_TODAY
        )
        return int(order_counter_text)

    @allure.step("Поиск заказа по ID {order_id}")
    def find_order_by_id(self, order_id):
        """
        Ищет заказ по его ID в истории.

        :param order_id: ID заказа для поиска
        :return: текст найденного элемента
        """
        locator = (
            FeedLocators.ORDER_ID_IN_HISTORY[0],
            FeedLocators.ORDER_ID_IN_HISTORY[1].format(order_id=order_id)
        )
        element = self.find_element_with_wait(locator)
        assert element, f"Заказ с ID {order_id} не найден"
        return element.text

    @allure.step("Cкролл до созданного заказа в истории заказов")
    def scroll_order_in_history(self):
        """
        Выполняет скролл до последнего заказа в истории.
        """
        self.scroll_into_view(FeedLocators.LAST_ORDER_IN_HISTORY)

    @allure.step("Переход в личный кабинет")
    def click_personal_account_button(self):
        """
        Выполняет переход в личный кабинет и проверяет URL.

        :return: текущий URL после перехода
        """
        self.click_on_element(FeedLocators.PERSONAL_ACCOUNT)
        self.wait_for_url(urls.ACCOUNT_URL)
        return self.get_current_url()
