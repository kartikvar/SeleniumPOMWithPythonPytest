import logging

import allure
import pytest

from Configurations.readConfigurations import ReadConfiguration
from pageObject.login_page import LoginPage
from utilities.Custom_Logger import LogGeneration
from utilities.ExcelUtilities import read_data_from_excel


@pytest.mark.usefixtures("tear_down")
class TestLoginPage:

    # @pytest.yield_fixture
    # def log_on_failure(request, setup):
    #     driver = setup
    #     yield
    #     item = request.node
    #     if item.rep_call.failed:
    #         allure.attach(driver.)

    excel_path = ("D:\\Learn_SDET\\Selenium\\Selenium_Codes\\Selenium_Framework_Python_Pytest"
                  "\\SeleniumPOMWithPythonPytest\\TestData\\test_data.xlsx")

    base_url = ReadConfiguration.get_application_url()
    username = ReadConfiguration.get_application_username()
    password = ReadConfiguration.get_application_password()

    log = LogGeneration.logging()

    invalid_username = read_data_from_excel(excel_path, "Sheet1", 2, 1)
    invalid_password = read_data_from_excel(excel_path, "Sheet1", 2, 2)

    def test_login_with_valid_credentials(self, setup):
        self.log.debug("****************** test_login_with_valid_credentials *******************")
        self.driver = setup
        self.log.debug("Opening the application URL")
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.log.debug("Enter valid username")
        self.lp.enter_username(self.username)
        self.log.debug("Enter valid password")
        self.lp.enter_password(self.password)
        self.log.debug("Click Sign In Button")
        self.lp.click_sign_in_button()

        self.log.debug("Validating the title of the Home Page")
        assert self.driver.title == "Home Page - PTC Inc. - Servigistics 141"

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

