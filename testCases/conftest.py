import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

'''
take screenshot in case of test failure
code taken from https://github.com/pytest-dev/pytest/issues/230
'''


@pytest.fixture()
def setup():
    os.environ['WDM_SSL_VERIFY'] = '0'
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
