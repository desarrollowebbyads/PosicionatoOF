from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
perfil_usuario = r"C:\Users\hegrog\AppData\Local\Temp\scoped_dir9040_125638281\Default"
chrome_options.add_argument(f"user-data-dir={perfil_usuario}")  


servicio = Service(r"C:\Users\hegrog\Documents\chromedriver.exe")  

navegador = webdriver.Chrome(service=servicio, options=chrome_options) 
options.add_argument('--profile-directory=Default')
options.add_argument('--user-data-dir=C:/Temp/ChromeProfile')

navegador.get("https://onlyfans.com/my/statements/earnings")

try:
    WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'b-stats-row__val'))
    )
    datos_ingresos = navegador.find_element(By.CLASS_NAME, 'b-stats-row__val').text
    print("Subscriptions:", datos_ingresos)
finally:
    navegador.quit()  