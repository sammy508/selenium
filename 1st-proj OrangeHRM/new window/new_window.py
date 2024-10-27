

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# driver.switch_to.new_window('window')  # It loads another application on new tab
driver.switch_to.new_window('tab')  # it loads another application on new tab
driver.get("https://www.nopcommerce.com/en/demo")
time.sleep(5)

driver.quit()
