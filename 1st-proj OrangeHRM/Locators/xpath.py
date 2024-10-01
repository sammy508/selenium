from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


## Relative and absolute xpath

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://www.daraz.com.np/#?")

search= "hp pavillion laptop"
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='q']"))).send_keys(search)

wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/div/form/div/div[2]/a"))).click()

# path with contains()

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class,'cart-icon-daraz')]"))).click()

#path with strat-with()

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[starts-with(@type,'submit')]"))).click()


# time.sleep(60)
driver.quit()