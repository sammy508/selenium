# selenium_with_python
here i will explore selenium with python

**Web Driver**  :<br>

. one of the component in selenium 
. it is a module
. web driver is an API
![image](https://github.com/user-attachments/assets/9a917400-7df5-403a-b56d-cf78c3fd174a)
.: 3 layer architecture of an web application

# Web driver Architecture <br>

- web driver contains so many classes and methods. By calling those methods we are able to interact with browser and these action are perfomed under APPLICATION. That's why Web driver is called API.
- ![image](https://github.com/user-attachments/assets/f7971860-03e6-4e67-b664-98eb30cf01b2)
- Architecture of selenium and it shows how selenium webdriver works
- Selenium Language binding ---> Json wire protocol -->Browser Driver -->W3C --> Browser

- Browser specific driver talk to browser using protocal calles W3C protocol. W3C stands for  **World Wide Web Consortium** and evry web have to follow this standard  protocol
- 
. **Selenium 4 Architecture** <br>

   ![image](https://github.com/user-attachments/assets/6f559cec-cdb0-4d4d-8dbe-9051a7f0c014)
  
- they updated the json protocol to w3c protocol
-  Selenium Language binding ---> W3c -->Browser Driver -->W3C --> Browser

-  **Setup an dconfiguration Selenium in Vscode** <br>

-  Pre -requisites:
-  python 3
-  Vscode
-  1. Browser driver for chrome (https://chromedriver.chromium.org/downloads)
   2. Browser driver for edge (https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

  And webdriver version should be compatible with your web browser version
  3. Just open vscode terminal and enter this cmnd to install selenium on your Ide
   - pip install selenium

**Test Case**  <br>

-Open web browser (chrome/edge/firefox)
-Open url https://admin-demo.nopcommerce.com.login
-provide Email (admin@yourstore.com)
- provide password (admin)
- click Login
- Capture title of the Dashboard page. (Actual title)
- verify title of the page : "OrangeHRM" (expected)
- Close Browser

  **Locators** <br>
  --> WHAT ARE LOCATORS? 
    - Locators are methods that are used to locate HTML web elements for 
      Selenium browser driver.
      
--> WHAT IT IS USED FOR? 
    - It is used to locate any specific web element 
    on the UI of AUT (application under test)
    <br>
    ![alt text](Web-Element-Locators-Explained-By-Louise-J-Gibbs.png)
    <br>

 **Types of locators** <br>
 ![image](https://github.com/user-attachments/assets/85e2629d-d80e-4a30-8315-21f75e13f7b5)  <br>

 **Id**: <br>
 my_element = driver.find_element(By.ID, 'Search box').send_keys("Sammy508")  <br>

 **Name**  <br>
 my_element = driver.find_element(By.Name, 'Submit_Search ').click()  <br>
 instead use this approach  <br>
 password_element = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_element.send_keys("admin123")   <br>

 
 **Link Text / Partial link text** <br>
 ![image](https://github.com/user-attachments/assets/38548c07-2129-4e39-a5fe-7066ab9a9b29) <br>

 Most of the time these Locators are mostly used in single web pages  <br>
 . **Id** <br>
 . **Name** <br>
 . **Linktext** <br>
 . **partial Linktext**  <br>
 
 Sometimes we need to find out More than 1 elements in that case we use  these locators like  <br>
 . **Classname** <br>
 eg:  slider = driver.find_elements(By.CLASS_NAME, "homeslider-Container") <br>
print(len(slider)) <br> 
 ![image](https://github.com/user-attachments/assets/c05048ab-0f35-46f4-84f2-038359755d33) <br>

 . **Tagname** <br>

 Eg:   links = driver.find_elements(By.TAG_NAME, "a") <br>
 print(len(links))
 

 **By. CLASS_NAME**
 
   driver.get("http://www.automationpractice.pl/index.php")

   sliders = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "homeslider-container")))
   print(len(sliders))

**CSS Selectors**
We can address css selectors by <br>
1. tag and ID    (tagname#ID)<br>
2. tag and class   (tagname.class) <br>
3. tag and attribute   (tagname[attribut = value])<br>
4. tag class and attribute   (tagname.class[attribute= value]) <br>

<br>
**Xpath** <br>
- Xpath are defined as Xml path  <br>
-It uses HTML DoM Structure to locate elemnt on web page <br>
-Its an address of an elemnt  <br>
**Types** of xpath  : <br>
.Relative Xpath  <br>
.Absolute Xpath  <br>







 
 

  




