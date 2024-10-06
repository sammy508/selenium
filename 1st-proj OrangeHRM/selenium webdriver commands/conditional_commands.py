
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get('https://opcr.nepalpolice.gov.np/#/register')


check = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='I am Nepali']")))

print("statusbefore",check.is_selected())

check.click()
time.sleep(12)

print("statuscheck",check.is_selected())
# print("statuschek",check.is_selected())

next =  WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']")))
next.click()



email_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='First Name']"))
    )
email_input.click()

print("email :",email_input.is_displayed())
print("email",email_input.is_enabled())

driver.save_screenshot('screenshot.png')
driver.quit()





