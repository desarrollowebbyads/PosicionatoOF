from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Inicialización del WebDriver de Firefox
service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get('https://onlyfans.com/my/statements/earnings')

try:
    # Asegúrate de ajustar los selectores CLASS_NAME según sean necesarios, porque pueden variar entre navegadores
    email_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))  # Ejemplo de ajuste a CSS_SELECTOR para email
    )
    password_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))  # Ejemplo de ajuste a CSS_SELECTOR para contraseña
    )
    
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))  # Ejemplo de ajuste a CSS_SELECTOR para el botón de login
    )

    username = os.getenv('USERNAME')  
    password = os.getenv('PASSWORD')  

    if username is None or password is None:
        print("Error: Las variables de entorno para el nombre de usuario y la contraseña no están establecidas.")
    else:
        email_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

        # Ajusta el selector para los datos de ingresos según sea necesario
        datos_ingresos_element = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'nombre-clase-datos-ingresos'))  # Asegúrate de reemplazar 'nombre-clase-datos-ingresos' con el correcto
        )
        datos_ingresos = datos_ingresos_element.text
        print("Ingresos diarios:", datos_ingresos)

except TimeoutException:
    print("El elemento no se encontró en el tiempo esperado")
finally:
    driver.quit()
