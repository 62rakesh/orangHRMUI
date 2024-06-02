import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.locators import Locators


class LoginPage:
    def __init__(self, driver):
        # driver = webdriver.Chrome()
        self.driver = driver

    def enter_username(self, name):
        print("username verification is started")
        self.driver.find_element(By.XPATH, Locators().loginPage_locator()["username_xpath"]).click()
        self.driver.find_element(By.XPATH, Locators().loginPage_locator()["username_xpath"]).send_keys(name)

    def enter_password(self, pwd):
        print("password verification is started")
        self.driver.find_element(By.XPATH, Locators().loginPage_locator()["password_xpath"]).click()
        self.driver.find_element(By.XPATH, Locators().loginPage_locator()["password_xpath"]).send_keys(pwd)

    def click_loginBtn(self):
        print("login button verification is started")
        self.driver.find_element(By.XPATH, Locators().loginPage_locator()["loginBtn_xpath"]).click()

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

    def switchingTab(self):
        # get_parentPage_title = self.driver.find_element(By.XPATH,Locators().loginPage_locator()["helpButton"])
        title = self.driver.title
        print(f"parent page title is {title}")
        parent_window = self.driver.current_window_handle
        helpPage = self.driver.find_element(By.XPATH, Locators().loginPage_locator()["helpButton"])
        helpPage.click()
        time.sleep(2)
        childWindow = self.driver.window_handles
        for window in childWindow:
            print(window)
            if window != parent_window:
                self.driver.switch_to.window(window)
                childTitle = self.driver.title
                print(f"title of the child page is {childTitle}")
                self.driver.find_element(By.XPATH, "(//SPAN[contains(text(),'Admin User Guide')])").click()
                time.sleep(2)
                self.driver.close()
                time.sleep(3)
            break
        # self.driver.switch_to.window(parent_window)
        time.sleep(2)






