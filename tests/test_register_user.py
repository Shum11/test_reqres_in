import allure
import pytest

from core.rest_methods import RestMethods
from data.lib_for_test import json_for_reg, json_for_reg_correct


@allure.title('Регистрация учетной записи')
@pytest.mark.parametrize('json', [i for i in json_for_reg_correct])
def test_register_successfull(json):
    req = "/api/register"
    response = RestMethods().post_method(req, json)
    with allure.step('проверить статус ответа'):
        assert response.status_code == 200
    with allure.step('проверить поле id'):
        assert response.json()['id'] == 4
    with allure.step('проверить token '):
        assert response.json()['token'] == 'QpwL5tke4Pnpja7X4'


@allure.title('Негативный тест на регистрацию учетной записи')
@pytest.mark.parametrize('json', [i for i in json_for_reg])
def test_register_unsuccessfull(json):
    req = "/api/register"
    response = RestMethods().post_method(req, json)
    with allure.step('проверить статус ответа'):
        assert response.status_code == 400
