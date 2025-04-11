import allure
import pytest

from core.rest_methods import RestMethods
from data.lib_for_test import json_for_reg, json_for_reg_correct
from static.enums.status_code import StatusCode


class TestLogin:
    @allure.title("Аутентификация учетной записи")
    @pytest.mark.parametrize("json", [i for i in json_for_reg_correct])
    def test_login_successfull(self, json):
        req = "/api/login"
        response = RestMethods().post_method(req, json)
        with allure.step("проверить статус ответа"):
            assert response.status_code == StatusCode.OK.value
        with allure.step("проверить token "):
            assert response.json()["token"] == "QpwL5tke4Pnpja7X4"

    @allure.title("Негативный тест аутентификации")
    @pytest.mark.parametrize("json", [i for i in json_for_reg])
    def test_login_unsuccessfull(self, json):
        req = "/api/login"
        response = RestMethods().post_method(req, json)
        with allure.step("проверить статус ответа"):
            assert response.status_code == StatusCode.BAD_REQUEST.value
