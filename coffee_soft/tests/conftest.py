import pytest

from coffee_soft.utils.drivers import DriverFactory


@pytest.fixture(scope="session")
def driver():
    factory = DriverFactory()
    factory.set_driver("chrome")  # Set the desired browser ("chrome", "firefox", or "edge")
    driver_instance = factory.get_driver()
    yield driver_instance
    driver_instance.quit()


