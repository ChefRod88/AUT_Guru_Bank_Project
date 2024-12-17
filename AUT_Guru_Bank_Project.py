import time
from selenium import webdriver
from selenium.webdriver.common.by import By


#Intialized the webdriver
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.demo.guru99.com/V4/")
driver.implicitly_wait(5)


def valid_user_id():
    try:

        email_input = driver.find_element(by=By.NAME, value="uid") # I located the element by the name
        email_input.send_keys("mngr604408")                        # I entered the username

        password_input = driver.find_element(by=By.NAME, value="password") # I located the element by the name
        password_input.send_keys("gYnaqAm")

        submit_login = driver.find_element(by=By.NAME, value="btnLogin")
        submit_login.click()

        print(f"PASS: Login was successful.")

    except:
        print(f"FAIL: Login was unsuccessful")


valid_user_id() # called the function



time.sleep(30)
driver.quit()


