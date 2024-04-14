import pytest
from coffee_soft.pages.edit_user_details_page import EditUserDetailsPage
from coffee_soft.pages.login_page import LoginPage
from coffee_soft.utils.drivers import DriverFactory


class TestEditProfile:
    @pytest.fixture
    def driver(self):
        driver_factory = DriverFactory('chrome')
        driver = driver_factory.create_driver()
        driver.get("https://www.coffe-soft.com")
        yield driver

    @pytest.mark.order(1)
    def test_edit_user_details(self, driver):
        login_page = LoginPage(driver)
        login_page.valid_user_login()
        edit_user_details_page = EditUserDetailsPage(driver)
        edit_user_details_page.edit_user_info()


if __name__ == "__main__":
    pytest.main([__file__])
