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

    def test1(self):
        driver.get("https://demoqa.com/text-box")
        time.sleep(4)
    def tearDown(self):
        driver.close()

if __name__=='__main__':
 unittest.main()
