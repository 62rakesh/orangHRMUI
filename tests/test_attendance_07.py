import time
import pytest
from pages.attandance import Attendance
from pages.loginPage import LoginPage
from utilities.readProperties import readConfig


@pytest.mark.usefixtures("setup_teardown")
class TestCheckAttendance:
    @pytest.mark.punch_IN
    def test_punchIN_punchOut(self):
        login = LoginPage(self.driver)
        login.enter_username(readConfig().getuserName())
        login.enter_password(readConfig().getPassword())
        login.click_loginBtn()
        time.sleep(5)
        attendance = Attendance(self.driver)
        attendance.navigate_to_timeSheetPage()
        attendance.navigate_to_attendance_page()
        attendance.validate_punchIn_Page()
