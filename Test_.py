import time
import driver as driver
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import keys, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service= ser, options=op)
driver.get("https://demoqa.com/upload-download")
driver.maximize_window()
time.sleep(4)

try:
    Bus = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'uploadFile')]")))
    Bus = driver.find_element(By.XPATH, "//input[contains(@id,'uploadFile')]")
    Bus.send_keys("C://Users//Romina//PycharmProjects//pythonProject2//Imagenes//Demo1.jpg")
    time.sleep(4)
    driver.find_element(By.ID, "downloadButton").click()
    time.sleep(4)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

<<<<<<< HEAD
    driver.quit()
=======
    driver.quit()
>>>>>>> origin/master1
