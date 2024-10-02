import pytest

from Configurations.readConfigurations import ReadConfiguration
from pageObject.login_page import LoginPage
from utilities.ExcelUtilities import read_data_from_excel


class TestLoginPage:

    excel_path = ("D:\\Learn_SDET\\Selenium\\Selenium_Codes\\Selenium_Framework_Python_Pytest"
                  "\\SeleniumPOMWithPythonPytest\\TestData\\test_data.xlsx")

    base_url = ReadConfiguration.get_application_url()
    username = ReadConfiguration.get_application_username()
    password = ReadConfiguration.get_application_password()

    invalid_username = read_data_from_excel(excel_path, "Sheet1", 2, 1)
    invalid_password = read_data_from_excel(excel_path, "Sheet1", 2, 2)

    def test_login_with_valid_credentials(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_sign_in_button()

        assert self.driver.title == "Home Page - PTC Inc. - Servigistics 14"

    def test_login_with_invalid_credentials(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.invalid_username)
        self.lp.enter_password(self.invalid_password)
        print("Invalid username from excel is --> {}".format(self.invalid_username))
        print("Invalid password from excel is --> {}".format(self.invalid_password))
        self.lp.click_sign_in_button()

        assert self.lp.error_message() == "Invalid Sign in Name or Password"

