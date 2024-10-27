from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import os
driver = webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='select2-billing_country-container']").click()
driver.implicitly_wait(5)

countrieslist = driver.find_elements(By.XPATH,"//*[@id='billing_country']/*")

time.sleep(5)
for country in countrieslist:
    if country.text == "Argentina":
        country.click()
        break

time.sleep(5)

driver.save_screenshot(f"{os.getcwd()}\snapshot.png")  # here it takes directory and file name

driver.quit()