from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver


class WebDriverFactory(ABC):
    @abstractmethod
    def set_driver(self, browser: str) -> None:
        pass

    @abstractmethod
    def get_driver(self) -> WebDriver:
        pass

    @abstractmethod
    def set_url(self, url: str) -> None:
        pass

    @abstractmethod
    def create_driver(self) -> WebDriver:
        pass


class MyWebDriverFactory(WebDriverFactory):
    def __init__(self):
        self.driver = None

    def set_driver(self, browser: str) -> None:

        pass

    def get_driver(self) -> WebDriver:
        return self.driver

    def set_url(self, url: str) -> None:
        self.driver.get(url)

    def create_driver(self) -> WebDriver:

        return self.driver

