import pytest
from coffee_soft.utils.drivers.driver_factory import DriverFactory
from coffee_soft.pages.login_page import LoginPage


class TestLogin:
    @pytest.fixture
    def driver(self):
        driver_factory = DriverFactory('chrome')
        driver = driver_factory.create_driver()
        driver.get("https://www.coffe-soft.com")
        yield driver

    @pytest.mark.order(1)
    def test_login(self, driver):
        login_page = LoginPage(driver)
        login_page.valid_user_login()

    @pytest.mark.order(2)
    def test_negative_login(self, driver):
        login_page = LoginPage(driver)
        login_page.invalid_user_credentials()


if __name__ == '__main__':
    pytest.main(['-v', '--strict-markers', 'tests/'])
