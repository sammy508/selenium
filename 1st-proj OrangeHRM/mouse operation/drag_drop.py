
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()

washington =driver.find_element(By.XPATH, "//div[@id='box3']")
cntry = driver.find_element(By.XPATH, "//div[@id='box103']")

acton = ActionChains(driver=driver)

time.sleep(2)
acton.drag_and_drop(washington, cntry).perform()
time.sleep(4)
driver.quit()