import re 
from colorama import Fore
import requests 
import webbrowser



website = "https://onlyfans.com/my/statements/earnings"
resultado = requests.get(website)
content = resultado.text 

edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

patron = r"span b-stats-row__val g-semibold[\w-]*>([^<]+)"
datos_repetidos = re.findall(patron, str(content))

sin_duplicados = list(set(datos_repetidos))

webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
webbrowser.get('edge').open(website) 

print(resultado.text)



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path='C:\\Users\\hegrog\\Documents\\chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://onlyfans.com/my/statements/earnings')

inputs = driver.find_elements(By.CLASS_NAME, 'v-input__slot')
username_input = inputs[0]
password_input = inputs[1]
login_button = driver.find_element(By.CSS_SELECTOR, '.g-btn.m-rounded')


username_input.send_keys('lmontoyz23@gmail.com')
password_input.send_keys('REfgab5%432/D')
login_button.click()


try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'b-stats-row__val'))
    )
    datos_ingresos = driver.find_element(By.CLASS_NAME, 'b-stats-row__val').text
    print("Subcriptions:", datos_ingresos)
finally:
    driver.quit()




    username_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME,'v-input__control')) 
)
password_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME,'v-input__solt'))  
)
login_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, ".g-btn.m-rounded"))  
)


username = os.getenv('lmontoyz23@gmail.com')
password = os.getenv('REfgab5%432/D')

if username is None or password is None:
    print("Error: Las variables de entorno para el nombre de usuario y la contraseña no están establecidas.")
    driver.quit()
else:
    
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()

    
    try:
        datos_ingresos_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'b-stats-row__val'))
        )
        datos_ingresos = datos_ingresos_element.text
        print("Ingresos diarios:", datos_ingresos)
    except TimeoutException:
        print("El elemento no se encontró en el tiempo esperado")
    finally:
    
        driver.quit()