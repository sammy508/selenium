
# # selenium contains 2 types of wait commands

# # 1. implicit wait()
# # 2. explicit wait()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.implicitly_wait(15)   # it waits each events that perfomes on that code for entire cycle

driver.get("https://www.google.com/")


searchbox = driver.find_element(By.NAME,'q')
searchbox.send_keys("https://github.com/sammy508")
searchbox.submit()

searchbox.send_keys(Keys.RETURN) 

time.sleep(5)

driver.quit()



