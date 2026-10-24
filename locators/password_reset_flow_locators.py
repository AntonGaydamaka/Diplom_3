from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    """
    Класс содержит локаторы для элементов страницы восстановления пароля.
    """

    EMAIL_FIELD = (
        By.XPATH,
        "//input[@name='name']"
    )
    """Поле ввода электронной почты."""

    RESET_BUTTON = (
        By.XPATH,
        "//button[text()='Восстановить']"
    )
    """Кнопка отправки запроса на восстановление пароля."""


class ResetPasswordLocators:
    """
    Класс содержит локаторы для элементов страницы сброса пароля.
    """

    PASSWORD_INPUT_BEFORE = (
        By.CSS_SELECTOR,
        "div.input.input_type_password"
    )
    """Поле ввода пароля до активации (скрытый режим)."""

    PASSWORD_INPUT_AFTER = (
        By.CSS_SELECTOR,
        "div.input.input_type_text.input_status_active"
    )
    """Поле ввода пароля после активации (открытый режим)."""

    TOGGLE_PASSWORD_BUTTON = (
        By.CSS_SELECTOR,
        "div.input__icon.input__icon-action"
    )
    """Кнопка переключения видимости пароля."""
