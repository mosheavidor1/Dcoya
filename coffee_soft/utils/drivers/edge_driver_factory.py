from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class EdgeDriverFactory:
    def set_driver(self, browser):

        pass

    def get_driver(self):

        return None

    def set_url(self, url):

        pass

    def create_driver(self):
        EdgeChromiumDriverManager().setup()
        return webdriver.Edge()
