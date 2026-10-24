from selenium.webdriver.common.by import By


class MainLocators:
    """
    Класс содержит локаторы для элементов главной страницы приложения.
    """

    # Локаторы кнопок авторизации
    LOGIN_TO_ACCOUNT_BUTTON = (
        By.XPATH,
        "//button[text()='Войти в аккаунт']"
    )
    """Кнопка входа в аккаунт."""

    # Локаторы кнопок и заголовков конструктора
    ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Оформить заказ']"
    )
    """Кнопка оформления заказа."""

    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[text()='Конструктор']"
    )
    """Кнопка перехода в конструктор."""

    ASSEMBLE_BURGER_TITLE = (
        By.XPATH,
        "//h1[text()='Соберите бургер']"
    )
    """Заголовок страницы конструктора бургеров."""

    # Локаторы элементов личного кабинета
    PERSONAL_ACCOUNT = (
        By.XPATH,
        "//p[text()='Личный Кабинет']"
    )
    """Элемент личного кабинета."""

    # Локаторы элементов ленты заказов
    ORDER_FEED_BUTTON = (
        By.XPATH,
        "//p[text()='Лента Заказов']"
    )
    """Кнопка перехода в ленту заказов."""

    ORDER_FEED_TITLE = (
        By.XPATH,
        "//h1[text()='Лента Заказов']"
    )
    """Заголовок ленты заказов."""

    # Локаторы ингредиентов бургера
    BURGER_INGREDIENT_BUN = (
        By.XPATH,
        "//img[@alt='Флюоресцентная булка R2-D3']"
    )
    """Ингредиент - булка."""

    BURGER_INGREDIENT_SOUSES = (
        By.XPATH,
        "//img[@alt='Соус Spicy-X']"
    )
    """Ингредиент - соус."""

    # Локаторы всплывающих окон
    POPUP_INGREDIENT_DETAILS_WINDOW = (
        By.CLASS_NAME,
        "Modal_modal__container__Wo2l_"
    )
    """Всплывающее окно с деталями ингредиента."""

    CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Modal_modal__close')]"
    )
    """Кнопка закрытия всплывающего окна."""

    # Локаторы элементов корзины
    BURGER_CONSTRUCTOR_BASKET = (
        By.XPATH,
        "//ul[contains(@class, 'BurgerConstructor_basket__list')]"
    )
    """Корзина конструктора бургеров."""

    COUNTER_BUN = (
        By.CSS_SELECTOR,
        "[class='counter_counter__num__3nue1']"
    )
    """Счетчик количества булочек."""

    # Локаторы окна подтверждения заказа
    POPUP_ORDER_ID_WINDOW = (
        By.CLASS_NAME,
        "Modal_modal__container__Wo2l_"
    )
    """Всплывающее окно с ID заказа."""

    ORDER_ID_TITLE = (
        By.CSS_SELECTOR,
        "h2.Modal_modal__title_shadow__3ikwq.text_type_digits-large"
    )
    """Заголовок с ID заказа."""
