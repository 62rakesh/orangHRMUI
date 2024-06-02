import time
import pytest
from pages.adminCreateUser import createUser
from pages.loginPage import LoginPage
from utilities.readProperties import readConfig
from testData.constants import Data


@pytest.mark.usefixtures("setup_teardown")
class TestCreateUser:
    @pytest.mark.create_user
    def test_createNewUser(self):
        login = LoginPage(self.driver)
        login.enter_username(readConfig().getuserName())
        login.enter_password(readConfig().getPassword())
        login.click_loginBtn()
        time.sleep(5)
        user = createUser(self.driver)
        user.navigate_to_the_adminPage()
        user.create_new_user()
        user.enter_user_name(Data().generate_random_userName())
        user.create_password(readConfig().createPassword())
        user.enter_emp_name("Virat")
        user.save_user()
