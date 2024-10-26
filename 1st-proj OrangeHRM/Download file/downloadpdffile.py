

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.service import Service
import time
import os 

driver = webdriver.Chrome()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driver.maximize_window()

time.sleep(3)

btnlink = "//*[@id='table-files']/tbody/tr[1]/td[5]/a"

driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/main[1]/section[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[5]/a[1]").click()

time.sleep(9)

driver.quit()
