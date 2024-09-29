
# I am learnign to test and automate on selenium and want to explore more 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait = WebDriverWait(driver,10)  # it waits 10 sec to load
wait.until(EC.presence_of_element_located((By.NAME,"username"))).send_keys ("Admin")

wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")

wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title :
    print("Login test Passed")
else:
    print("Login test Failed")

time.sleep(15)
driver.close()  


