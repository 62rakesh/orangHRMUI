import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.customLogger import LogGen


class recruitment:
    logs = LogGen.generateLog()
    recruit_locators = {
        "recruitment_xpath": "(//LI[@class='oxd-main-menu-item-wrapper'])[position()=5]",
        "vacancies_xpath": "(//A[contains(text(),'Vacancies')])",
        "table_xpath": "(//DIV[@class='oxd-table orangehrm-vacancy-list'])",
        "jobTitle_xpath": "(//DIV[@class='oxd-table orangehrm-vacancy-list'])//div[@class='oxd-table-header-cell oxd-padding-cell oxd-table-th'][position()=3]",
    }

    def __init__(self, driver):
        # driver = webdriver.Chrome()
        self.driver = driver

    def recruitment_page_validation(self):
        self.logs.info("recruitment page navigation is started")
        self.driver.find_element(By.XPATH, self.recruit_locators["recruitment_xpath"]).click()
        time.sleep(2)
        self.logs.info("user navigates to the recruitment page")
        self.logs.info("select the vacancies tab")
        self.driver.find_element(By.XPATH, self.recruit_locators["vacancies_xpath"]).click()
        time.sleep(2)
        table = self.driver.find_element(By.XPATH,self.recruit_locators["table_xpath"])
        table_data = ""
        if table.is_displayed():
            self.logs.info("the job title is displayed")
            table_text = table.text
            table_data += table_text
        print(f"table data is {table_data}")
        self.logs.info(f"table data is {table_data}")
        time.sleep(5)




