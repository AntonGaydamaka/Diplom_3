import allure
import pytest
import utils.urls as urls


class TestFeedPage:
    """
    Тест-кейсы для проверки функционала страницы «Лента заказов»
    """

    @allure.feature('Раздел «Лента заказов»')
    @allure.story('Отображение созданного заказа')
    @allure.title('Тест на отображение ID созданного заказа '
                  'в разделе «В работе»')
    def test_display_id_order(self, main_page, feed_page, order_id):
        """
        Проверяет появление ID заказа в разделе «В работе» после его создания
        """
        main_page.click_order_feed_button()
        feed_page.wait_for_order_id_in_ready_list(order_id)
        actual_id = feed_page.get_order_id_from_list_ready()
        assert actual_id == f'0{order_id}', (
            f"Ожидался ID заказа '0{order_id}', но получен {actual_id}"
        )

    @allure.feature('Раздел «Лента заказов»')
    @allure.story('Работа с деталями заказа')
    @allure.title('Тест открытия модального окна с деталями заказа')
    def test_open_popup_window_with_order_details(
        self,
        main_page,
        feed_page,
        order_id
    ):
        """
        Проверяет открытие всплывающего окна с деталями заказа
        """
        main_page.click_order_feed_button()
        feed_page.find_and_click_order_by_id(order_id)
        assert feed_page.wait_for_popup_order_details_window(), (
            "Не открылось всплывающее окно с деталями заказа"
        )

    @pytest.mark.parametrize(
        "counter_name, get_initial_count, get_new_count, story, title",
        [
            (
                "за все время",
                lambda feed_page: feed_page.get_number_orders_all_time(),
                lambda feed_page: feed_page.get_number_orders_all_time(),
                "При создании нового заказа счётчик "
                "«Выполнено за всё время» увеличивается",
                "Тест на увеличение счётчика заказов "
                "«за все время» после добавления заказа",
            ),
            (
                "за сегодня",
                lambda feed_page: feed_page.get_number_orders_today(),
                lambda feed_page: feed_page.get_number_orders_today(),
                "При создании нового заказа счётчик "
                "«Выполнено за сегодня» увеличивается",
                "Тест на увеличение счётчика заказов "
                "«за сегодня» после добавления заказа",
            ),
        ],
    )
    @allure.feature('Раздел «Лента заказов»')
    def test_order_counter_increases(
        self,
        main_page,
        feed_page,
        login_in,
        counter_name,
        get_initial_count,
        get_new_count,
        story,
        title
    ):
        """
        Проверяет корректность работы счетчиков заказов
        """
        allure.dynamic.story(story)
        allure.dynamic.title(title)

        # Переход в ленту заказов
        main_page.click_order_feed_button()
        # Зафиксировать текущее значение счётчика
        initial_count = get_initial_count(feed_page)
        # Создание нового заказа
        main_page.click_constructor_button()
        main_page.create_order()
        # Проверка нового значения счётчика
        main_page.click_order_feed_button()
        new_count = get_new_count(feed_page)
        assert new_count == initial_count + 1, (
            f"Ожидалось увеличение счётчика на 1, "
            f"но он изменился с {initial_count} на {new_count}"
        )

    @allure.feature('Раздел «Лента заказов»')
    @allure.story('Синхронизация заказов между разделами')
    @allure.title('Тест на отображение заказа в разделах '
                  '«Лента заказов» и «История заказов»')
    def test_display_id_order_from_order_history(
        self, main_page, feed_page, account_page, order_id
    ):
        """
        Проверяет синхронизацию заказов между лентой и историей
        """
        # Переход в ленту заказов
        main_page.click_order_feed_button()

        # Поиск заказа в ленте
        order_id_in_feed = feed_page.find_order_by_id(order_id)

        # Переход в личный кабинет
        feed_page.click_personal_account_button()

        # Переход в историю заказов
        account_page.click_order_history_link()

        # Прокрутка до заказа в истории
        feed_page.scroll_order_in_history()

        # Поиск заказа в истории
        order_id_in_history = feed_page.find_order_by_id(order_id)

        # Проверка совпадения ID заказа
        assert order_id_in_feed == order_id_in_history, (
            f"ID заказа в ленте ({order_id_in_feed}) не совпадает "
            f"с ID в истории ({order_id_in_history})"
        )


class TestAccountPage:
    """
    Тест-кейсы для проверки функционала страницы «Личный кабинет»
    """

    @allure.feature('Навигация')
    @allure.story('Переход в раздел «История заказов»')
    @allure.title('Тест перехода в раздел «История заказов»')
    def test_switch_order_history_in_account(
        self, login_in, account_page
    ):
        """
        Проверяет корректность перехода в историю заказов
        """
        current_url = account_page.click_order_history_link()
        assert current_url == urls.ACCOUNT_ORDER_HISTORY_URL, (
            f"Ожидался URL {urls.ACCOUNT_ORDER_HISTORY_URL}, "
            f"но был {current_url}"
        )

    @allure.feature('Авторизация')
    @allure.story('Выход из аккаунта')
    @allure.title('Тест выхода из аккаунта')
    def test_exit_in_account(
        self, login_in, account_page
    ):
        """
        Проверяет корректность выхода из аккаунта
        """
        current_url = account_page.click_exit_button()
        assert current_url == urls.LOGIN_URL, (
            f"Ожидался URL {urls.LOGIN_URL}, но был {current_url}"
        )
