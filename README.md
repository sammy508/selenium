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
****Xpath**** <br>
- Xpath are defined as Xml path  <br>
-It uses HTML DoM Structure to locate elemnt on web page <br>
-Its an address of an elemnt  <br>
**Types** of xpath  : <br>
.Relative Xpath (partial xpath) <br>
      Eg: //*[@id="u_0_9_UA"] (facebbok login button's rel xpath)
.Absolute Xpath (Full xpath) <br>
      Eg : /html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button  (Full xpath)
<br>
**DOM STRUCTURE** : <br>
. Dom is an API interface provided by browser  <br>
. When a web page is loaded, the browser creates a Document Object model of the page <br>

# Difference Between Absolute and Relative Xpath <br>
 1. Absolute path statrts from Root HTML Node
  Relative Xpath directly jumps to element on DOM <br><br>
2. Absolute xpath start with / But Relative xpath starts with //   <br><br>
3. In Absolute xpath we use only tags/ nodes But in Relative xpath we use Attributes <br><br>

  We can use ** **selector HUb extension** **  on browser to capture x path automatically  <br>

** **Reason to Pick relative xpath**  <br>
1. If developer introduce new element then absolute path will be broken
2. If Dev change the location then absolute xpath will be broken S0, we haave to pick relative xpath   <br>
Absolute path are not Stable <br>

**Xpath Options**  <br>

and, or, contains(), start-with(), text()   <br>

 # Xpath with OR operator
 wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='q' or @placeholder = 'search']"))).send_keys(search)

 # xpath with and operator
 
 wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='q' and @placeholder = 'search']"))).send_keys(search)

# path with contains()

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class,'cart-icon-daraz')]"))).click()

# path with strat-with()

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[starts-with(@type,'submit')]"))).click()

# Xpath Axes  
  An axis represents a relationship to the context (current) node, and is used to locate nodes relative to that node on the tree.  <br>
  ![alt text]({5559403E-CDF4-4E86-9D5A-3D0D054BCAB1}.png)  <br>
  


# # self  xpath axes
 text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'KFIN Technologies')]/self::a").text
 print(text_msg)

# # xpath with parents

 text_msgparent= driver.find_element(By.XPATH,"//a[contains(text(),'KFIN Technologies')]/parent::h4").text
 print(text_msgparent)
 KFIN Technologies  it prints the same value of self because its parent doesnt have any text

# child
text_msgchild= driver.find_elements(By.XPATH,"//a[contains(text(),'KFIN Technologies')]/ancestor::div/ancestor::div")
print(len(text_msgchild))

# ancestor
text_ances= driver.find_elements(By.XPATH,"//a[contains(text(),'KFIN Technologies')]/parent::h4/child::div")
print(len(text_ances))


# desendants node

text_dece = driver.find_elements(By.XPATH, "//a[contains(text(),'KFIN Technologies')]/ancestor::div/parent::div/descendant::*")
print(len(text_dece))



# Preceding Sibling
Definition: Selects only sibling nodes that come before the current node at the same level in the hierarchy.

 #preceding - sibling
text_pre= driver.find_elements(By.XPATH,"//a[contains(text(),'KFIN Technologies')]/ancestor::div/ancestor::div/preceding-sibling::*")
print(len(text_pre))

# following sibling

its also like a preceding ones  <br>
#following - sibling
text_foll= driver.find_elements(By.XPATH,"//a[contains(text(),'KFIN Technologies')]/ancestor::div/ancestor::div/following-sibling::div")
print(len(text_foll))

# Selenium WebDriver Commands

What are Selenium WebDriver Commands? <br>
Selenium WebDriver commands are set of functions and method used for controlling or automating the web browser. these command helps developer and tester to write script programmatically using various languages (Java, C#, Python, etc.) to interact with web elements or perform various automation task.

** Types of selenium web driver commands** <br>
1. Application commands  <br> <br
   Application commnds

    --> title (sntx: driver.title) <br>
    --> get() (sntx: driver.get('url)) <br>
   ---> current_url(): (sntx: driver.current_url) <br>
   ---> page_source() : (sntx: driver.pagesource) <br>
            It captures the source code of the web pages (inspect and view source code)
    <br>

2. Conditional commands <br>
     In Selenium with Python, we can use conditional commands to perform different actions based on specific conditions during your web automation tasks.
     These methods belongs to web element and these commmands can access only through web elements not from driver<br>

     1. is_displayed():  (sntx:- )<br>
          . Checks if the element is visible on the page <br>
          . Returns: True if the element is visible; otherwise, it returns False. <br>
          .  Useful for determining if an element can be interacted with (like clicking).

     2. is_enabled():  (sntx: )  <br>
          . Checks if the element is enabled and can be interacted with. <br>
          . Returns True if the element is enabled; otherwise, it returns False. <br>
          .  Commonly used for buttons, input fields, and links to see if they can be clicked or entered. <br><br>

     3. is_selected(): (sntx: )  <br>
           . It is mostly ussed on checkbox and radio button to check the conditions <br>
           . Returns: True if the element is selected; otherwise, it returns False. <br>

   <br>
3. Browser  commands <br>
    1. close()   // kills on once and app still running on memomachine  <br>
    2. quit()    // kills all browser tabs on once and kill properly <br>


4. Navigational commands <br>
    1. back() <br>
    2. forward() <br>
    3. refresh() <br>
    

5. Wait commands <br>

   In Selenium, wait commands are mechanisms used to pause the execution of your test scripts until a certain condition is met, allowing you to interact with web elements reliably  <br>

   There are two types of wait commands<br>

   1. Implicit wait():  <br>
     driver.implicitly_wait(10)<br>
     Implicit Wait is a global wait that is set for the entire duration of the WebDriver instance till the exit/ end of code. <br>

   2. Explicit wait(): <br>
      Explicit Wait allows you to wait for a specific condition to occur before proceeding <br>
      its more flexible tha implicit wait <br>
      it works under condition

** time.sleep()  ** 
   time.sleep() paused the coode for the certain time and it has certain drawbacks: <br>
   
   1. Perfomance of the script is very poor
   2. if the targeted element isn't found in mentioned time then it got exception error

# find_elements():

** text vs get_attribute in selenium **
** "text" **
   Purpose: Retrieves the visible text of an element.
   Usage: This is commonly used when you want to extract text that a user can see on the webpage.
   It return inner text of an elements
  ///** <div id="parent">
    This is the parent text.
    <span>This is the child text.</span>
   </div>  ***//

** get_attribite() **
   Purpose: Retrieves the value of a specified attribute of an element.  <br>
   Usage: Use this when you need to access attributes like href, value, class, or any custom attribute.<br>

   element = driver.find_element(By.ID, "example")  <br>
   attribute_value = element.get_attribute("class")  <br>

** Checkboxes in selenium ** <br>
      Things we can do with checkboxes: <br>
      1. select <br>
      2. unselect <br>


   ** How to locate checkboxes** <br>
   
   # 1. For specific checkboxes
   # checkbox = driver.find_element(By.XPATH, "//label[@for='RESULT_CheckBox-8_0']").click()

   # 2. for multiple checkboxes
   checkboxes = driver.find_elements(By.XPATH, "//*[@id='q15']/table/tbody/tr[*]" )  <br>

   ** To select all checkboxes **  <br>

      for ckeckbox in checkboxs:
       checkbox.click()
  <br>

  # Links in selenium
  ** TYPES ** <br>
      1. Internal Links <br>
          Navigate on another location on same page
      2. External Links <br>
            a hyperlink that leads to a page or resource outside a particular website  <br>
      3. Broken Links <br>
         hyperlinks or URLs on a web page that are not functioning as expected and it doesn't have target are called broken links<br>

   # Dropdown in selenium
   To interact with dropdowns in selenium first we have to import select class <br>
      from selenium.webdriver.support.ui import Select  <br>


   We can identify or select options on multiple ways like: <br>
      1. by visible_text() <br>
      2. by value() <br>
      3. by index() <br>

  ** 1. By visible text() ** <br>
         drpcountry_ele = driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select") <br>
         drpcountry = Select(drpcountry_ele) <br>
         drpcountry.select_by_visible_text("Nepal") <br>

   ** 2. By value() ** <br>
        drpcountry_ele = Select(driver.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select"))<br>
       drpcountry_ele.select_by_value("NPL") <br>
       time.sleep(5) <br>

   ** 2. By index() ** <br>     
         drpcountry_ele = Select(driver.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select")) <br>
         drpcountry_ele.select_by_index(20) <br>
         time.sleep(3) <br>

   # Alerts-popups in selenium

      There are 2 types of alerts.
        1- HTML Alert: Nothing special with this one. 
          You just locate as WebElement then click.   <br>

        2- JS Alert: We cannot locate this web element
           in the HTML code.  <br>
           
        You have to handle it differently
        - We handle alerts using Alert class
         creating ALERT object and 

        - Alert alert = driver.switchTo.alert
         There are 3 options :
        - alert.accept()
        - alert.dismiss()
        - alert.sendKeys()
        
        
   ======================================================        
    - How many different types of JS alerts do we have?
        - 3 types of JS Alerts.
            - Information : You can only accept.
            - Confirmation: You can accept or decline.
            - Prompt    : You can accept, decline, and/or sendKeys.      
         
# Basic Authentication popups

      We cannot pass values by using send_keys like on other alerts beacause it isn't a web elements 
      we have to pass inject  the values directly on url links.  <br>

      Syantax: https://username:password@siteurl.com

# Frames/iframes in selenium

      We can handle frames in Selenium. A frame is an HTML element that keeps a document within another document in a page. HTML has the <frame> or <iframe> tags for embedding a frame inside a document. This method is used to identify a frame with the help of frame id and then switch the focus to that particular frame   

      eg:- 
      driver.switch_to.frame("Id or a Name of frame")  <br>
      driver.find_element(By.PARTIAL_LINK_TEXT,"any button to click")  <br>
      driver.switch_to.default_content() #go back to main page  <br>

# windows Handle in selenium: 
      Selenium can access the another tab using   switch_to.windows_handle   method.  <br>
      # to navigate to next window we use switch_to.window_handles in selenium   <br>
       by using this function we are able to access or control next tab / windows on browser  <br>

       ANd we switch window using windows id and it is given by  indexing  <br>
       parent_window = windowsIDS[0]  <br>

#  Notification alerts/ popups
      We cannot handle it directly by using alert commands because it a browser level popups. Its not even like authentication popups we can't by pass it.
# Basic authentication Popups      
      Authentication popups are types of popups and we cannot switch to them we have to handle it directly by bypassing the authentication value on browser.
      
      driver.get("https://Admin:Admin@the-internet.herokuapp.com/basic_auth")
 
 
# Notification popups
   It appears when we lunch sites and it contains two buttons containing allow and block. we have to click one otherwise we cannot perfom any task on web pages. Its not like a authentication popups we cannot bypass it. We cannot bypass it and we cannot switch to this alert it comes from browser level.TO solve this or handle this we have to disable this alert from browser level for that we need to add some setting to browser level.
   WE add service object at the time of lunching the chrome browser.

   we have a specific types of classes to and this specific class is used to specify the browser level setting and we can disable the popups.
  
   ops = webdriver.ChromeOptions()
   ops.add_argument("--disable-notifications")
   driver = webdriver.Chrome(ops)

# Web Tables
   web tables also called HTML Tables, it is of 2 types:
   1. Static table
       static table consist of same type of data on table and keep unchanged

       data = driver.find_element(By.XPATH,""" //*[@id="HTML1"]/div[1]/table//tr[5]/td[1] """).text
       print(data)

   2. Dynamic table
       Dynamic table contain different type of data and it keeep updating or changeable.

         rows = len(driver.find_elements(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div"))
          print(f"total num of users : {(rows)}")

         time.sleep(5)

         count = 0
         for r in range(rows):
            status = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div['+str(r)+']/div/div[5]").text

            if status== "Enabled":
               count+=1

# Date picker
   The datepicker is tied to a standard form input field. Focus on the input (click, or use the tab key) to open an interactive calendar in a small overlay.

   if the date picker is inside frame 1st we have to switch to frame and perform operation

   Some date pickers allow you to type. In this case we can 
   just use sendKeys method to enter the date we want.

   If that does not work, we need to write our logic 
   for this : 
   1. Click on the field to trigger the date picker
   2. Get the displayed date on the date picker and calculate
      how many times you need to click left/right
      to go to the right month/year. 
   3. Once we go to the correct month/year, select the date.
    
    Date doesn't contains both next future date and previous date at once, its rare we can apply our own logic also

    # date picker also can be on dropdown also
    is also a easy to identify and interact with dropdown
    small eg:
      month = Select(driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/select[1]"))
      mon = month.select_by_visible_text("Dec")
      print(mon)

# Mouse operation in selenium
   We can perform mouseover action in Selenium webdriver in Python by using the ActionChains class. We have to create an object of this class and then apply suitable methods on it.

   Different methods available in mouse operation/ mouse action
   1. Mouse hover
   2. Right click
   3. Double click
   4. Drag and Drop

   # Mouse hover
       We shall use the move_to_element method and pass the element locator as a parameter. Then apply the perform method to actually perform this action. After hovering on the element, we can apply click action on it with the help of the click method.  

       eg:
         architect = driver.find_element(By.XPATH, "//span[normalize-space()='Architecture']")
         designpattrn = driver.find_element(By.XPATH, "//span[normalize-space()='Design Pattern']")

         action = ActionChains(driver= driver)
         action.move_to_element(architect).move_to_element(designpattrn).click().perform()