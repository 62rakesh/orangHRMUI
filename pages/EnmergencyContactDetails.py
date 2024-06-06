import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from pynput.keyboard import Key, Controller


class emergencyContact:
    logs = LogGen.generateLog()
    contact_locators = {
        "myInfo_xpath": "(//SPAN[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[position()=6]",
        "emergencyContact_xpath": "(//A[contains(text(),'Emergency Contacts')])",
        "emergencyContactAdd_Btn_xpath": "(//BUTTON[@class='oxd-button oxd-button--medium oxd-button--text'])[1]",
        "attachmentAdd_Btn_xpath": "(//BUTTON[@class='oxd-button oxd-button--medium oxd-button--text'])[2]",
        "name_xpath": "(//INPUT[@class='oxd-input oxd-input--active'])[2]",
        "relationship_xpath": "(//INPUT[@class='oxd-input oxd-input--active'])[2]",
        "mobileNo_xpath": "(//INPUT[@class='oxd-input oxd-input--active'])[4]",
        "saveBtn_xpath": "(//BUTTON[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'])[1]",
        "browseBtn_xpath": "(//I[@class='oxd-icon bi-upload oxd-file-input-icon'])",
    }

    def __init__(self, driver):
        # driver = webdriver.Chrome()
        self.driver = driver

    def navigate_to_myInfo_page(self):
        self.logs.info("user profile verification started")
        self.driver.find_element(By.XPATH, self.contact_locators["myInfo_xpath"]).click()
        time.sleep(2)
        self.logs.info("user navigates to the my profile page")

    def emergencyContact_verification(self):
        self.logs.info("emergency contact verification is started")
        self.driver.find_element(By.XPATH, self.contact_locators["emergencyContact_xpath"]).click()
        time.sleep(2)
        self.logs.info("user navigates to the emergency contact tab")

    def addEmenrgecyContactUserDetails(self, name, relation, mNo):
        self.logs.info("add emergency contact information")
        self.driver.find_element(By.XPATH, self.contact_locators["emergencyContactAdd_Btn_xpath"]).click()
        time.sleep(1)
        self.logs.info("click on the add button")
        self.driver.find_element(By.XPATH, self.contact_locators["name_xpath"]).send_keys(name)
        self.logs.info(f"emergency contact person name is: {name}")
        self.driver.find_element(By.XPATH, self.contact_locators["relationship_xpath"]).send_keys(relation)
        time.sleep(1)
        self.logs.info(f"relation is {relation}")
        self.driver.find_element(By.XPATH, self.contact_locators["mobileNo_xpath"]).send_keys(mNo)
        self.logs.info(f"Emergency contact number is {mNo}")
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.contact_locators["saveBtn_xpath"]).click()
        time.sleep(2)

    def upload_emergencyContact_details(self):
        self.logs.info("upload an attachment of emergency contact details")
        self.driver.find_element(By.XPATH, self.contact_locators["attachmentAdd_Btn_xpath"]).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.contact_locators["browseBtn_xpath"]).click()
        time.sleep(3)
        keyboard = Controller()
        keyboard.type("C:\\Users\\Rakesh\\OneDrive\\Documents\\login_details.xlsx")
        keyboard.press(Key.enter)
        time.sleep(1)
        keyboard.release(Key.enter)
        time.sleep(2)
        self.logs.info("file uploaded successfully")
        self.driver.find_element(By.XPATH, self.contact_locators["saveBtn_xpath"]).click()
        time.sleep(2)
