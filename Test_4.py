import time
from idlelib import search

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import keys, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service= ser, options=op)
driver.get("https://demoqa.com/links")
driver.maximize_window()
time.sleep(2)

links = driver.find_elements(By.TAG_NAME, "a")

print("El numero de links que hay en la pagina son: ",len(links))

for num1 in links:
    print(num1.text)
time.sleep(2)

nom1 = driver.find_element_by_id("moved")
nom1.send_keys(Keys.ENTER)
<<<<<<< HEAD
time.sleep(4)
=======
time.sleep(4)
>>>>>>> origin/master1
