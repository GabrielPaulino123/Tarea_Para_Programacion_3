import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

@pytest.mark.story("Historia 2")
def test_modificar_campos_de_texto():
    chromedriver_path = "chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:

        url = "https://www.selenium.dev/selenium/web/web-form.html"
        driver.get(url)
        assert driver.current_url == url, f"No estás en la URL correcta: {driver.current_url}"

        text_input = driver.find_element(By.NAME, "my-text")
        text_input.clear()
        text_input.send_keys("Texto de prueba")


        password_input = driver.find_element(By.NAME, "my-password")
        password_input.clear()
        password_input.send_keys("Contraseña123")


        time.sleep(3)


        driver.save_screenshot("captura_historia2.png")

    finally:

        driver.quit()
