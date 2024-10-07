from time import sleep

from selenium.webdriver.common.by import By


class PolicyFoldersPage:
    menu_burger_menu_id = "servi-nav-menu-toggler-svg"
    menu_price_simulation_xpath = "//span[@data-labelkey='PRICE_SIMULATION']"
    menu_standard_pricing_xpath = "//span[@data-labelkey='STANDARD_PRICING']"
    menu_price_cost_change_configuration = "//a[@href='/WebUI/PolicyFolder-list.mvc']"
    button_add_xpath = "//span[@class='ui-icon toolbar-item-icon-solo icon-mat-add']"

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_policy_folders_page(self):
        self.driver.find_element(By.ID, self.menu_burger_menu_id).click()
        self.driver.find_element(By.XPATH, self.menu_price_simulation_xpath).click()
        self.driver.find_element(By.XPATH, self.menu_standard_pricing_xpath).click()
        self.driver.find_element(By.XPATH, self.menu_price_cost_change_configuration).click()
