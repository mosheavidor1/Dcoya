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

    def test_login_tab(self, driver):
        login_page = LoginPage(driver)
        login_page.click_on_login()
        login_page.set_username()
        login_page.set_password()
        login_page.submit()


if __name__ == '__main__':
    pytest.main(['-v', 'tests/'])
