import time

import allure
import pytest
from pages.EnmergencyContactDetails import emergencyContact
from pages.loginPage import LoginPage
from utilities.readProperties import readConfig


@pytest.mark.usefixtures("setup_teardown")
class TestEmergencyContact:
    @pytest.mark.test1
    def test_fillEmergencyContactDetails(self):
        login = LoginPage(self.driver)
        login.enter_username(readConfig().getuserName())
        login.enter_password(readConfig().getPassword())
        login.click_loginBtn()
        time.sleep(5)
        emergency = emergencyContact(self.driver)
        emergency.navigate_to_myInfo_page()
        emergency.emergencyContact_verification()
        emergency.addEmenrgecyContactUserDetails("Sanju", "wife", "1234567890")
        emergency.upload_emergencyContact_details()
