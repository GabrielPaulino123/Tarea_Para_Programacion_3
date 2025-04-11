import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
@pytest.mark.story("Historia 1 - Navegar a una página web")
def test_navegacion_basica():

    chromedriver_path = "chromedriver.exe"

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Abrir maximizado

    service = Service(chromedriver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:

        url = "https://www.selenium.dev/selenium/web/web-form.html"

        driver.get(url)

        time.sleep(3)

        assert driver.current_url == url, f"La URL actual no es la esperada: {driver.current_url}"
        driver.save_screenshot("captura_historia1.png")

    finally:
        driver.quit()
