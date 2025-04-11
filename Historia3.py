
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

chromedriver_path = "./chromedriver.exe"

@pytest.fixture
def setup():
    service = Service(chromedriver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_lleno_todos_los_campos_y_capturo(setup):
    driver = setup
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    time.sleep(2)


    driver.find_element(By.NAME, "my-text").send_keys("Texto de prueba")

    driver.find_element(By.NAME, "my-password").send_keys("MiRealclavesitaepica123")

    driver.find_element(By.NAME, "my-textarea").send_keys("Texto extenso\nen varias líneas\npara probar.")

    checkbox = driver.find_element(By.NAME, "my-check")
    if not checkbox.is_selected():
        checkbox.click()


    radio = driver.find_element(By.ID, "my-radio-2")
    radio.click()


    select_element = Select(driver.find_element(By.NAME, "my-select"))
    select_element.select_by_visible_text("Three")

    datalist_input = driver.find_element(By.NAME, "my-datalist")
    datalist_input.clear()
    datalist_input.send_keys("New York")

    date_input = driver.find_element(By.NAME, "my-date")
    date_input.send_keys("2025-04-10")  # Formato YYYY-MM-DD

    color_picker = driver.find_element(By.NAME, "my-colors")
    color_picker.send_keys("#00FF00")  # Verde brillante acuerdate xd

    range_input = driver.find_element(By.NAME, "my-range")
    range_input.send_keys("8")

    time.sleep(2)

    driver.save_screenshot("captura_historia3.png")
    time.sleep(1)
