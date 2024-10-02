import configparser

path = "D:\\Learn_SDET\\Selenium\\Selenium_Codes\\Selenium_Framework_Python_Pytest\\SeleniumPOMWithPythonPytest\\Configurations\\config.ini"
config = configparser.ConfigParser()
config.read(path)


class ReadConfiguration:

    @staticmethod
    def get_application_url():
        url = config.get("app_url", "base_url")
        return url

    @staticmethod
    def get_application_username():
        username = config.get("credentials", "login_username")
        return username

    @staticmethod
    def get_application_password():
        password = config.get("credentials", "login_password")
        return password
