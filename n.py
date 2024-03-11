from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from dotenv import load_dotenv
import os


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
if username is None or password is None:
    print("Error: Environment variables for username and password are not set.")
    exit()

s = Service('C:/Users/hegrog/Desktop/chromedriver.exe')
driver = webdriver.Chrome(service=s)


driver.get('https://onlyfans.com')

try:
    # Wait until the email input field is clickable
    email_input = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, '.v-input__slot'))
    )
    password_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, '.v-input__slot'))
    )
    login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, '.g-btn'))
    )

    email_input.send_keys(username)
    password_input.send_keys(password)
    
    login_button.click()

    datos_ingresos_element = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.CLASS_NAME, '.b-stats-row__val'))
    )
    datos_ingresos = datos_ingresos_element.text
    print("Daily income:", datos_ingresos)

except (TimeoutException, NoSuchElementException, WebDriverException) as e:
    print(f"An error occurred: {str(e)}")
finally:
    driver.quit()