import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:
    """Базовый класс для всех страниц приложения."""

    def __init__(self, driver):
        """
        Инициализация страницы.

        :param driver: объект веб-драйвера
        """
        self.driver = driver

    @allure.step("Открыть страницу по указанному URL: {url}")
    def get_url(self, url: str) -> None:
        """
        Открыть страницу по указанному URL.

        :param url: URL страницы для открытия
        """
        self.driver.get(url)

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self) -> str:
        """
        Получить текущий URL страницы.

        :return: текущий URL
        """
        return self.driver.current_url

    @allure.step("Ожидать, пока текущий URL станет равным: {url}")
    def wait_for_url(
        self, url: str, timeout: int = 5
    ) -> None:
        """
        Ожидать, пока текущий URL не станет равным ожидаемому.

        :param url: ожидаемый URL
        :param timeout: время ожидания (в секундах)
        """
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_to_be(url)
        )

    @allure.step("Найти элемент с локатором: {locator}")
    def find_element_with_wait(self, locator) -> None:
        """
        Найти элемент на странице с ожиданием его появления.

        :param locator: локатор элемента
        """
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    @allure.step("Кликнуть по элементу: {locator}")
    def click_on_element(self, locator) -> None:
        """
        Выполнить клик по элементу.

        :param locator: локатор элемента
        """
        element = self.find_element_with_wait(locator)
        ActionChains(self.driver).move_to_element(element).click().perform()

    @allure.step("Прокрутить страницу до элемента: {locator}")
    def scroll_into_view(self, locator) -> None:
        """
        Прокрутить страницу до заданного элемента.

        :param locator: локатор элемента
        """
        element = self.find_element_with_wait(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step("Получить текст из элемента: {locator}")
    def get_text_from_element(self, locator) -> str:
        """
        Получить текст из элемента.

        :param locator: локатор элемента
        :return: текст элемента
        """
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step("Проверить наличие элемента: {locator}")
    def is_element_present(
        self, locator, timeout: int = 5
    ) -> bool:
        """
        Проверить наличие элемента на странице.

        :param locator: локатор элемента
        :param timeout: время ожидания (в секундах)
        :return: True, если элемент найден, иначе False
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                expected_conditions.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Проверить отсутствие элемента: {locator}")
    def is_element_absent(
        self, locator, timeout: int = 5
    ) -> bool:
        """
        Проверить отсутствие элемента на странице.

        :param locator: локатор элемента
        :param timeout: время ожидания (в секундах)
        :return: True, если элемент отсутствует, иначе False
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                expected_conditions.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Перетащить элемент с {source_locator} на {target_locator}")
    def drag_and_drop_on_to_element(
        self, source_locator, target_locator
    ) -> None:
        """
        Перетащить элемент из одного места в другое.

        :param source_locator: локатор исходного элемента
        :param target_locator: локатор целевого элемента
        """
        from_element = self.find_element_with_wait(source_locator)
        to_element = self.find_element_with_wait(target_locator)
        return drag_and_drop(self.driver, from_element, to_element)

    @allure.step(
            "Ожидать изменения текста элемента {locator} "
            "с '{initial_text}'"
    )
    def wait_for_text_to_change(
        self, locator, initial_text: str, timeout: int = 10
    ) -> None:
        """
        Ожидает, пока текст элемента не изменится
        с initial_text на любой другой.

        :param locator: локатор элемента
        :param initial_text: исходный текст
        :param timeout: время ожидания (в секундах)
        """
        WebDriverWait(self.driver, timeout).until(
            lambda driver: (
                self.find_element_with_wait(locator)
                .text != initial_text
            )
        )

    @allure.step(
            "Ожидать появления текста '{expected_text}' в элементе {locator}"
    )
    def wait_for_text_to_be(
        self, locator, expected_text: str, timeout: int = 10
    ) -> None:
        """
        Ожидание, пока текст элемента не станет равным ожидаемому значению

        :param locator: локатор элемента
        :param expected_text: ожидаемый текст
        :param timeout: время ожидания (в секундах)
        """
        WebDriverWait(self.driver, timeout).until(
            lambda driver: (
                self.find_element_with_wait(locator).text == expected_text
            )
        )
