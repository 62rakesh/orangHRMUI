import time
import pytest
from pages.adminCreateUser import createUser
from pages.createEmployeePage import createNewEmp
from pages.loginPage import LoginPage
from utilities.readProperties import readConfig
from testData.constants import Data


@pytest.mark.usefixtures("setup_teardown")
class TestAddEmployee:
    @pytest.mark.add_emp_test
    def test_addNewEmp(self):
        login = LoginPage(self.driver)
        login.enter_username(readConfig().getuserName())
        login.enter_password(readConfig().getPassword())
        login.click_loginBtn()
        time.sleep(5)
        emp = createNewEmp(self.driver)
        emp.navigate_to_PIM_page()
        emp.click_add_emp_Btn()
        emp_fullName = emp.create_employeeName(Data().generate_random_firstName(),
                                               Data().generate_random_middleName(),
                                               Data().generate_random_lastname())
        empID = emp.enter_empID("112233")
        emp.enable_loginDetails()
        emp_user_name = emp.create_user_Name(Data().generate_random_userName())
        user = createUser(self.driver)
        user.create_password(readConfig().createPassword())
        user.save_user()
        print(f"employee full name is: {emp_fullName}")
        print(f"employeeID is: {empID}")
        print(f"employee username is: {emp_user_name}")
        return emp_fullName


