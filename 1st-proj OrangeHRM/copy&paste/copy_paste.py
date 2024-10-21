from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import time

driver = webdriver.Chrome()
driver.get("https://text-compare.com/")
driver.maximize_window()

input1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")


input1.send_keys("Here is the some text to be selected , to practice copy paste on selenium.")
time.sleep(2)

act = ActionChains(driver=driver)

# Select all text om input1 (ctrl+A)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
time.sleep(2)
# copy text (ctrl+c)
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()


input2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

# switch to next text box by pressing tab key
act.send_keys(Keys.TAB).perform()
time.sleep(2)
# paste copied text on input2 (ctrl+v)
input2.click()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(5)



driver.quit()


