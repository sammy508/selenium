
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import time

driver = webdriver.Chrome()

driver.get("https://www.nopcommerce.com/en/demo")
driver.maximize_window()

# capture cookies from browser
time.sleep(2)
# cookie is a dictonary collection which contains multiple of keys and values

# Add cookies to browser
driver.add_cookie({
    "name":"Nopnewcookie",
    "value": "123456",
    #"expiry": "Nahi he re" 
})
cookies = driver.get_cookies()
print(len(cookies))   # capture all the cookies from browser



# get data from cookies
for cookie in cookies:
    # print(cookie.get('name'))  # by using .get() attribut we can get data of the cookies
    print(f"{cookie.get('name')} :  {cookie.get('value')}")

# Delete specific cookies
driver.delete_cookie("Nopnewcookie")  

# To deldete all the cookies 
# driver.delete_all_cookies()0x

driver.quit()
