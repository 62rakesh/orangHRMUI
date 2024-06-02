from pytest import mark
import pytest
import time
from pages.loginPage import LoginPage
from utilities.readProperties import readConfig


@pytest.mark.usefixtures("setup_teardown")
class TestLogin_001:
    @mark.sanity_Test_1
    def test_login_with_valid_credentials(self):
        login = LoginPage(self.driver)
        login.enter_username(readConfig().getuserName())
        login.enter_password(readConfig().getPassword())
        login.click_loginBtn()
        time.sleep(5)
        login.switchingTab()
        # login.handle_window_alert()
        login.logout()
