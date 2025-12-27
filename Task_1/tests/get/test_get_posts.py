import allure
import requests
from Task_1.config.constants import BASE_URL
from http import HTTPStatus


@allure.feature("Получение списка постов")
@allure.story("Проверка статус кода ответа")
def test_get_posts():
    response = requests.get(f'{BASE_URL}/posts')
    assert response.status_code == HTTPStatus.OK, f" GET /posts вернул {response.status_code}, ожидали 200 OK"