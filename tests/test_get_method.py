import pytest
import allure

import lib_for_test
from core.rest_methods import RestMethods


@allure.title('тест на гет-запрос')
@pytest.mark.parametrize("req", [i for i in lib_for_test.get_positive])
def test_get_method(req):
    response = RestMethods().get_method(req)
    assert response.status_code == 200
    assert response.json() == lib_for_test.get_positive[req]


@allure.title('несуществующий запрос')
@pytest.mark.parametrize("req", [i for i in lib_for_test.get_negative])
def test_get_method_negative(req):
    response = RestMethods().get_method(req)
    assert response.status_code == 404
