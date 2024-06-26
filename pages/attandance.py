import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from utilities.customLogger import LogGen


class Attendance:
    logs = LogGen.generateLog()
    timesheet_locators = {
        "time_xpath": "(//LI[@class='oxd-main-menu-item-wrapper'])[position()=4]",
        "attendanceBtn_xpath": "(//SPAN[contains(text(),'Attendance ')])",
        "attendace_dropdownList_xpath": "(//UL[@class='oxd-dropdown-menu'])",
        "selectAttendanceList_xpath": "(//ul[@class='oxd-dropdown-menu']//li)",
        "punchIN-PunchOut_xpath": "(//A[contains(text(),'Punch In/Out')])",
        "date_xpath": "(//DIV[@class='oxd-input-group oxd-input-field-bottom-space']//following::input)[1]",
        "timeInput_xpath": "(//DIV[@class='oxd-input-group oxd-input-field-bottom-space']//following::input)[2]",
        "InBtn_xpath": "(//BUTTON[@type='submit'])",
    }

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def navigate_to_timeSheetPage(self):
        self.logs.info("user navigates to the timesheet page")
        self.driver.find_element(By.XPATH, self.timesheet_locators["time_xpath"]).click()
        time.sleep(2)
        self.logs.info("user landed on the timesheet page")

    def navigate_to_attendance_page(self):
        self.driver.find_element(By.XPATH, self.timesheet_locators["attendanceBtn_xpath"]).click()
        time.sleep(2)
        self.logs.info("attendance dropdown is showing")
        attendance_list = self.driver.find_elements(By.XPATH,
                                                    self.timesheet_locators["attendace_dropdownList_xpath"])
        for data in attendance_list:
            print(f"attendance dropdown is having below options: {data.text}")

    def validate_punchIn_Page(self):
        self.driver.find_element(By.XPATH, self.timesheet_locators["punchIN-PunchOut_xpath"]).click()
        time.sleep(1)
        self.logs.info("user clicked on the punchIn button and navigates to the Punch In page")
        self.logs.info("select today's date in the date field")
        todayDate = datetime.now()
        # Format the date time object into a string
        current_date = todayDate.strftime("%Y-%m-%d")
        print(f"Today's date is {current_date}")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//DIV[@class='oxd-date-input'])").click()
        time.sleep(1)
        # self.driver.find_element(By.XPATH, "(//DIV[@class='oxd-date-input'])").clear()
        # time.sleep(1)
        self.driver.find_element(By.XPATH, self.timesheet_locators["date_xpath"]).send_keys(current_date)
        time.sleep(2)