import allure
import requests
from config.constants import BASE_URL, expected_codes_post


@allure.feature("Создание поста")
@allure.story("Проверка статус кода ответа")
def test_post_post():
    response = requests.post(f'{BASE_URL}/posts')
    assert response.status_code in expected_codes_post, (f" POST /posts вернул {response.status_code},"
                                                         f" ожидали 201 CREATED")
