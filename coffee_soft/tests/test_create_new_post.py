import pytest
from coffee_soft.utils.drivers.driver_factory import DriverFactory
from coffee_soft.pages.login_page import LoginPage
from coffee_soft.pages.create_post_page import CreatePostPage


class TestCreateNewPost:
    @pytest.fixture
    def driver(self):
        driver_factory = DriverFactory('chrome')
        driver = driver_factory.create_driver()
        driver.get("https://www.coffe-soft.com")
        yield driver

    @pytest.mark.order(1)
    def test_create_new_post(self, driver):
        login_page = LoginPage(driver)
        login_page.valid_user_login()
        create_post_page = CreatePostPage(driver)
        create_post_page.create_new_post("My post", "Hello everyone")


if __name__ == '__main__':
    pytest.main(['-v', '--strict-markers', 'tests/'])
