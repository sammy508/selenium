from selenium import webdriver

def Headless_chrome():
    ops = webdriver.ChromeOptions()
    # ops.headless()# Older approach
    ops.add_argument('--headless')   # new approach after new updated version
    driver = webdriver.Chrome(options=ops)
    return driver

driver = Headless_chrome()
driver.get('https://www.facebook.com/')
print(driver.title)
print(driver.current_url)
driver.quit()