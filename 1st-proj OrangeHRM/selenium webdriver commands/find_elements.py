
# Application / web Browser commands

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://www.nopcommerce.com/en/demo")


elements = driver.find_elements(By.XPATH,"//div[@class='footer-upper']//a")

for ele in elements:
    print(ele.text)



 # in case of find_elements() if it doesn't find a elements it doesn't return any exceptions it returns nothing
elem = driver.find_elements(By.LINK_TEXT,"Log")
print(f"elements returned:",{len(elem)})   
# Output = elements returned: {0}

time.sleep(30)

driver.quit()

