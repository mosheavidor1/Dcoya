from coffee_soft.pages.new_register import NewRegisterPage
from coffee_soft.utils.drivers import DriverFactory
import unittest


class RegisterNewUserTest(unittest.TestCase):

    def setUp(self):
        self.driver_factory = DriverFactory("chrome")
        self.driver = self.driver_factory.create_driver(maximize_window=True, detach=True)
        self.driver.get("https://www.coffe-soft.com")

    def test_register_new_user(self):
        register_user = NewRegisterPage(self.driver)
        register_user.valid_register()

    def test_invalid_registration(self):
        register_user = NewRegisterPage(self.driver)
        register_user.invalid_user()


if __name__ == "__main__":
    unittest.main()
