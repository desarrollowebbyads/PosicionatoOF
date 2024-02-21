from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://onlyfans.com/my/statements/earnings")
driver.implicitly_wait(10)
content = driver.page_source
driver.quit()
soup = BeautifulSoup(content, "html.parser")
valores = [span.text for span in soup.find_all('span', class_='b-stats-row__val')]
for valor in valores: 
    print(valor)
 

