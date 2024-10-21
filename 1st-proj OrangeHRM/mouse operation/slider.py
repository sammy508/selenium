
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/jquerymobile/tryit.asp?filename=tryjqmob_forms_slider_range")

driver.maximize_window()
time.sleep(2)

frame = driver.find_elements(By.XPATH,"//iframe[@id='iframeResult']")
driver.switch_to.frame(frame)

form = driver.find_element(By.XPATH, "//form[@method='post']")
driver.switch_to.frame(form)

min_val =driver.find_element(By.XPATH, "//a[@title='200']")
max = driver.find_element(By.XPATH, "//a[@title='800']")
time.sleep(2)
print(min_val.location)
print(max.location)


# action
action = ActionChains(driver=driver)
action.drag_and_drop_by_offset(min_val,100,0).perform()  # (self=min, x=100, y=0) it takes values on x axis and y axis
action.drag_and_drop_by_offset(max,-50, 0).perform()