from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import requests as request


driver = webdriver.Chrome()

driver.get("https://www.daraz.com.np/#?")
driver.maximize_window()

# finding links
Linktotal = driver.find_elements(By.TAG_NAME,"a")  # or
Links = driver.find_elements(By.XPATH, "//a")
print("Total num of links: ",len(Linktotal))
print("Total num of links: ",len(Links))


# print links name
count = 0
for link in Links:
    print(link.text)
    try:
    # finding broken links
      url = link.get_attribute('href')
    except:
        None  
    res = request.head(url)
    if res.status_code>=400:
        print(url, "Link is broken")
        count+1

    else:
        print(url,"is valid link") 

print("total broken link are : ", count)           
# Click on links  partial_text links
# driver.find_element(By.PARTIAL_LINK_TEXT, 'LOG').click()

driver.quit()


