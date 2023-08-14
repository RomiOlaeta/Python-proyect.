import time
import driver as driver
import unittest
from idlelib import search
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import keys, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver

    def test_login(self):
        driver = self.driver
        driver.get("https://demoqa.com/login")
        driver.maximize_window()
        time.sleep(4)
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'userName')]")
        clave=driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        bt=driver.find_element(By.XPATH, "//button[contains(@id,'login')]")
        nom.send_keys("Romina")
        clave.send_keys("123")
        bt.click()
        error=driver.find_element_by_xpath("//p[contains(@id,'name')]")

        if(error=="Invalid username or password!"):
            print("Los datos no son correctos")
        else:
            print("La prueba esta OK")
        time.sleep(4)

    def tearDown(self):
        driver.close()

if __name__=='__main__':
 unittest.main()