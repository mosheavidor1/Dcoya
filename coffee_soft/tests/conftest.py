import pytest
from coffee_soft.utils.drivers.driver_factory import DriverFactory

@pytest.fixture(scope="session")
def driver():
    driver = DriverFactory.get_driver("chrome")
    yield driver
    driver.quit()