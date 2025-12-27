import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")

    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    time.sleep(2)
    assert "inventory" in driver.current_url, "Вход не удался"

    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()

    logout_link = WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_link.click()

    assert "saucedemo.com" in driver.current_url, "Выход не удался"
