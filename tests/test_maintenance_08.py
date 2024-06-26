import time
import pytest
from pytest import mark
from pages.loginPage import LoginPage
from pages.maintenance import Maintenance
from utilities.readProperties import readConfig


@mark.usefixtures("setup_teardown")
class TestMaintenance:
    @pytest.mark.maintenance
    def test_maintenance(self):
        login = LoginPage(self.driver)
        login.enter_username(readConfig().getuserName())
        login.enter_password(readConfig().getPassword())
        login.click_loginBtn()
        time.sleep(5)
        main = Maintenance(self.driver)
        main.verify_user(readConfig().getPassword())
        main.verify_user_access_records("Virat")
