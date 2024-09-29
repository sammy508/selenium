from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def startbot(username, password, url):
    # Initialize the WebDriver using ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())

    try:
        # Open the specified URL
        driver.get(url)

        # Wait for the username field to be present and enter the username
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_field.send_keys(username)

        # Wait for the password field to be present and enter the password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(password)

        # Wait for the login button to be clickable and click it
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        login_button.click()

    except TimeoutException:
        print("An element took too long to load. Please check the website structure or your connection.")
    finally:
        # Optional: close the driver after a delay or keep it open
        # driver.quit()
        pass

# Define your credentials and URL
username = "codesammy1000@gmail.com"
password = "D!lk$@mU01221"
url = "https://www.reddit.com/login/"

# Start the bot with the given credentials and URL
startbot(username, password, url)
