import allure
import pytest

from core.rest_methods import RestMethods
from data.lib_for_test import json_for_reg, negative_num
from static.enums.status_code import StatusCode


class TestUsersNegative:
    @allure.title('Негативный тест на регистрацию учетной записи')
    @pytest.mark.parametrize('json', [i for i in json_for_reg])
    def test_register_unsuccessfull(self, json):
        req = "/api/register"
        response = RestMethods().post_method(req, json)
        with allure.step('проверить статус ответа'):
            assert response.status_code == StatusCode.BAD_REQUEST.value

    @allure.title('Негативный тест на получение несуществующего пользователя')
    @pytest.mark.parametrize('numbers', [i for i in negative_num])
    def test_get_user(self, numbers):
        ask = f'/api/users/{numbers}'
        response = RestMethods().get_method(ask)
        with allure.step('проверить статус ответа'):
            assert response.status_code == StatusCode.NOT_FOUND.value

    @allure.title('Негативный тест на получение списка пользователей')
    @pytest.mark.parametrize('numbers', [i for i in negative_num])
    def test_get_users_list(self, numbers):
        ask = f'/api/users?page={numbers}'
        response = RestMethods().get_method(ask)
        with allure.step('Проверить статус ответа'):
            assert response.status_code == StatusCode.OK.value
        with allure.step('Проверить что список данных пуст'):
            assert response.json()['data'] == []
