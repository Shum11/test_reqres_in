import allure
import pytest

from core.rest_methods import RestMethods


@allure.title('Проверить удаление учетной записи')
@pytest.mark.parametrize('num', [1, 5, 12])
def test_delete(num):
    req = '/api/users/' + str(num)
    response = RestMethods().delete_method(req)
    assert response.status_code == 204
