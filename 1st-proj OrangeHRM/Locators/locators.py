

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

wait = WebDriverWait(driver, 15)


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


try:
    username_element = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_element.send_keys("Admin")

#By name
    password_element = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_element.send_keys("admin123")

# BY path
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit_button.click()

  #  By. TAG_NAME

    title = wait.until(EC.presence_of_element_located((By.TAG_NAME, "title")))
    print(title.text)

except Exception as e:
    print(f"An error occurred: {e}")


time.sleep(20)

# Close the browser properly
driver.quit()
