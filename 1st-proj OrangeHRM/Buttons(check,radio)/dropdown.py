from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()

driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/#google_vignette")
driver.maximize_window()


# Approach 1

# drpcountry_ele = driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select")
# drpcountry = Select(drpcountry_ele)

# drpcountry.select_by_visible_text("Nepal")
# time.sleep(15)

# Approach 2

drpcountry_ele = Select(driver.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select"))
drpcountry_ele.select_by_index(20)
time.sleep(3)
# Approach 3 
drpcountry_ele = Select(driver.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select"))
drpcountry_ele.select_by_value("NPL")

# deselect value
drpcountry_ele.deselect_by_value("NPL")

time.sleep(5)



# Capture all the options of dropdown

alloption = drpcountry_ele.options
print(len(alloption))

for options in alloption:
    print(options.text)


# select option without using built in function

for option in alloption:
    option.text
    if option.text == "Germany":
        option.click
        break


driver.quit()