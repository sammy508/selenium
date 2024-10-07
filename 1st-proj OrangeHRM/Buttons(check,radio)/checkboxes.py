from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


driver = webdriver.Chrome()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")


# 1. For specific checkboxes
# checkbox = driver.find_element(By.XPATH, "//label[@for='RESULT_CheckBox-8_0']").click()

# 2. for multiple checkboxes
checkboxes = driver.find_elements(By.XPATH, "//*[@id='q15']/table/tbody/tr[*]" )

# checkboxes = driver.find_elements(By.CSS_SELECTOR, ".inline_grid.choices input[type='checkbox']")

# print(len(checkboxes))
# boxes = [checkboxs]

# # Approach 1
# for i in range(len(checkboxs)):
#     checkboxs[i].click()

# Approach 2

for check in checkboxes:
    try:
    
        if check ==  checkboxes[-1]  or check== checkboxes[-3]:
            check.click()
            time.sleep(2)
    except Exception as e:
        print(f"Error clicking checkbox: {e}")



# Clearing all the selected checkboxes

for check in checkboxes:
   if check.is_selected()==True:
       time.sleep(1)
       check.click()

time.sleep(15)
driver.quit()



