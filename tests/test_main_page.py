import allure
import utils.urls as urls


class TestMainPage:
    """
    Тест-кейсы для проверки функционала главной страницы
    """

    @allure.feature('Навигация между страницами')
    @allure.story('Переход в личный кабинет')
    @allure.title(
        'Тест перехода в личный кабинет '
        'по клику на кнопку «Личный кабинет»')
    def test_switch_from_main_to_personal_account(self, main_page, login_in):
        """
        Проверяет корректность перехода в личный кабинет
        """
        current_url = main_page.click_personal_account_button()
        assert current_url == urls.ACCOUNT_URL, (
            f"Ожидался URL {urls.ACCOUNT_URL}, но был {current_url}"
        )

    @allure.feature('Навигация между страницами')
    @allure.story('Переход в конструктор бургеров')
    @allure.title('Тест перехода в конструктор '
                  'по клику на кнопку «Конструктор»')
    def test_switch_from_main_to_constructor(self, main_page, login_in):
        """
        Проверяет корректность перехода в конструктор бургеров
        """
        main_page.click_constructor_button()
        assert main_page.wait_for_title_burger(), (
            "Заголовок «Соберите бургер» не отобразился на экране"
        )

    @allure.feature('Навигация между страницами')
    @allure.story('Переход в ленту заказов')
    @allure.title('Тест перехода в ленту заказов '
                  'по клику на кнопку «Лента заказов»')
    def test_switch_from_main_to_order_feed(self, main_page, login_in):
        """
        Проверяет корректность перехода в ленту заказов
        """
        current_url = main_page.click_order_feed_button()
        assert (
            current_url == urls.FEED_URL
            and main_page.wait_for_title_order_feed
        ), f"Ожидался URL {urls.FEED_URL}, но был {current_url}"

    @allure.feature('Функционал сборки заказа')
    @allure.story('Работа с всплывающим окном ингредиента')
    @allure.title('Тест открытия всплывающего окна с деталями ингредиента')
    def test_open_popup_window_with_ingredient_details(
        self,
        main_page,
        login_in
    ):
        """
        Проверяет открытие всплывающего окна при клике на ингредиент
        """
        main_page.click_ingredient()
        assert main_page.wait_for_popup_ingredient_details_window(), (
            "Не открылось всплывающее окно с деталями"
        )

    @allure.feature('Функционал сборки заказа')
    @allure.story('Закрытие всплывающего окна ингредиента')
    @allure.title('Тест закрытия всплывающего окна с деталями ингредиента')
    def test_close_popup_window_with_ingredient_details(
        self,
        main_page,
        login_in
    ):
        """
        Проверяет корректное закрытие всплывающего окна
        """
        main_page.click_ingredient()
        main_page.wait_for_popup_ingredient_details_window()
        main_page.click_cross_in_popup_window()
        assert main_page.is_popup_window_closed(), (
            "Всплывающее окно не закрылось после клика по крестику"
        )

    @allure.feature('Функционал сборки заказа')
    @allure.story('Работа счетчика ингредиентов')
    @allure.title('Тест проверки увеличения счетчика '
                  'при добавлении ингредиента')
    def test_add_ingredient_to_order(self, main_page, login_in):
        """
        Проверяет корректность работы счетчика ингредиентов
        """
        main_page.drag_and_drop_ingredient_bun()
        counter_value = main_page.check_counter_num()
        assert counter_value == '2', (
            f"Неверное значение счетчика: "
            f"ожидалось '2', получено {counter_value}"
        )

    @allure.feature('Функционал оформления заказа')
    @allure.story('Оформление заказа авторизованным пользователем')
    @allure.title('Тест оформления заказа залогиненным пользователем')
    def test_place_order_as_logged_user(self, main_page, login_in):
        """
        Проверяет возможность оформления заказа авторизованным пользователем
        и получение корректного ID заказа
        """
        # Добавляем ингредиенты в заказ
        main_page.drag_and_drop_ingredient_bun()
        main_page.drag_and_drop_ingredient_souses()

        # Оформляем заказ
        main_page.click_place_order_button()
        order_id = main_page.get_order_id_from_popup()

        # Проверяем успешное оформление заказа
        assert (
            main_page.wait_for_popup_order_id_window()
            and order_id is not None
            and order_id != '9999'
        ), (
            "Не открылось всплывающее окно с идентификатором заказа, "
            "ID заказа остался '9999' или не обновился на актуальный"
        )
