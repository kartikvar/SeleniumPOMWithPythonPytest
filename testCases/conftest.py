import os

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Configurations.readConfigurations import ReadConfiguration
from pageObject.login_page import LoginPage

'''
take screenshot in case of test failure
code taken from https://github.com/pytest-dev/pytest/issues/230
'''

screenshot_path = ("D:\\Learn_SDET\\Selenium\\Selenium_Codes\\Selenium_Framework_Python_Pytest"
                   "\\SeleniumPOMWithPythonPytest\\Screenshot\\screen_shot.png")
baseURL = ReadConfiguration.get_application_url()
username = ReadConfiguration.get_application_username()
password = ReadConfiguration.get_application_password()


@pytest.fixture()
def setup():
    os.environ['WDM_SSL_VERIFY'] = '0'
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver


@pytest.fixture()
def login_to_home_page():
    os.environ['WDM_SSL_VERIFY'] = '0'
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get(baseURL)
    lp = LoginPage(driver)
    lp.enter_username(username)
    lp.enter_password(password)
    lp.click_sign_in_button()
    return driver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.yield_fixture
def tear_down_login(request, setup):
    driver = setup
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screen_shot", attachment_type=AttachmentType.PNG)
        driver.save_screenshot(screenshot_path)
        driver.close()
    else:
        driver.find_element(By.ID, "logo").click()


@pytest.yield_fixture
def tear_down(request, login_to_home_page):
    driver = login_to_home_page
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screen_shot", attachment_type=AttachmentType.PNG)
        driver.save_screenshot(screenshot_path)
        driver.close()
    else:
        driver.find_element(By.ID, "logo").click()
