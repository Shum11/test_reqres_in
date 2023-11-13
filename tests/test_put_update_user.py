import allure
import pytest

from core.rest_methods import RestMethods
from data.lib_for_test import json_for_patch


@allure.title('Замена данных учетной записи')
@pytest.mark.parametrize('json', [i for i in json_for_patch])
def test_put_method(json):
    req = "/api/users/2"
    response = RestMethods().put_method(req, json)
    with allure.step('проверить статус ответа'):
        assert response.status_code == 200
    with allure.step('проверить изменение поля name'):
        assert json['name'] in response.json()['name']
    with allure.step('проверить изменение поля job '):
        assert json['job'] in response.json()['job']
