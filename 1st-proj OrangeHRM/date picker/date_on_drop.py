
# select a date on a drop down button

from selenium import webdriver
from selenium. webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

driver.get("https://bookonwardticket.com/dummy-ticket/?gad_source=1&gclid=Cj0KCQjwsc24BhDPARIsAFXqAB0luAWhAfCQO7ehHm_GkHOtXE6iIkcLV5AyDDGUPepNj96_7g2Ez8AaAm-bEALw_wcB")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='dummy-departure-date']").click()

time.sleep(3)
month = Select(driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/select[1]"))
mon = month.select_by_visible_text("Dec")
print(mon)

time.sleep(4)
#year
year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
yr = year.select_by_visible_text("2025")
print(yr)
time.sleep(5)

days = driver.find_elements(By.XPATH, "//tbody/tr/td")

for day in days:
  if  day.text == "22":
    day.click()
    print(day.text)
    break
time.sleep(4)  




