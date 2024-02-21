from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

driver = webdriver.Chrome ()

driver.get('https://onlyfans.com/my/statements/earnings')


try:
    username_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    password_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))  
    )
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div/div[2]/div/form/button[1]'))   
    )

    username = os.getenv('lmontoyz23@gmail.com')  
    password = os.getenv('REfgab5%432/D')  

    if username is None or password is None:
        print("Error: Las variables de entorno para el nombre de usuario y la contraseña no están establecidas.")
    else:
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

        datos_ingresos_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]' ))
        )
        datos_ingresos = datos_ingresos_element.text
        print("Ingresos diarios:", datos_ingresos)

except TimeoutException:
    print("El elemento no se encontró en el tiempo esperado")
finally:
    driver.quit()

    