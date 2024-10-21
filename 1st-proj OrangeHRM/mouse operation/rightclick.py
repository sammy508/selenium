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

action = ActionChains(driver=driver)
action.context_click(architect).perform()
time.sleep(4)

driver.quit()