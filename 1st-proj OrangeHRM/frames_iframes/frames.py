from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()

driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/#google_vignette")
driver.maximize_window()

# Incase of independent frames

driver.switch_to.frame("Id or a Name of frame")
driver.find_element(By.PARTIAL_LINK_TEXT,"any button to click")
driver.switch_to.default_content() #go back to main page

driver.switch_to.frame("Id or a Name of frame")
driver.find_element(By.PARTIAL_LINK_TEXT,"any button to click")
driver.switch_to.default_content() #go back to main page

# if we have to go to any other iframes or frames then we must have to repeat the following process again

driver.quit()