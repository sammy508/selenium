
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get('https://member.daraz.com.np/user/login?spm=a2a0e.tm80335409.header.login.28a379e0mn2fUv')
driver.get('https://www.facebook.com/events/894052652527381/944916830774296/')
driver.back()

driver.forward()

driver.refresh()

driver.quit()