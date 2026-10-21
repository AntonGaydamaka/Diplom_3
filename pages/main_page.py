import allure
import utils.urls as urls

from locators.main_page_elements import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    """
    Класс для работы с главной страницей приложения.
    """

    @allure.step("Переход в личный кабинет")
    def click_personal_account_button(self):
        """
        Выполняет переход в личный кабинет и проверяет URL.

        :return: текущий URL после перехода
        """
        self.click_on_element(MainLocators.PERSONAL_ACCOUNT)
        self.wait_for_url(urls.ACCOUNT_URL)
        return self.get_current_url()

    @allure.step("Переход в конструктор бургеров")
    def click_constructor_button(self):
        """
        Выполняет переход в раздел конструктора бургеров.
        """
        self.click_on_element(MainLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Ожидание появления заголовка «Соберите бургер»")
    def wait_for_title_burger(self):
        """
        Ожидает появления заголовка конструктора бургеров.

        :return: True, если заголовок найден
        """
        return self.is_element_present(MainLocators.ASSEMBLE_BURGER_TITLE)

    @allure.step("Переход в ленту заказов")
    def click_order_feed_button(self):
        """
        Выполняет переход в ленту заказов и проверяет URL.

        :return: текущий URL после перехода
        """
        self.click_on_element(MainLocators.ORDER_FEED_BUTTON)
        self.wait_for_url(urls.FEED_URL)
        return self.get_current_url()

    @allure.step("Ожидание появления заголовка «Лента заказов»")
    def wait_for_title_order_feed(self):
        """
        Ожидает появления заголовка ленты заказов.

        :return: True, если заголовок найден
        """
        return self.is_element_present(MainLocators.ORDER_FEED_TITLE)

    @allure.step("Клик на ингредиент")
    def click_ingredient(self):
        """
        Выполняет клик по ингредиенту (булка).
        """
        self.click_on_element(MainLocators.BURGER_INGREDIENT_BUN)

    @allure.step("Ожидание появления всплывающего окна с ингредиентом")
    def wait_for_popup_ingredient_details_window(self):
        """
        Ожидает появления всплывающего окна с деталями ингредиента.

        :return: True, если окно найдено
        """
        return self.is_element_present(
            MainLocators.POPUP_INGREDIENT_DETAILS_WINDOW
            )

    @allure.step("Закрытие всплывающего окна ингредиента")
    def click_cross_in_popup_window(self):
        """
        Закрывает всплывающее окно с ингредиентом.
        """
        self.click_on_element(MainLocators.CLOSE_BUTTON)

    @allure.step("Проверка закрытия всплывающего окна ингредиента")
    def is_popup_window_closed(self):
        """
        Проверяет, что всплывающее окно ингредиента закрыто.

        :return: True, если окно отсутствует
        """
        return self.is_element_absent(
            MainLocators.POPUP_INGREDIENT_DETAILS_WINDOW
            )

    @allure.step("Добавление ингредиента (булка) в заказ")
    def drag_and_drop_ingredient_bun(self):
        """
        Перетаскивает ингредиент (булка) в корзину конструктора.
        """
        return self.drag_and_drop_on_to_element(
            MainLocators.BURGER_INGREDIENT_BUN,
            MainLocators.BURGER_CONSTRUCTOR_BASKET
        )

    @allure.step("Проверка количества ингредиента в корзине")
    def check_counter_num(self):
        """
        Получает количество ингредиента из счетчика.

        :return: текст счетчика
        """
        return self.get_text_from_element(MainLocators.COUNTER_BUN)

    @allure.step("Добавление ингредиента (соус) в заказ")
    def drag_and_drop_ingredient_souses(self):
        """
        Перетаскивает ингредиент (соус) в корзину конструктора.
        """
        return self.drag_and_drop_on_to_element(
            MainLocators.BURGER_INGREDIENT_SOUSES,
            MainLocators.BURGER_CONSTRUCTOR_BASKET
        )

    @allure.step("Клик на кнопку «Оформить заказ»")
    def click_place_order_button(self):
        """
        Выполняет клик по кнопке оформления заказа.
        """
        self.click_on_element(MainLocators.ORDER_BUTTON)

    @allure.step("Ожидание появления всплывающего окна с заказом")
    def wait_for_popup_order_id_window(self):
        """
        Ожидает появления всплывающего окна с ID заказа.

        :return: True, если окно найдено
        """
        return self.is_element_present(MainLocators.POPUP_ORDER_ID_WINDOW)

    @allure.step("Получение ID заказа из всплывающего окна")
    def get_order_id_from_popup(self):
        """
        Получает ID заказа из всплывающего окна.

        :return: ID заказа
        """
        self.wait_for_text_to_change(
            MainLocators.ORDER_ID_TITLE,
            initial_text="9999",
            timeout=10
        )
        element = self.find_element_with_wait(MainLocators.ORDER_ID_TITLE)
        order_id = element.text
        return order_id

    @allure.step("Создание заказа")
    def create_order(self):
        """
        Выполняет полный процесс создания заказа:
        1. Добавляет ингредиенты
        2. Оформляет заказ
        3. Получает ID заказа
        4. Закрывает всплывающее окно
        """
        self.drag_and_drop_ingredient_bun()
        self.drag_and_drop_ingredient_souses()
        self.click_place_order_button()
        order_id = self.get_order_id_from_popup()
        self.click_cross_in_popup_window()
        return order_id
