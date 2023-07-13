import time
from idlelib import search

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import keys, Keys
from selenium.webdriver.chrome.service import Service


ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service= ser, options=op)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)


nom = driver.find_element(By.XPATH, "//input[contains(@id,'userName')]")
nom.send_keys("Romina")
time.sleep(3)

nom = driver.find_element(By.XPATH,"//input[contains(@id,'userEmail')]")
nom.send_keys("romiolae1506@gmail.com")
time.sleep(2)

nom = driver.find_element(By.XPATH,"//textarea[contains(@id,'currentAddress')]")
nom.send_keys("Dirección 1")
time.sleep(2)

nom = driver.find_element(By.XPATH,"//textarea[contains(@id,'permanentAddress')]")
nom.send_keys("Direccion 2")
time.sleep(2)

driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)

nom = driver.find_element(By.XPATH,"//button[contains(@id,'submit')]")
nom.send_keys(Keys.ENTER)
time.sleep(2)

driver.back()
driver.close()

