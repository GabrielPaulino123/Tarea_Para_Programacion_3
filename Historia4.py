# test_historia4.py

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

def test_lleno_y_envio_formulario_completo(setup):
    driver = setup
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    time.sleep(2)

    driver.find_element(By.NAME, "my-text").send_keys("Texto de prueba")

    driver.find_element(By.NAME, "my-password").send_keys("Clavinclinprogramacion")

    driver.find_element(By.NAME, "my-textarea").send_keys("Comentario de prueba\nEn varias líneas.")

    checked_checkbox = driver.find_element(By.ID, "my-check-1")
    if not checked_checkbox.is_selected():
        checked_checkbox.click()

    default_checkbox = driver.find_element(By.ID, "my-check-2")
    if not default_checkbox.is_selected():
        default_checkbox.click()

    checked_radio = driver.find_element(By.ID, "my-radio-1")
    checked_radio.click()

    default_radio = driver.find_element(By.ID, "my-radio-2")
    default_radio.click()

    select_element = Select(driver.find_element(By.NAME, "my-select"))
    select_element.select_by_visible_text("Two")

    datalist_input = driver.find_element(By.NAME, "my-datalist")
    datalist_input.send_keys("Berlin")

    date_input = driver.find_element(By.NAME, "my-date")
    date_input.send_keys("2025-04-10")


    color_picker = driver.find_element(By.NAME, "my-colors")
    color_picker.send_keys("#0033FF")  # Azul

    range_input = driver.find_element(By.NAME, "my-range")
    range_input.send_keys("7")

    time.sleep(2)

    driver.save_screenshot("captura_historia4_antes_de_enviar.png")

    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(2)

    driver.save_screenshot("captura_historia4_despues_de_enviar.png")
