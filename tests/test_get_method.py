import pytest
import allure

import lib_for_test
from core.rest_methods import RestMethods


@allure.title('получение списка пользователей')
def test_get_users_list():
    response = RestMethods().get_method("/api/users?page=2")
    assert response.status_code == 200
    assert response.json() == lib_for_test.get_positive["/api/users?page=2"]


@allure.title('получение определённого пользователя')
def test_get_user():
    response = RestMethods().get_method('/api/users/2')
    assert response.status_code == 200
    assert response.json() == lib_for_test.get_positive['/api/users/2']


@allure.title('получение списка ресурсов')
def test_get_list_resource():
    response = RestMethods().get_method('/api/unknown')
    assert response.status_code == 200
    assert response.json() == lib_for_test.get_positive['/api/unknown']


@allure.title('получение определённого ресурса')
def test_get_method():
    response = RestMethods().get_method('/api/unknown/2')
    assert response.status_code == 200
    assert response.json() == lib_for_test.get_positive['/api/unknown/2']


@allure.title('несуществующий запрос')
@pytest.mark.parametrize("req", [i for i in lib_for_test.get_negative])
def test_get_method_negative(req):
    response = RestMethods().get_method(req)
    assert response.status_code == 404
