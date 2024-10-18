from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# Handling notification popups

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=ops)

driver.get("https://whatmylocation.com/#google_vignette")
driver.maximize_window()
time.sleep(10)

driver.quit()