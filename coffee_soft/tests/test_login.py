import pytest
from coffee_soft.utils.drivers.driver_factory import DriverFactory


class TestLogin:
    @pytest.fixture
    def driver(self):
        driver_factory = DriverFactory('chrome')
        driver = driver_factory.create_driver()
        yield driver
        driver_factory.quit_driver()

    def test_google_title(self, driver):
        driver.get("https://google.com")
