from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import excelutils
import time

driver = webdriver.Chrome()


driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()

driver.implicitly_wait(5)

file = r"D:\selenium projects\selenium\1st-proj OrangeHRM\Data driven testing\data_to_drivetest.xlsx"
rows = excelutils.row_count(file, "Sheet 1")

for r in range(2, rows+1):
    princ= excelutils.read_data(file,"Sheet 1", r,1)
    rateof_intrst = excelutils.read_data(file, "Sheet 1",r, 2 )
    per1 = excelutils.read_data(file, "Sheet 1",r, 3)
    per2 = excelutils.read_data(file, "Sheet 1",r,4 )
    freq = excelutils.read_data(file, "Sheet 1",r, 5)
    exp_matu_val = excelutils.read_data(file, "Sheet 1",r, 6)

    # passing data to application

    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(princ)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rateof_intrst)
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)
    time.sleep(2)
    # driver.find_element(By.XPATH,"  //select[@id='tenurePeriod']").click()
    periodrop = Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    periodrop.select_by_visible_text(per2)

    freqdrp = Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    freqdrp.select_by_visible_text(freq)

    driver.find_element(By.XPATH,"//div[@class='cal_div']//a[1]").click()
    actual_val = driver.find_element(By.XPATH, "//*[@id='resp_matval']/strong"  ).text

    if float(exp_matu_val)== float(actual_val):
        print("Test passed")

        excelutils.write_data(file,"Sheet 1",r,8, "passed")
    else:
            print("Test failed")

            excelutils.write_data(file,"Sheet 1",r,8, "failed")

    time.sleep(5)

driver.close()    


# 