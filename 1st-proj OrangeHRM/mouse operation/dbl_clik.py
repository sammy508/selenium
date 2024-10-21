
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")

driver.maximize_window()

name =driver.find_element(By.XPATH, "//input[@id='name']")
name.clear() # to clear input field if there were any dommy data or text 
name.send_keys("Sammy")

action = ActionChains(driver=driver)
action.double_click(name)