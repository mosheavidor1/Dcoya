from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriverFactory :
    def set_driver(self, browser):

        pass

    def get_driver(self):

        return None

    def set_url(self, url):

        pass

    def create_driver(self):
        ChromeDriverManager().setup()
        return webdriver.Chrome()

