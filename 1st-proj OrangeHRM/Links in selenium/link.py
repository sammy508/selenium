from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


driver = webdriver.Chrome()

driver.get("https://www.daraz.com.np/#?")
driver.maximize_window()

# finding links
Links = driver.find_elements(By.XPATH, "//a")
print(len(Links))

# Click on links  partial_text links
driver.find_element(By.PARTIAL_LINK_TEXT, 'LOG').click()

driver.quit()


