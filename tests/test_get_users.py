import allure
import pytest

from core.rest_methods import RestMethods
from data import lib_for_test
from data.lib_for_test import negative_num


@allure.title('Получение списка пользователей')
def test_get_users_list_page_1():
    response = RestMethods().get_method('/api/users?page=2')
    with allure.step('проверить статус ответа'):
        assert response.status_code == 200
    with allure.step('сравнить ответ с шаблоном'):
        assert response.json()['data'] == lib_for_test.get_positive['/api/users?page=2']['data']
    with allure.step('проверить текущий номер страницы'):
        assert response.json()['page'] == 2


@allure.title('Получение списка пользователей')
def test_get_users_list_page_2():
    response = RestMethods().get_method('/api/users?page=1')
    with allure.step('проверить статус ответа'):
        assert response.status_code == 200
    with allure.step('сравнить ответ с шаблоном'):
        assert response.json()['data'] == lib_for_test.get_positive['/api/users?page=1']['data']
    with allure.step('проверить текущий номер страницы'):
        assert response.json()['page'] == 1


@allure.title('Негативный тест на получение списка пользователей')
@pytest.mark.parametrize('numbers', [i for i in negative_num])
def test_get_users_list(numbers):
    ask = '/api/users?page=' + str(numbers)
    response = RestMethods().get_method(ask)
    with allure.step('Проверить статус ответа'):
        assert response.status_code == 200
    with allure.step('Проверить что список данных пуст'):
        assert response.json()['data'] == []
