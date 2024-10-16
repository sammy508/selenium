from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

driver.get("https://Admin:Admin@the-internet.herokuapp.com/basic_auth")
time.sleep(5)

driver.quit()
