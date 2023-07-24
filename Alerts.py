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
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
time.sleep(2)

aler = driver.find_element(By.XPATH, "//button[contains(@id,'confirmButton')]")

if(aler.is_displayed()==True):
    print("Existe el alerta")
    aler.click()
else:
    print("No existe")

time.sleep(3)

# / / aler = driver.switch_to_alert()
# / / aler.send_keys(Keys.CANCEL)
