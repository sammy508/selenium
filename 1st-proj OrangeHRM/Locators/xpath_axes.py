
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://money.rediff.com/bse/daily/groupa")

# self  xpath axes
text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'KFIN Technologies')]/self::a").text
print(text_msg)

# xpath with parents

text_msgparent= driver.find_element(By.XPATH,"//a[contains(text(),'KFIN Technologies')]/parent::h4").text
print(text_msgparent)
# KFIN Technologies  it prints the same value of self because its parent doesnt have any text

# child
text_msgchild= driver.find_elements(By.XPATH,"//a[contains(text(),'KFIN Technologies')]/ancestor::div/ancestor::div")
print(len(text_msgchild))

#ancestor
text_ances= driver.find_elements(By.XPATH,"//a[contains(text(),'KFIN Technologies')]/parent::h4/child::div")
print(len(text_ances))


#desendants node
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'KFIN Technologies')]"))
)

text_dece = driver.find_elements(By.XPATH, "//a[contains(text(),'KFIN Technologies')]/ancestor::div/parent::div/descendant::*")
print(len(text_dece))



#following - sibling
text_foll= driver.find_elements(By.XPATH,"//a[contains(text(),'KFIN Technologies')]/ancestor::div/ancestor::div/following-sibling::div")
print(len(text_foll))


#preceding - sibling
text_pre= driver.find_elements(By.XPATH,"//a[contains(text(),'KFIN Technologies')]/ancestor::div/ancestor::div/preceding-sibling::*")
print(len(text_pre))



driver.quit()

