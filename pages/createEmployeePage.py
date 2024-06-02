import time
from selenium.webdriver.common.by import By
from selenium import webdriver


class createNewEmp:
    emp_locator = {
        "PIM_navigation_xpath": "(//LI[@class='oxd-main-menu-item-wrapper'])[position()=2]",
        "addEmp_xpath": "(//A[contains(text(),'Add Employee')])",
        "emp_firstName_xpath": "(//INPUT[@placeholder='First Name'])",
        "emp_middleName_xpath": "(//INPUT[@placeholder='Middle Name'])",
        "emp_lastName_xpath": "(//INPUT[@placeholder='Last Name'])",
        "empID_xpath": "(//INPUT[@class='oxd-input oxd-input--active'])[2]",
        "create_logindetails_xpath": "(//SPAN[@class='oxd-switch-input oxd-switch-input--active --label-right'])",
        "userName_xpath": "(//INPUT[@class='oxd-input oxd-input--active'])[3]",
    }

    def __init__(self, driver):
        # driver = webdriver.Chrome()
        self.driver = driver

    def navigate_to_PIM_page(self):
        self.driver.find_element(By.XPATH, self.emp_locator["PIM_navigation_xpath"]).click()
        time.sleep(5)
        print("navigate to the PIM page")

    def click_add_emp_Btn(self):
        self.driver.find_element(By.XPATH, self.emp_locator["addEmp_xpath"]).click()
        print("add employee button ")
        time.sleep(3)

    def create_employeeName(self, fname, mName, lName):
        fullName = fname + mName + lName
        self.driver.find_element(By.XPATH, self.emp_locator["emp_firstName_xpath"]).send_keys(fname)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.emp_locator["emp_middleName_xpath"]).send_keys(mName)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.emp_locator["emp_lastName_xpath"]).send_keys(lName)
        time.sleep(1)
        return fullName

    def enter_empID(self, id):
        emp_ID = self.driver.find_element(By.XPATH, self.emp_locator["empID_xpath"])
        emp_ID.click()
        time.sleep(3)
        emp_ID.clear()
        emp_ID.send_keys(id)
        time.sleep(3)
        print(f"employee id is: {id}")
        return id

    def enable_loginDetails(self):
        self.driver.find_element(By.XPATH, self.emp_locator["create_logindetails_xpath"]).click()
        time.sleep(3)
        print("enable the toggle to create employee login details")

    def create_user_Name(self, Uname):
        U_name = self.driver.find_element(By.XPATH, self.emp_locator["userName_xpath"])
        U_name.send_keys(Uname)
        print(f"employee username is: {Uname}")
        time.sleep(3)
        return Uname


