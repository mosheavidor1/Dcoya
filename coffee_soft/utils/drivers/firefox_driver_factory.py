from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

class FirefoxDriverFactory:
    def set_driver(self, browser):

        pass

    def get_driver(self):

        return None

    def set_url(self, url):

        pass

    def create_driver(self):
        GeckoDriverManager().setup()
        return webdriver.Firefox()
