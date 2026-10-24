from selenium.webdriver.common.by import By


class LoginLocators:
    """
    Класс содержит локаторы для элементов страницы авторизации.
    """

    # Локаторы полей ввода
    LOGIN_FIELD = (
        By.XPATH,
        "//input[@name='name']"
    )
    """Локатор поля ввода логина."""

    PASSWORD_FIELD = (
        By.XPATH,
        "//input[@name='Пароль']"
    )
    """Локатор поля ввода пароля."""

    # Локаторы кнопок и ссылок
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Войти']"
    )
    """Локатор кнопки входа."""

    RESET_PASSWORD_LINK = (
        By.XPATH,
        "//a[text()='Восстановить пароль']"
    )
    """Локатор ссылки для восстановления пароля."""
