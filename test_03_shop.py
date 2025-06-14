import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()


def test_purchase(browser):
    browser.get("https://www.saucedemo.com/")

    username_input = browser.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()

    backpack_button = browser.find_element(
        By.XPATH, "//div[@class='inventory_item' and \
            .//div[contains(text(), 'Sauce Labs Backpack')]]//button")
    backpack_button.click()
    tshirt_button = browser.find_element(
        By.XPATH, "//div[@class='inventory_item' and \
            .//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]]//button")
    tshirt_button.click()
    onesie_button = browser.find_element(
        By.XPATH, "//div[@class='inventory_item' and \
            .//div[contains(text(), 'Sauce Labs Onesie')]]//button")
    onesie_button.click()

    cart_link = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()

    checkout_button = browser.find_element(By.ID, "checkout")
    checkout_button.click()

    first_name_input = browser.find_element(By.ID, "first-name")
    first_name_input.send_keys("Анастасия")
    last_name_input = browser.find_element(By.ID, "last-name")
    last_name_input.send_keys("Иванова")
    postal_code_input = browser.find_element(By.ID, "postal-code")
    postal_code_input.send_keys("987654")

    continue_button = browser.find_element(By.ID, "continue")
    continue_button.click()

    total_cost = browser.find_element(
        By.CLASS_NAME, "summary_total_label").text
    total_cost_value = float(total_cost.split("$")[1])

    assert total_cost_value == 58.29, f"Итоговая сумма \
        должна быть 58.29, но получена {total_cost_value}"
