import pytest

import allure

from core.rest_methods import RestMethods
from data.lib_for_test import json_for_patch


@allure.title('Создать новую учетную запись')
@pytest.mark.parametrize('json', [i for i in json_for_patch])
def test_create(json):
    req = "/api/users"
    response = RestMethods().post_method(req, json)
    with allure.step('проверить статус ответа'):
        assert response.status_code == 201
    with allure.step('проверить поле name'):
        assert json['name'] in response.json()['name']
    with allure.step('проверить поле job '):
        assert json['job'] in response.json()['job']