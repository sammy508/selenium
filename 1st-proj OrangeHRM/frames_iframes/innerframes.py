

# Switching to default content is not required like on frames or independent frames
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

# outer frame
outerframe = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

# finding inner iframe
innerframe = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

# finding text input box

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("welcomee")

time.sleep(6)

driver.quit()

