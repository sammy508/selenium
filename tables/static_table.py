from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Counting total header and toal columns in table

row_no = driver.find_elements(By.XPATH, """//*[@id="HTML1"]/div[1]/table//tr """)
row = (len(row_no))

column_no = driver.find_elements(By.XPATH,""" //*[@id="HTML1"]/div[1]/table/tbody/tr/th""")
col =(len(column_no))



# Read specific row and column data in table
data = driver.find_element(By.XPATH,""" //*[@id="HTML1"]/div[1]/table//tr[5]/td[1] """).text
print(data)

# Read all the rows and columns from table\

for r in range(2,row+1):

    for c in range(1, col + 1):
   
     data=   driver.find_element(By.XPATH, " //*[@id='HTML1']/div[1]/table//tr["+str(r)+"]/td["+str(c)+"]").text    # it called dynamic xpath or a 
     print(data, end="   ")  # end gives the space between two item and print it on tabular form
    print() 


# Read data based on condition

for r in range(2,row+1):

    auth_name =   driver.find_element(By.XPATH, " //*[@id='HTML1']/div[1]/table//tr["+str(r)+"]/td[2]").text   
    if auth_name == "Mukesh":
       book_name =   driver.find_element(By.XPATH, " //*[@id='HTML1']/div[1]/table//tr["+str(r)+"]/td[1]").text
       price =   driver.find_element(By.XPATH, " //*[@id='HTML1']/div[1]/table//tr["+str(r)+"]/td[4]").text
       print(book_name,":", " ", price)
 # output
#  Learn Java : Mukesh price
# Master In Selenium : Mukesh  price