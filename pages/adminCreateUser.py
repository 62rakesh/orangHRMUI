import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.locators import Locators


class createUser:
    adminPage = {
        "adminPage_navigate_xpath": "(//LI[@class='oxd-main-menu-item-wrapper'])[position()=1]",
        "addButton_xpath": "(//BUTTON[@class='oxd-button oxd-button--medium oxd-button--secondary'])",
        "select_user_role_xpath": "(//DIV[contains(text(),'-- Select --')])[position()=1]",
        "select_admin_user_role": "(//SPAN[contains(text(),'Admin')])",
        "employeeName_xpath": "//INPUT[@data-v-75e744cd='']",
        "user_status_xpath": "(//DIV[contains(text(),'-- Select --')])[position()=1]",
        "select_status_xpath": "(//SPAN[contains(text(),'Enabled')])",
        "username_xpath": "(//INPUT[@class='oxd-input oxd-input--active'])[position()=2]",
        "password_xpath": "(//INPUT[@type='password'])[position()=1]",
        "confirmPWD_xpath": "(//INPUT[@type='password'])[position()=2]",
        "saveBtn": "(//BUTTON[@type='submit'])",
        "select_empName_xpath": "(//SPAN[contains(text(),'Virat ')])",
    }

    def __init__(self, driver):
        # driver = webdriver.Chrome()
        self.driver = driver

    def navigate_to_the_adminPage(self):
        time.sleep(2)
        print("navigate to the admin page")
        self.driver.find_element(By.XPATH, self.adminPage["adminPage_navigate_xpath"]).click()
        print("user navigate to the admin/user management page")

    def create_new_user(self):
        time.sleep(2)
        print("create user verification is started")
        self.driver.find_element(By.XPATH, self.adminPage["addButton_xpath"]).click()
        print("user clicked on the add button")
        print("verify a new Add user pop-up is appeared")
        print("select user-role for the new user")
        self.driver.find_element(By.XPATH, self.adminPage["select_user_role_xpath"]).click()
        time.sleep(2)
        script = self.driver.find_element(By.XPATH, self.adminPage["select_admin_user_role"])
        script.click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.adminPage["user_status_xpath"]).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.adminPage["select_status_xpath"]).click()
        time.sleep(2)

    def enter_user_name(self, uName):
        user_name = self.driver.find_element(By.XPATH, self.adminPage["username_xpath"])
        user_name.send_keys(uName)
        time.sleep(4)

    def enter_emp_name(self, empName):
        self.driver.find_element(By.XPATH, self.adminPage["employeeName_xpath"]).click()
        self.driver.find_element(By.XPATH, self.adminPage["employeeName_xpath"]).send_keys(empName)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.adminPage["select_empName_xpath"])
        self.driver.find_element(By.XPATH, self.adminPage["select_empName_xpath"]).click()
        time.sleep(2)

    def create_password(self, password):
        pwd = self.driver.find_element(By.XPATH, self.adminPage["password_xpath"])
        pwd.send_keys(password)
        time.sleep(2)
        cnf_pwd = self.driver.find_element(By.XPATH, self.adminPage["confirmPWD_xpath"])
        cnf_pwd.send_keys(password)
        time.sleep(2)
        return password

    def save_user(self):
        saveUser = self.driver.find_element(By.XPATH, self.adminPage["saveBtn"])
        saveUser.click()
        time.sleep(5)
