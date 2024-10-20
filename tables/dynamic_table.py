from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(3)
username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
username.send_keys("Admin")

passw = driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
time.sleep(5)
driver.find_element(By.XPATH, "//span[normalize-space()='User Management']").click()

time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li").click()
time.sleep(5)

rows = len(driver.find_elements(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div"))
# print(f"total num of users : {(rows)}")

time.sleep(5)

count = 0
for r in range(rows):
    status = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div['+str(r)+']/div/div[5]").text

    if status== "Enabled":
        count+=1

time.sleep(10)
print(f"Total enabled user are {count}")
print(f"Total disabled user are {rows -count}")
driver.quit()

