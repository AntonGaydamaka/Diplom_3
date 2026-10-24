import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from pages.account_page import AccountPage
from pages.feed_page import FeedPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage
from utils.user_operations import register_new_user, delete_new_user

from utils.urls import (
    MAIN_URL,
    ACCOUNT_URL,
    LOGIN_URL,
    FORGOT_PASSWORD_URL,
    RESET_PASSWORD_URL,
    FEED_URL
)


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    """
    Фикстура для инициализации веб-драйвера
    """
    if request.param == 'firefox':
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)

    # Установка размера окна браузера
    driver.set_window_size(1920, 1080)
    yield driver
    # Закрытие драйвера после выполнения теста
    driver.quit()


@pytest.fixture()
def main_page(driver):
    """
    Фикстура для работы с главной страницей
    """
    page = MainPage(driver)
    page.get_url(MAIN_URL)
    return page


@pytest.fixture()
def account_page(driver):
    """
    Фикстура для работы со страницей личного кабинета
    """
    page = AccountPage(driver)
    page.get_url(ACCOUNT_URL)
    return page


@pytest.fixture()
def login_page(driver):
    """
    Фикстура для работы со страницей авторизации
    """
    page = LoginPage(driver)
    page.get_url(LOGIN_URL)
    return page


@pytest.fixture()
def forgot_password_page(driver):
    """
    Фикстура для работы со страницей восстановления пароля
    """
    page = ForgotPasswordPage(driver)
    page.get_url(FORGOT_PASSWORD_URL)
    return page


@pytest.fixture()
def reset_password_page(driver):
    """
    Фикстура для работы со страницей сброса пароля
    """
    page = ResetPasswordPage(driver)
    page.get_url(RESET_PASSWORD_URL)
    return page


@pytest.fixture()
def feed_page(driver):
    """
    Фикстура для работы со страницей ленты заказов
    """
    page = FeedPage(driver)
    page.get_url(FEED_URL)
    return page


@pytest.fixture()
def order_id(main_page, login_in):
    """
    Фикстура для создания заказа и получения его ID
    """
    # Создание заказа
    main_page.drag_and_drop_ingredient_bun()
    main_page.drag_and_drop_ingredient_souses()
    main_page.click_place_order_button()

    # Получение ID заказа
    order_id = main_page.get_order_id_from_popup()
    main_page.click_cross_in_popup_window()
    return order_id


@pytest.fixture
def login():
    """
    Фикстура для регистрации нового пользователя
    """
    # Регистрация пользователя
    user_data, response = register_new_user()
    yield user_data

    # Удаление пользователя после выполнения теста
    access_token = user_data.get('access_token')
    delete_new_user(access_token)


@pytest.fixture
def login_in(login, login_page):
    """
    Фикстура для авторизации пользователя
    """
    email = login['email']
    password = login['password']

    # Процесс авторизации
    login_page.set_email(email)
    login_page.set_password(password)
    login_page.click_login_button()
