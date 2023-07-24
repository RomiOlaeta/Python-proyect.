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
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

nom = driver.find_element(By.CSS_SELECTOR, "#item-2")
nom.click()
time.sleep(4)
btn1 = driver.find_element(By.XPATH, "//label[@class='custom-control-label'][contains(.,'Yes')]")
print(btn1.is_enabled())

if(btn1.is_enabled()==True):
    print("Puedes darle click")
    btn1.click()

else:
    print("No se puede dar click")
time.sleep(4)
