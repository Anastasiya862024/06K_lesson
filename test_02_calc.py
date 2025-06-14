from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_slow_calculator():

    browser = webdriver.Chrome()

    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    input = browser.find_element(By.CSS_SELECTOR, '#delay')
    input.clear()
    input.send_keys("45")

    button = browser.find_element(By.XPATH, '//span[text()="7"]')
    button.click()

    button = browser.find_element(By.XPATH, '//span[text()="+"]')
    button.click()

    button = browser.find_element(By.XPATH, '//span[text()="8"]')
    button.click()

    button = browser.find_element(By.XPATH, '//span[text()="="]')
    button.click()

    WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))
    )
    WebDriverWait(browser, 60).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    res = browser.find_element(By.CSS_SELECTOR, ".screen").text
    assert res == "15"

    browser.quit()
