## Описание
 Проект содержит:
 - Экспорт коллекции Postman (.json)
 - Отчет о тестировании
 - Автотесты

### Работа с отчётами allure-pytest
1. Установка allure: pip install allure-pytest
2. Запуск с генерацией Allure-отчёта: pytest --alluredir=allure-results
3. Просмотр отчёта: allure serve allure-results