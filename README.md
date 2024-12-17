# AUT_Guru_Bank_Project

README: Selenium Login Automation Script
This README will guide you through the steps required to understand and run the provided Selenium-based automation script. The script is designed to perform an automated login operation on the demo Guru99 website using a specified user ID and password.

1. Introduction
This script automates the process of logging into the demo Guru99 banking website using Selenium WebDriver with the Firefox browser. It performs the following actions:

Opens the website.
Inputs a valid user ID and password.
Submits the login form.
Prints the success or failure message based on the outcome.
2. Prerequisites
Before running the script, ensure the following prerequisites are in place:

Python 3.x installed on your machine.
Selenium WebDriver installed via pip. You can install it using the following command:
bash
pip install selenium
Firefox browser installed (as the script uses the Firefox WebDriver).
Geckodriver installed (this is the WebDriver for Firefox). Ensure it is available in your system's PATH. Download it from here.
3. Setup Instructions
Install the Required Python Libraries
The script requires the selenium library. You can install it using pip:

bash
pip install selenium
Ensure Firefox and Geckodriver Are Installed

Make sure you have Firefox installed.
Download Geckodriver, and ensure it is added to your system's PATH.
Download or Clone the Script
Ensure you have a copy of the script on your machine.

4. Script Overview
The provided Python script performs the following tasks:

Initialization of WebDriver:
The webdriver.Firefox() command initializes the WebDriver, allowing you to interact with the Firefox browser.

python

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.demo.guru99.com/V4/")
Implicit Wait:
The script waits for elements to load before interacting with them:

python
driver.implicitly_wait(5)
Login Function (valid_user_id):

Locates the uid (user ID) and password input fields by their name attributes.
Enters the predefined user ID (mngr604408) and password (gYnaqAm).
Submits the login form by clicking the submit button using the btnLogin attribute.
Prints a message based on whether the login was successful or not.
python

email_input = driver.find_element(by=By.NAME, value="uid")
email_input.send_keys("mngr604408")
password_input = driver.find_element(by=By.NAME, value="password")
password_input.send_keys("gYnaqAm")
submit_login = driver.find_element(by=By.NAME, value="btnLogin")
submit_login.click()
Closing the Browser:
The script waits for 10 seconds after the login attempt and then closes the browser.

python

time.sleep(10)
driver.quit()
5. Running the Script
To run the script:

Save the script to a .py file (e.g., selenium_login.py).
Open a terminal or command prompt in the directory where the script is saved.
Execute the script by running:
bash

python selenium_login.py
6. Troubleshooting
Geckodriver issues: Ensure that Geckodriver is installed and added to your system's PATH. You can check if it's accessible by running the following command in your terminal:

bash

geckodriver --version
If Geckodriver isn't installed, download it from the official page.

Element Not Found:
If the script fails to locate elements (e.g., uid, password, or btnLogin), ensure the web elements have not changed. You can inspect the page using the browser's developer tools (right-click > Inspect) to check if the element locators (like name) are still valid.

Browser Version Compatibility:
Ensure the version of Firefox you are using is compatible with the version of Geckodriver. Sometimes, mismatches can cause issues.

Conclusion
This script automates the login process on the demo Guru99 website using Selenium WebDriver and Firefox. By following this README, you should be able to set up, run the script, and troubleshoot common issues.
