# test_google_search_firefox.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver for Firefox
driver = webdriver.Firefox()  # Ensure you have GeckoDriver installed
  
try:
    # Open Google
    driver.get("https://www.google.com")

    # Find the search box using its name attribute value
    search_box = driver.find_element(By.NAME, "q")

    # Type "Ryan Gosling" in the search box
    search_box.send_keys("Ryan Gosling")

    # Press Enter to submit the search
    search_box.send_keys(Keys.RETURN)

    # Wait for a few seconds to let the results load
    time.sleep(10)

    # Print the title of the results page
    print(driver.title)

finally:
    # Close the browser
    driver.quit()
