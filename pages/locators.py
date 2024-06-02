class Locators:

    def loginPage_locator(self):
        loginPage = {
            "username_xpath": "(//INPUT[@name='username'])",
            "password_xpath": "(//INPUT[@name='password'])",
            "loginBtn_xpath": "(//BUTTON[@class='oxd-button oxd-button--medium oxd-button--main "
                              "orangehrm-login-button'])",
            "logout_xpath": "(//A[contains(text(),'Logout')])",
            "account_xpath": "(//IMG[@class='oxd-userdropdown-img'])",
            "comapnyBrandLogo_xpath": "(//IMG[@alt='company-branding'])",
            "helpButton":"(//BUTTON[@class='oxd-icon-button'])",
            "admin":"(//SPAN[contains(text(),'Admin User Guide')])",
        }
        return loginPage

    def adminPage_locator(self):
        adminPage = {
            "adminPage_navigate_xpath": "(//LI[@class='oxd-main-menu-item-wrapper'])[position()=1]",
            "addButton_xpath": "(//BUTTON[@class='oxd-button oxd-button--medium oxd-button--secondary'])",
            "select_user_role_xpath":"(//DIV[contains(text(),'-- Select --')])[position()=1]",
            "select_admin_user_role":"(//DIV[@class()='oxd-select-dropdown --position-bottom'])[1]",

        }
        return adminPage
