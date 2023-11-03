import lib_for_test
from core.rest_methods import RestMethods


def test_create():
    req = "/api/users"
    json = {
        "name": "morpheus",
        "job": "leader"
    }
    response = RestMethods().post_method(req, json)
    assert response.status_code == 201
    assert "morpheus" in response.json()["name"]


def test_register_successfull():
    req = "/api/register"
    json = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = RestMethods().post_method(req, json)
    assert response.status_code == 200
    assert response.json() in lib_for_test.post_json


def test_login():
    req = "/api/login"
    json = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = RestMethods().post_method(req, json)
    assert response.status_code == 200
    assert response.json() in lib_for_test.post_json


def test_register_unsuccessfull():
    req = "/api/register"
    json = {
        "email": "sydney@fife"
    }
    response = RestMethods().post_method(req, json)
    assert response.status_code == 400
    assert response.json() in lib_for_test.post_json


def test_login_unsuccessfull():
    req = "/api/login"
    json = {
        "email": "peter@klaven"
    }
    response = RestMethods().post_method(req, json)
    assert response.status_code == 400
    assert response.json() in lib_for_test.post_json