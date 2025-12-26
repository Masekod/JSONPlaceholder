import requests
from config.constants import BASE_URL
import allure


class ApiClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()

    @allure.step("Получение списка постов")
    def get_posts(self):
        response = requests.get(f'{BASE_URL}/posts')
        return response

    @allure.step("Получение списка постов")
    def post_posts(self):
        response = requests.post(f'{BASE_URL}/posts')
        return response

    @allure.step("Получение списка постов")
    def delete_post(self):
        response = requests.get(f'{BASE_URL}/posts/1')
        return response
