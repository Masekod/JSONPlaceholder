import allure
import requests
from Task_1.config.constants import BASE_URL, expected_codes_delete


@allure.feature("Удаление поста")
@allure.story("Проверка статус кода ответа")
def test_delete_post():
    response = requests.get(f'{BASE_URL}/posts/1')
    assert response.status_code in expected_codes_delete, (f"DELETE /posts/1 вернул {response.status_code}, "
                                                           f"ожидали 204 NO_CONTENT")
