
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# explixit driver works under certain conditions
# it takes 2 arguments (driver, time) driver instance and time
#

driver = webdriver.Chrome()

# also contain poll frequency Poll_frequency = 2 means it again research after 2 seconds of time until it reaches to given time
wait = WebDriverWait(driver, 10, ignored_exceptions=[NoSuchElementException]) 

driver.get('https://opcr.nepalpolice.gov.np/#/register')


check = wait.until(
    EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='I am Nepali']"))).click


driver.quit()


