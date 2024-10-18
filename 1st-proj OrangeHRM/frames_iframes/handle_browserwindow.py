from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT, "OrangeHRM, Inc").click()

windowsIDS = driver.window_handles

# Approach 1

# parent_window = windowsIDS[0]
# child_window = windowsIDS[1]

# print(parent_window)

# time.sleep(2)
# driver.switch_to.window(child_window)
# print(driver.title)

# driver.switch_to.window(parent_window)
# print(driver.title)

# time.sleep(8)

# Approach 2

for wind in windowsIDS:
    driver.switch_to.window(wind)
    print(driver.title)

    if driver.title == "OrangeHRM":
        driver.close()
        
driver.quit()

# to navigate to next window we use switch_to.window_handles in selenium 
# by using this function we are able to access or control next tab / windows on browser

# ANd we switch window using windows id and it is given by  indexing 
# parent_window = windowsIDS[0]