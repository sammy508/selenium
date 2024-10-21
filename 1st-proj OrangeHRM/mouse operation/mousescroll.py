from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.flagworld.com.au/flags.html?srsltid=AfmBOorNPEm1bWodSaXcAkZgsky-Vp5RcYm-L8IskwvGU6_RFDRE_4EP")
driver.maximize_window()
time.sleep(3)

# scroll down by pixel
# driver.execute_script("windows.scrollBy(0,3000)", "")
# value = driver.execute_script("return window.pageYoffset;")
# print("Total pixel moved:",value)

# scroll page till the element is visible
flag = driver.find_element(By.XPATH, "//img[@alt='Sporting Flag of Australia']")
time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView(true);", flag)
value = driver.execute_script("return window.pageYOffset;")
print("Num of pixel moved:", value)
time.sleep(5)


# scroll page directly to the end 
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

driver.quit()
