
## Here is the code to automate login your facebook  account


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

driver.get("https://www.facebook.com")
driver.maximize_window()

# tag and id
email = "Yourgmail@12.com"
driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys(email)
# tag and class
password = "passowrd"
driver.find_element(By.CSS_SELECTOR, "input#pass").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "button._42ft[type=submit]").click()

time.sleep(20)

driver.quit()