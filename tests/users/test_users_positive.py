import allure
import pytest

from core.rest_methods import RestMethods
from data import lib_for_test
from data.lib_for_test import json_for_patch, json_for_reg_correct
from static.enums.status_code import StatusCode


class TestUsers:
    @allure.title('Создать новую учетную запись')
    @pytest.mark.parametrize('json', [i for i in json_for_patch])
    def test_create(self, json):
        req = "/api/users"
        response = RestMethods().post_method(req, json)
        with allure.step('проверить статус ответа'):
            assert response.status_code == StatusCode.CREATED.value
        with allure.step('проверить поле name'):
            assert json['name'] in response.json()['name']
        with allure.step('проверить поле job '):
            assert json['job'] in response.json()['job']

    @allure.title('Проверить удаление учетной записи')
    @pytest.mark.parametrize('num', [1, 5, 12])
    def test_delete(self, num):
        req = f'/api/users/{num}'
        response = RestMethods().delete_method(req)
        assert response.status_code == StatusCode.NO_CONTENT.value

    @allure.title('Получить пользователя по id')
    @pytest.mark.parametrize('numbers', [i for i in range(1, 13)])
    def test_get_user(self, numbers):
        ask = f'/api/users/{numbers}'
        response = RestMethods().get_method(ask)
        json = lib_for_test.get_positive['/api/users?page=1']
        json2 = lib_for_test.get_positive['/api/users?page=2']
        with allure.step('проверить статус ответа'):
            assert response.status_code == StatusCode.OK.value
        with allure.step('проверить data'):
            assert response.json()['data'] in json['data'] or json2

    @allure.title('Получить список пользователей, страница 1')
    def test_get_users_list_page_1(self):
        response = RestMethods().get_method('/api/users?page=1')
        with allure.step('проверить статус ответа'):
            assert response.status_code == StatusCode.OK.value
        with allure.step('сравнить ответ с шаблоном'):
            assert response.json()['data'] == lib_for_test.get_positive['/api/users?page=1']['data']
        with allure.step('проверить текущий номер страницы'):
            assert response.json()['page'] == 1

    @allure.title('Получить список пользователей, страница 2')
    def test_get_users_list_page_2(self):
        response = RestMethods().get_method('/api/users?page=2')
        with allure.step('проверить статус ответа'):
            assert response.status_code == StatusCode.OK.value
        with allure.step('сравнить ответ с шаблоном'):
            assert response.json()['data'] == lib_for_test.get_positive['/api/users?page=2']['data']
        with allure.step('проверить текущий номер страницы'):
            assert response.json()['page'] == 2

    @allure.title('Измененить значения полей учетной записи')
    @pytest.mark.parametrize('json', [i for i in json_for_patch])
    def test_patch_method(self, json):
        req = "/api/users/2"
        response = RestMethods().patch_method(req, json)
        with allure.step('проверить статус ответа'):
            assert response.status_code == StatusCode.OK.value
        with allure.step('проверить изменение поля name'):
            assert json['name'] in response.json()['name']
        with allure.step('проверить изменение поля job '):
            assert json['job'] in response.json()['job']

    @allure.title('Заменить данные учетной записи')
    @pytest.mark.parametrize('json', [i for i in json_for_patch])
    def test_put_method(self, json):
        req = "/api/users/2"
        response = RestMethods().put_method(req, json)
        with allure.step('проверить статус ответа'):
            assert response.status_code == StatusCode.OK.value
        with allure.step('проверить изменение поля name'):
            assert json['name'] in response.json()['name']
        with allure.step('проверить изменение поля job '):
            assert json['job'] in response.json()['job']

    @allure.title('Регистрация учетной записи')
    @pytest.mark.parametrize('json', [i for i in json_for_reg_correct])
    def test_register_successfull(self, json):
        req = "/api/register"
        response = RestMethods().post_method(req, json)
        with allure.step('проверить статус ответа'):
            assert response.status_code == StatusCode.OK.value
        with allure.step('проверить поле id'):
            assert response.json()['id'] == 4
        with allure.step('проверить token '):
            assert response.json()['token'] == 'QpwL5tke4Pnpja7X4'
