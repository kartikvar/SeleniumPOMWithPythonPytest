from selenium.webdriver.common.by import By


class LoginPage:

    text_box_username_id = "txtUsername"
    text_box_password_id = "txtPassword"
    button_sign_in_link_text = "Sign in"
    error_message_xpath = "//div[@class='bubblecontent']/table/tbody/tr/td[3]/span"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.text_box_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.text_box_password_id).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(By.LINK_TEXT, self.button_sign_in_link_text).click()

    def error_message(self):
        error_message_login_page = self.driver.find_element(By.XPATH, self.error_message_xpath).text
        return error_message_login_page
