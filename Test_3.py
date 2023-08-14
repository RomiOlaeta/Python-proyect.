import time
import driver as driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import keys, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service= ser, options=op)
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
time.sleep(4)



dia = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(By.XPATH("//div[@class=' css-1hwfws3'][contains(.,'Select Option')]")))
print(dia.is_displayed())
dia.click()
dia.select_by_visible_text("Group 1, option 1")
time.sleep(4)
dia.click()

dia.select_by_value("Group 1, option 1")
time.sleep(3)
dia.select_by_value("groupOption")
<<<<<<< HEAD


=======
>>>>>>> origin/master1
