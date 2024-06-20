from selenium import webdriver
from selenium.webdriver.common.by import By

def startbot(username, password, url):
    # Correct path to the ChromeDriver
    path = "/home/sammy/Downloads/chromedriver"

    # Initialize the WebDriver
    driver = webdriver.Chrome(path)

    # Open the specified URL
    driver.get(url)

    # Find the username field and enter the username
    driver.find_element(By.NAME, "username").send_keys(username)

    # Find the password field and enter the password
    driver.find_element(By.NAME, "password").send_keys(password)

    # Find the login button and click it
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Define your credentials and URL
username = "codesammy1000@gmail.com"
password = "D!lk$@mU01221"
url = "https://www.reddit.com/login/"

# Start the bot with the given credentials and URL
startbot(username, password, url)
