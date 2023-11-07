import allure
from core.rest_methods import RestMethods


@allure.title('изменение данных')
def test_patch_method():
    req = "/api/users/2"
    json = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = RestMethods().patch_method(req, json)
    assert response.status_code == 200
    assert "morpheus" in response.json()["name"]
    assert "zion resident" in response.json()["job"]

