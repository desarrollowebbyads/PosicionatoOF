from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='C:\\path\\to\\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://onlyfans.com/my/statements/earnings')

try:
   
    datos_ingresos_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'b-stats-row__val'))
    )
    
    
    datos_ingresos = datos_ingresos_element.text
    print("Ingresos diarios:", datos_ingresos)
finally:
   
    driver.quit()