from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
time.sleep(6)

alertwindow = driver.switch_to.alert
print(alertwindow.text)

alertwindow.send_keys(" I am practicing selenium")
alertwindow.accept()   # to click on ok button

# alertwindow.dismiss() # to click on cancel button on alert
time.sleep(5)
driver.quit()


