
# Application / web Browser commands

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()
driver.get('https://www.nopcommerce.com/en/demo')

print(driver.title)  # to capture title of current webpage

print(driver.current_url)
# print(driver.page_source)

driver.quit()