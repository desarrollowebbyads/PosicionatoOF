from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Agregar esta importación
from dotenv import load_dotenv
import os

# Cargar el archivo .env
load_dotenv('C:\\Users\\hegrog\\Desktop\\WebScrappingOnly\\.env')

# Inicializar el driver de Chrome
driver = webdriver.Chrome()

# Abrir la página web
driver.get('https://onlyfans.com')

try:
    # Esperar hasta que el campo de correo electrónico esté interactuable
    email_input = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'v-input__slot'))
    )

    # Esperar hasta que el campo de contraseña esté interactuable
    password_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, 'password'))
    )

    # Esperar hasta que el botón de inicio de sesión esté interactuable
    login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'g-btn'))
    )

    # Obtener el nombre de usuario y la contraseña del archivo .env
    username = os.getenv('USERNAME')  
    password = os.getenv('PASSWORD')  

    # Verificar si se han definido las variables de entorno
    if username is None or password is None:
        print("Error: Las variables de entorno para el nombre de usuario y la contraseña no están establecidas.")
    else:
        # Introducir el nombre de usuario y la contraseña
        email_input.send_keys(username)
        password_input.send_keys(password)
        # Hacer clic en el botón de inicio de sesión
        login_button.click()

        # Esperar hasta que se cargue la información de ingresos
        datos_ingresos_element = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'b-stats-row__val'))
        )
        datos_ingresos = datos_ingresos_element.text
        print("Ingresos diarios:", datos_ingresos)

except TimeoutException:
    print("El elemento no se encontró en el tiempo esperado")
finally:
    # Cerrar el navegador
    driver.quit()


