
# # How to download file using selenium

# from telnetlib import EC
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.service import Service
# import time
# import os 

# location = os.getcwd()  # it gives the location of the current working directory


# def chrome_setup():
    
#     # Download file in desired locations
#     prefrences = {"download.default_directory":location}
#     ops = webdriver.ChromeOptions()
#     ops.add_experimental_option("prefs",prefrences)

#     driver = webdriver.Chrome()
#     return driver

# driver = chrome_setup()
# driver.get("https://file-examples.com/index.php/sample-documents-download/")
# driver.maximize_window()

# driver.find_element(By.XPATH, "//*[@id='table-files']/tbody/tr[1]/td[3]/a")

# time.sleep(5)
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

location = os.getcwd()  # Current working directory

def chrome_setup():
    # Download file in desired location
    preferences = {
        "download.default_directory": location,
        "download.prompt_for_download": False,  # Disable download prompt
        "directory_upgrade": True,  # Allow upgrading the directory
        "safebrowsing.enabled": True  # Enable safe browsing
    }
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(options=options)
    return driver

# For Firefox setup
def firefox_setup():
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveTODisk","application/msword")
    ops.set_preference("browser.download.manager.showWhenStarting",False)
    ops.set_preference("browser.download.folderList",2)  # it specify location 0 = desktop. 1= default dowload, 2= desired location
    ops.set_preference ('browser.download.dir',location)
    driver= webdriver.Firefox(options=ops)
    return driver


driver = chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/")
driver.maximize_window()



# Find and click the download link
download_link = driver.find_element(By.XPATH, "//*[@id='table-files']/tbody/tr[1]/td[3]/a")
download_link.click()

# Wait for the download to complete
time.sleep(10)  # Adjust the sleep time as necessary for larger files

driver.quit()
