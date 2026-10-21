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

    # Локаторы элементов ленты заказов
    ORDER_FEED_ITEM_BY_ID = (
        By.XPATH,
        "//p[contains(@class, 'text_type_digits-default') "
        "and contains(text(), '{order_id}')]"
    )
    """Элемент заказа в ленте заказов по ID."""

    ORDER_ID_IN_HISTORY = (
        By.XPATH,
        "//p[contains(@class, 'text_type_digits-default') "
        "and text()='#0{order_id}']"
    )
    """Локатор для поиска конкретного ID заказа в истории заказов."""

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
