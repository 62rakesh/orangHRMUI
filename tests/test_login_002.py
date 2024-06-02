import time
import pytest
from pytest import mark
from pages.loginPage import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestLogin_002:
    @mark.sanity_test
    def test_login_with_invalid_credentials(self):
        login = LoginPage(self.driver)
        login.enter_username("Admin123")
        login.enter_password("admin1233413")
        login.click_loginBtn()
        time.sleep(5)

