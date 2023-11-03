from core.rest_methods import RestMethods


def test_delete():
    req = "/api/users"
    response = RestMethods().delete_method(req)
    assert response.status_code == 204
