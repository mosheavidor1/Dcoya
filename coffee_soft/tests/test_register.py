import pytest
from coffee_soft.utils.drivers.driver_factory import DriverFactory
from coffee_soft.pages.new_register import NewRegister


class RegisterLogin:
    @pytest.fixture
    def driver(self):
        driver_factory = DriverFactory("chrome")
        driver = driver_factory.create_driver()
        driver.get("https://www.coffe-soft.com")
        yield driver


@pytest.mark.order(1)
def test_register_new_user(self, driver):
    register_user = NewRegister(driver)
    register_user.valid_register()


if __name__ == '__main__':
    pytest.main(['-v', '--strict-markers', 'coffee_soft/tests/'])
