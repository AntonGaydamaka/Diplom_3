import pytest
import allure
import requests
from faker import Faker

import utils.urls as urls

fake = Faker("ru_RU")


def generate_first_name():
    """
    Генерирует случайное имя пользователя
    """
    return fake.first_name()


def generate_email():
    """
    Генерирует случайный email
    """
    return fake.email()


def generate_password():
    """
    Генерирует случайный пароль
    """
    return fake.password()


def generate_data_user():
    """
    Формирует словарь с данными пользователя
    """
    return {
        'first_name': generate_first_name(),
        'email': generate_email(),
        'password': generate_password()
    }


@allure.step("Создание нового пользователя")
def register_new_user():
    """
    Выполняет регистрацию нового пользователя через API
    """
    user_data = generate_data_user()

    with allure.step("Формирование данных для регистрации"):
        register_url = urls.CREATE_USER
        payload = {
            "email": user_data['email'],
            "password": user_data['password'],
            "name": user_data['first_name']
        }
        headers = {'Content-Type': 'application/json'}

    with allure.step("Отправка запроса на регистрацию"):
        response = requests.post(
            register_url,
            json=payload,
            headers=headers
        )

    with allure.step("Проверка результата регистрации"):
        if response.status_code == 200:
            user_data['access_token'] = response.json().get("accessToken")
            return user_data, response
        else:
            pytest.fail(
                f"Ошибка при создании пользователя: "
                f"{response.status_code} - {response.text}"
            )


@allure.step("Удаление нового пользователя")
def delete_new_user(access_token):
    """
    Выполняет удаление пользователя через API
    """
    with allure.step("Формирование заголовков для удаления"):
        delete_url = urls.DELETE_USER
        delete_headers = {
            'Accept': 'application/json',
            'Authorization': f'{access_token}'
        }

    with allure.step("Отправка запроса на удаление"):
        delete_response = requests.delete(
            delete_url,
            headers=delete_headers
        )

    with allure.step("Проверка результата удаления"):
        if delete_response.status_code != 202:
            pytest.fail(
                f"Ошибка при удалении пользователя: "
                f"{delete_response.status_code} - {delete_response.text}"
            )
