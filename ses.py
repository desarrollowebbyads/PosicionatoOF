from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service  # Asegúrate de importar Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://onlyfans.com")

try:
    username_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']"))
    )
    username_input.send_keys("lmontoyz23@gmail.com")

    password_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
    )
    password_input.send_keys("REfgab5%432/D")

    submit_button = WebDriverWait(driver, 20).until( 
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

except TimeoutException:
    print("El elemento no se encontró en el tiempo máximo especificado.")
  
finally:
    driver.quit()