from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.vinsguru.com/selenium-webdriver-automating-hoverable-multilevel-dropdowns/")
driver.maximize_window()

time.sleep(3)
architect = driver.find_element(By.XPATH, "//span[normalize-space()='Architecture']")
designpattrn = driver.find_element(By.XPATH, "//span[normalize-space()='Design Pattern']")


# Mouse Hover action
# to do mouse action we have to create action chains object first

action = ActionChains(driver= driver)
time.sleep(2)
action.move_to_element(architect).move_to_element(designpattrn).click().perform()
time.sleep(9)

driver.quit()