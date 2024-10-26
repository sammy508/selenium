
# How to download file using selenium

from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.service import Service
import time
import os 

location = os.getcwd()  # it gives the location of the current working directory


def chrome_setup():
    
    # Download file in desired locations
    prefrences = {"download.default_directory":location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",prefrences)

    driver = webdriver.Chrome()
    return driver

driver = chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/")
driver.maximize_window()

driver.find_element(By.XPATH, "//*[@id='table-files']/tbody/tr[1]/td[3]/a")

time.sleep(5)
driver.quit()

