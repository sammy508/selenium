from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.service import Service
import time
import os 

driver = webdriver.Chrome()
driver.get("https://practice.expandtesting.com/upload")
driver.maximize_window()

time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='fileInput']").send_keys("D:\pyhton projects\todos.txt")
time.sleep(5)

driver.find_element(By.XPATH,"//button[@id='fileSubmit']").click()
time.sleep(9)

driver.quit()


# Most of the times selesnium not recommend to automate to upload and download file operations
