# standard date picker
from selenium import webdriver
from selenium. webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)
time.sleep(4)


# Approach 1 by directly passing date through send keys

# date = "05/10/2024"
# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys(date)
# time.sleep(10)

# Approach 2

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

month = "March"
year = "2022"
day = "25"

while True:
    mont = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr =  driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mont==month and yr==year:
        break

    else:
        # driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()  # future date
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()  # previous dates

dates = driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td")

for ele in dates:

    if  ele.text== day:
        ele.click()
        print(ele.text)
        break