from selenium.webdriver.common.by import By


class FeedLocators:
    """
    Класс содержит локаторы для элементов страницы «Лента заказов».
    """

    # Локаторы элементов управления
    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[text()='Конструктор']"
    )
    """Кнопка перехода в конструктор в хеддере."""

    PERSONAL_ACCOUNT = (
        By.XPATH,
        "//p[text()='Личный Кабинет']"
    )
    """Элемент личного кабинета."""

    # Локаторы всплывающих окон
    POPUP_ORDER_DETAILS_WINDOW = (
        By.CLASS_NAME,
        "Modal_modal__container__Wo2l_"
    )
    """Всплывающее окно с деталями заказа."""

    # Локаторы списка заказов
    ORDER_READY_LIST = (
        By.CSS_SELECTOR,
        ".OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi"
    )
    """Список заказов 'В работе'."""

    ORDER_READY_ID = (
        By.CSS_SELECTOR,
        ".OrderFeed_orderListReady__1YFem .text_type_digits-default"
    )
    """ID заказа в списке 'В работе'."""

    # Локаторы счётчиков
    ORDER_COUNTER_ALL_TIME = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']"
        "/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    )
    """Счётчик выполненных заказов за всё время."""

    ORDER_COUNTER_TODAY = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']"
        "/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    )
    """Счётчик выполненных заказов за сегодня."""

    # Локаторы истории заказов
    LAST_ORDER_IN_HISTORY = (
        By.XPATH,
        "(//p[contains(@class, 'text_type_digits-default')])[last()]"
    )
    """Последний выполненный заказ в истории заказов."""

    # Динамические локаторы (методы, возвращающие готовый tuple локатора)
    @staticmethod
    def order_feed_item_by_id(order_id):
        """
        Возвращает локатор элемента заказа в ленте заказов по его ID.

        :param order_id: ID заказа
        :return: tuple с типом и значением локатора
        """
        return (
            By.XPATH,
            "//p[contains(@class, 'text_type_digits-default') "
            f"and contains(text(), '{order_id}')]"
        )

    @staticmethod
    def order_id_in_history(order_id):
        """
        Возвращает локатор элемента заказа в истории заказов по его ID.

        :param order_id: ID заказа
        :return: tuple с типом и значением локатора
        """
        return (
            By.XPATH,
            "//p[contains(@class, 'text_type_digits-default') "
            f"and text()='#0{order_id}']"
        )