import time
import pytest
from pages.loginPage import LoginPage
from pages.recruitmentTableVerification import recruitment
from utilities.readProperties import readConfig


@pytest.mark.usefixtures("setup_teardown")
class TestrecruitmentTableVerification:
    @pytest.mark.recruit_table
    def test_recruitmentTable(self):
        login = LoginPage(self.driver)
        login.enter_username(readConfig().getuserName())
        login.enter_password(readConfig().getPassword())
        login.click_loginBtn()
        time.sleep(5)
        recruit = recruitment(self.driver)
        recruit.recruitment_page_validation()

