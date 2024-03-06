from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--enable-logging")
chrome_options.add_argument("--v=1")

# Asegúrate de reemplazar 'C:\\path\\to\\chromedriver.exe' con tu ruta correcta a chromedriver
ser = Service('C:\\path\\to\\chromedriver.exe')
service = Service(executable_path='C:\\path\\to\\chromedriver.exe', log_path='C:\\path\\to\\chromedriver.log')
driver = webdriver.Chrome(service=ser)

driver.get("http://www.google.com")

datos_ingresos_element = WebDriverWait(driver, 120).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'b-stats-row__val'))
)
datos_ingresos = datos_ingresos_element.text
print("Ingresos diarios:", datos_ingresos)


driver.quit()