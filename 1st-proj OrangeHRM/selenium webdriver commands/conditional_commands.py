
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get('https://opcr.nepalpolice.gov.np/#/register')


check = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='I am Nepali']")))
check.click()

next =  WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']")))
next.click()

 

print("status",check.is_selected)
print("status",next)

email_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='First Name']"))
    )
email_input.click()

print("status :",email_input.is_displayed())
print("status",email_input.is_enabled())

driver.save_screenshot('screenshot.png')
driver.quit()





