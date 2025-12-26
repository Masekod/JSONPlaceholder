from http import HTTPStatus

BASE_URL = 'https://jsonplaceholder.typicode.com/'
expected_codes_post = [HTTPStatus.CREATED, HTTPStatus.OK]
expected_codes_delete = [HTTPStatus.CREATED, HTTPStatus.OK]