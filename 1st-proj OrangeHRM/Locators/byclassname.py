from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

wait = WebDriverWait(driver, 15)


driver.get("http://www.automationpractice.pl/index.php")

sliders = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "homeslider-container")))
print(len(sliders))