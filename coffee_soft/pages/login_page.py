from selenium.webdriver.common.by import By
from coffee_soft.pages import base_page
from coffee_soft.pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    _username_field = (By.ID, "username")
    _password_field = (By.ID, "password")
    _login_button = (By.CSS_SELECTOR, "button[type='submit']")
    _login_error_message = (By.CSS_SELECTOR, ".error-message")

    def navigate_to_login_page(self):
        self.driver.get("https://www.coffe-soft.com/blog/post/61/")

    def enter_username(self, username):
        self.find_element(*self._username_field).send_keys(username)

    def enter_password(self, password):
        self.find_element(*self._password_field).send_keys(password)

    def click_login_button(self):
        self.find_element(*self._login_button).click()

    def is_logged_in(self):
        # Implement logic to check if the user is logged in, e.g., by checking for the presence of a logout button
        # or the absence of the login form
        return False

    def is_login_error_displayed(self):
        try:
            self.find_element(*self._login_error_message)
            return True
        except:
            return False