#Uses Selenium to log in to page, navigate to page behind login, and get innerHTML
from selenium import webdriver


browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
url = "http://example.com/login.php"
browser.get(url) #navigate to the page

username = browser.find_element_by_id("username_id") #username form field
password = browser.find_element_by_id("password_id") #password form field

username.send_keys("my_username")
password.send_keys("my_password")

submitButton = browser.find_element_by_id("submit_button_id") 
button.click() 

browser.get("http://example.com/page.php") #navigate to page behind login
innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string

print(innerHTML)
