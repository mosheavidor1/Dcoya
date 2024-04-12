from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverFactory:
    def __init__(self):
        self.driver = None

    def set_driver(self, browser):
        if browser == "chrome":
            chrome_options = Options()
            self.driver = webdriver.Chrome(chrome_options=chrome_options)

        elif browser == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == "edge":
            self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        else:
            print("Browser does not exist")

    def get_driver(self):
        return self.driver

    def set_url(self, url):
        if self.driver:
            self.driver.get(url)

    def create_driver(self):
        return self.driver
