from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

driver = webdriver.Chrome ()

driver.get('https://onlyfans.com')

load_dotenv('C:\Users\hegrog\Desktop\WebScrappingOnly\.env')

try:
    email_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'v-input__slot'))
    )
    password_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'v-input__slot')) 
    )
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'g-btn'))   
    )

    username = os.getenv('USERNAME')  
    password = os.getenv('PASSWORD')  

    if username is None or password is None:
        print("Error: Las variables de entorno para el nombre de usuario y la contraseña no están establecidas.")
    else:
        email_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

        datos_ingresos_element = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.CLASS_NAME,'.b-stats-row__val' ))
        )
        datos_ingresos = datos_ingresos_element.text
        print("Ingresos diarios:", datos_ingresos)

except TimeoutException:
    print("El elemento no se encontró en el tiempo esperado")
finally:
    driver.quit()

    