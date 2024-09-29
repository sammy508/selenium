# selenium_with_python
here i will explore selenium with python

Web Driver  :<b>
. one of the component in selenium 
. it is a module
. web driver is an API
![image](https://github.com/user-attachments/assets/9a917400-7df5-403a-b56d-cf78c3fd174a)
.: 3 layer architecture of an web application

# Web driver Architecture <b>
- web driver contains so many classes and methods. By calling those methods we are able to interact with browser and these action are perfomed under APPLICATION. That's why Web driver is called API.
- ![image](https://github.com/user-attachments/assets/f7971860-03e6-4e67-b664-98eb30cf01b2)
- Architecture of selenium and it shows how selenium webdriver works
- Selenium Language binding ---> Json wire protocol -->Browser Driver -->W3C --> Browser

- Browser specific driver talk to browser using protocal calles W3C protocol. W3C stands for  **World Wide Web Consortium** and evry web have to follow this standard  protocol
- 
. **Selenium 4 Architecture** <b>
   ![image](https://github.com/user-attachments/assets/6f559cec-cdb0-4d4d-8dbe-9051a7f0c014)
- they updated the json protocol to w3c protocol
-  Selenium Language binding ---> W3c -->Browser Driver -->W3C --> Browser

-  **Setup an dconfiguration Selenium in Vscode** <b>
-  Pre -requisites:
-  python 3
-  Vscode
-  1. Browser driver for chrome (https://chromedriver.chromium.org/downloads)
   2. Browser driver for edge (https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

  And webdriver version should be compatible with your web browser version
  3. Just open vscode terminal and enter this cmnd to install selenium on your Ide
   - pip install selenium

. **Test Case**  <b>
-Open web browser (chrome/edge/firefox)
-Open url https://admin-demo.nopcommerce.com.login
-provide Email (admin@yourstore.com)
- provide password (admin)
- click Login
- Capture title of the Dashboard page. (Actual title)
- verify title of the page : "OrangeHRM" (expected)
- Close Browser
  




