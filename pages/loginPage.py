import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.locators import Locators
from utilities.customLogger import LogGen

class LoginPage:
    logs = LogGen.generateLog()
    def __init__(self, driver):
        # driver = webdriver.Chrome()
        self.driver = driver

    def enter_username(self, name):
        print("username verification is started")
        self.logs.info("user name verification started")
        self.driver.find_element(By.XPATH, Locators().loginPage_locator()["username_xpath"]).click()
        self.logs.info("user clicked on the username field")
        self.driver.find_element(By.XPATH, Locators().loginPage_locator()["username_xpath"]).send_keys(name)
        self.logs.info("enter the username")

    def enter_password(self, pwd):
        print("password verification is started")
        self.logs.info("password verification is started")
        self.driver.find_element(By.XPATH, Locators().loginPage_locator()["password_xpath"]).click()
        self.driver.find_element(By.XPATH, Locators().loginPage_locator()["password_xpath"]).send_keys(pwd)
        self.logs.info("enter a valid password")

    def click_loginBtn(self):
        print("login button verification is started")
        self.driver.find_element(By.XPATH, Locators().loginPage_locator()["loginBtn_xpath"]).click()
        self.logs.info("click on the login button")

    def handle_window_alert(self):
        print("The window alert verification is started")
        alert = self.driver.switch_to.alert
        print("The alert message has shown up")
        get_alertText = alert.text
        print(f"message on the window alert is: {get_alertText}")
        alert.accept()
        print("accept the warning and click on the 'OK' button")
        time.sleep(2)

    def logout(self):
        print("user-logout verification is started")
        self.driver.find_element(By.XPATH, Locators().loginPage_locator()["account_xpath"]).click()
        time.sleep(2)
        self.logs.info("user clicked on the logout button")
        self.driver.find_element(By.XPATH, Locators().loginPage_locator()["logout_xpath"]).click()
        time.sleep(3)
        print("user is successfully logged out from the dashboard")
        logo = self.driver.find_element(By.XPATH, Locators().loginPage_locator()["comapnyBrandLogo_xpath"])
        if logo.is_displayed():
            text = logo.text
            print("user has successfully logged-out"
                  f"and the logo text is: {text}")
        else:
            print("log-out is not successful")
        self.logs.info("user logged out successfully")

    def switchingTab(self):
        # get_parentPage_title = self.driver.find_element(By.XPATH,Locators().loginPage_locator()["helpButton"])
        title = self.driver.title
        print(f"parent page title is {title}")
        self.logs.info(f"parent page title is {title}")
        parent_window = self.driver.current_window_handle
        helpPage = self.driver.find_element(By.XPATH, Locators().loginPage_locator()["helpButton"])
        helpPage.click()
        self.logs.info("user clicked on the help button")
        time.sleep(2)
        childWindow = self.driver.window_handles
        # self.logs.info(f"child windows are {childWindow}")
        for window in childWindow:
            print(window)
            self.logs.info(f"child windows are {window}")
            if window != parent_window:
                self.driver.switch_to.window(window)
                childTitle = self.driver.title
                print(f"title of the child page is {childTitle}")
                self.logs.info(f"Title of the child window is {childTitle}")
                self.driver.find_element(By.XPATH, "(//SPAN[contains(text(),'Admin User Guide')])").click()
                time.sleep(2)
                self.driver.close()
                self.logs.info("close the child window")
                time.sleep(3)
            break
        self.driver.switch_to.window(parent_window)
        self.logs.info("user navigates to the parent window")
        time.sleep(2)







