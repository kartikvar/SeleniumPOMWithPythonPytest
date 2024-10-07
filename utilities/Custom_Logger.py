import logging

path = ("D:\\Learn_SDET\\Selenium\\Selenium_Codes\\Selenium_Framework_Python_Pytest\\SeleniumPOMWithPythonPytest\\Logs"
        "\\log_file.log")


class LogGeneration:
    @staticmethod
    def logging():
        logger = logging.getLogger()
        fileHandler = logging.FileHandler(path)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
