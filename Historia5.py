import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

chromedriver_path = "chromedriver.exe"

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

try:

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    time.sleep(2)

    driver.find_element(By.NAME, "my-text").send_keys("Texto de prueba")

    driver.find_element(By.NAME, "my-password").send_keys("password123")

    driver.find_element(By.NAME, "my-textarea").send_keys("Este es un comentario extenso\nen varias líneas.")

    driver.find_element(By.NAME, "my-date").send_keys("2025-04-10")

    driver.find_element(By.NAME, "my-datalist").send_keys("Option 1")

    select_element = Select(driver.find_element(By.NAME, "my-select"))
    select_element.select_by_visible_text("Two")

    driver.find_element(By.NAME, "my-colors").send_keys("#ff5733")  # Color personalizado

    driver.find_element(By.NAME, "my-range").send_keys("8")

    checkbox1 = driver.find_element(By.ID, "my-check-1")
    if not checkbox1.is_selected():
        checkbox1.click()

    checkbox2 = driver.find_element(By.ID, "my-check-2")
    if not checkbox2.is_selected():
        checkbox2.click()

    radio1 = driver.find_element(By.ID, "my-radio-1")
    radio1.click()
    radio2 = driver.find_element(By.ID, "my-radio-2")
    radio2.click()

    time.sleep(2)

    driver.save_screenshot("captura_historia5_formulario_lleno.png")

    main_window = driver.current_window_handle

    driver.execute_script("window.open('https://www.google.com', '_blank');")
    time.sleep(3)

    all_windows = driver.window_handles
    for win in all_windows:
        if win != main_window:
            driver.switch_to.window(win)
            break
    time.sleep(2)

    search_input = driver.find_element(By.NAME, "q")
    search_input.send_keys("Perros y gatos")
    search_input.send_keys(Keys.RETURN)
    time.sleep(4)

    driver.close()

    driver.switch_to.window(main_window)
    time.sleep(2)

    driver.save_screenshot("captura_historia5_final.png")
    time.sleep(1)

finally:
    driver.quit()
