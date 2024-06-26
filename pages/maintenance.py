from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from selenium.common.exceptions import NoSuchElementException


class Maintenance:
    logs = LogGen.generateLog()
    recrruitment_locator = {
        "recruitment_tab_xpath" : "(//LI[@class='oxd-main-menu-item-wrapper'])[position()=10]",
        "title_xpath": "(//H6[@class='oxd-text oxd-text--h6 orangehrm-admin-access-title'])",
        "password_xpath": "(//DIV[@class='oxd-input-group oxd-input-field-bottom-space'])//following::input[@name='password']",
        "submitBtn_xpath": "//BUTTON[@type='submit']",
        "accessRecords_xpath": "(//A[contains(text(),'Access Records')])",
        "employeeName_xpath": "//INPUT[@data-v-75e744cd='']",
        "select_empName_xpath": "(//SPAN[contains(text(),'Virat ')])",
        "search_btn_xpath": "(//BUTTON[@type='submit'])",
        "employee_details_xpath": "(//DIV[@class='orangehrm-card-container'])[2]",
    }

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def verify_user(self, pwd):
        self.logs.info("verifying user credentials for maintaining record")
        self.driver.find_element(By.XPATH, self.recrruitment_locator["recruitment_tab_xpath"]).click()
        time.sleep(2)
        self.logs.info("user navigates to verify user credentials")
        title = self.driver.find_element(By.XPATH, self.recrruitment_locator["title_xpath"]).text
        expected_title = "Administrator Access"
        if title == expected_title:
            print(f"title of the popup is {title}")
            assert title == expected_title
            try:
                self.driver.find_element(By.XPATH, self.recrruitment_locator["password_xpath"]).click()
                self.driver.find_element(By.XPATH, self.recrruitment_locator["password_xpath"]).send_keys(pwd)
                self.logs.info("user enter the password to verify the user credentials")
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.recrruitment_locator["submitBtn_xpath"]).click()
                self.logs.info("user clicked on the confirm button to ensure user is validated successfully")
                time.sleep(3)
            except NoSuchElementException:
                time.sleep(3)
        else:
            print("No title found")

    def verify_user_access_records(self, empName):
        self.logs.info("verify the user records")
        self.driver.find_element(By.XPATH, self.recrruitment_locator["accessRecords_xpath"]).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.recrruitment_locator["employeeName_xpath"]).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.recrruitment_locator["employeeName_xpath"]).send_keys(empName)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.recrruitment_locator["select_empName_xpath"]).click()
        self.logs.info("user enter the employee name that they want to access the records")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.recrruitment_locator["search_btn_xpath"]).click()
        time.sleep(1)
        self.logs.info("user clicked on the search button")
        employee_data = self.driver.find_elements(By.XPATH, self.recrruitment_locator["employee_details_xpath"])
        for data in employee_data:
            print(f"Title of the employee records are:- ", end="")
            print(data.text)
        time.sleep(3)







