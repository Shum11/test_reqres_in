import allure
import pytest

from core.rest_methods import RestMethods
from data import lib_for_test
from data.lib_for_test import negative_num


@allure.title('Получение пользователя по id')
@pytest.mark.parametrize('numbers', [i for i in range(1, 13)])
def test_get_user(numbers):
    ask = '/api/users/' + str(numbers)
    response = RestMethods().get_method(ask)
    json = lib_for_test.get_positive['/api/users?page=1']
    json2 = lib_for_test.get_positive['/api/users?page=2']
    with allure.step('проверить статус ответа'):
        assert response.status_code == 200
    with allure.step('проверить data'):
        assert response.json()['data'] in json['data'] or json2


@allure.title('Негативный тест на получение несуществующего пользователя')
@pytest.mark.parametrize('numbers', [i for i in negative_num])
def test_get_user(numbers):
    ask = '/api/users/' + str(numbers)
    response = RestMethods().get_method(ask)
    with allure.step('проверить статус ответа'):
        assert response.status_code == 404
