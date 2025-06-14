import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    browser = webdriver.Edge()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.mark.usefixtures("browser")
def test_fill_form(browser):

    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    first_name_input = browser.find_element(By.NAME, 'first-name')
    first_name_input.send_keys("Иван")

    last_name_input = browser.find_element(By.NAME, 'last-name')
    last_name_input.send_keys("Петров")

    address_input = browser.find_element(By.NAME, 'address')
    address_input.send_keys("Ленина, 55-3")

    email_input = browser.find_element(By.NAME, 'e-mail')
    email_input.send_keys("test@skypro.com")

    phone_number_input = browser.find_element(By.NAME, 'phone')
    phone_number_input.send_keys("+7985899998787")

    city_input = browser.find_element(By.NAME, 'city')
    city_input.send_keys("Москва")

    country_input = browser.find_element(By.NAME, 'country')
    country_input.send_keys("Россия")

    job_position_input = browser.find_element(By.NAME, 'job-position')
    job_position_input.send_keys("QA")

    company_input = browser.find_element(By.NAME, 'company')
    company_input.send_keys("SkyPro")

    button = browser.find_element(By.CSS_SELECTOR, 'button')
    button.click()

    pole_z = browser.find_element(By.ID, "zip-code").get_attribute("class")
    assert pole_z == "alert py-2 alert-danger"

    poles = [
        "#first-name", "#last-name", "#address", "#city",
        "#country", "#e-mail", "#phone", "#company"]
    for pole in poles:
        pole_class = browser.find_element(By.CSS_SELECTOR, pole).get_attribute(
            "class")
        assert pole_class == "alert py-2 alert-success"
