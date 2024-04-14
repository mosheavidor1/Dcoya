from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from typing import Optional
from coffee_soft.utils.users.user_credentials import NEW_USER, NEW_PASSWORD, EMAIL


class NewRegisterPage:
    def __init__(self, driver: WebDriver, timeout: Optional[int] = 10):
        self.driver = driver
        self.timeout = timeout
        self.firstNameInput = (By.XPATH, "//input[@id='id_username']")
        self.emailInput = (By.XPATH, "//input[@id='id_email']")
        self.passwordInput = (By.XPATH, "//input[@id='id_password1']")
        self.confirmPasswordInput = (By.XPATH, "//input[@id='id_password2']")
        self.registerButton = (By.XPATH, "//button[normalize-space()='Sign Up!']")
        self.registerTab = (By.XPATH, "//a[normalize-space()='Register']")
        self.invalidRegistration = (By.XPATH, "//strong[normalize-space()='A user with that username already exists.']")

    def navigate_to_page(self):
        try:
            register_tab_element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(self.registerTab)
            )
            register_tab_element.click()
        except TimeoutException as e:
            print(f"Exception occurred while navigating to the register page: {e}")

    def enter_username(self, first_name):
        try:
            username_field = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(self.firstNameInput)
            )
            username_field.send_keys(first_name)
        except TimeoutException as e:
            print(f"Exception occurred while entering the username: {e}")

    def enter_email(self, email):
        try:
            email_field = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(self.emailInput)
            )
            email_field.send_keys(email)
        except TimeoutException as e:
            print(f"Exception occurred while entering the email: {e}")

    def enter_password(self, password):
        try:
            password_field = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(self.passwordInput)
            )
            password_field.send_keys(password)
        except TimeoutException as e:
            print(f"Exception occurred while entering the password: {e}")

    def enter_confirm_password(self, password):
        try:
            confirm_password_field = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(self.confirmPasswordInput)
            )
            confirm_password_field.send_keys(password)
        except TimeoutException as e:
            print(f"Exception occurred while entering the confirm password: {e}")

    def click_register_button(self):
        try:
            register_button = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(self.registerButton)
            )
            register_button.click()
        except TimeoutException as e:
            print(f"Exception occurred while clicking the register button: {e}")

    def is_invalid_registration_message_displayed(self):
        try:
            invalid_registration_element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(self.invalidRegistration)
            )
            return invalid_registration_element.is_displayed()
        except TimeoutException:
            return False

    def register(self):
        self.navigate_to_page()
        self.enter_username(NEW_USER)
        self.enter_email(EMAIL)
        self.enter_password(NEW_PASSWORD)
        self.enter_confirm_password(NEW_PASSWORD)
        self.click_register_button()

    def valid_register(self):
        self.register()

    def invalid_user(self):
        self.valid_register()
        try:
            invalid_reg = self.driver.find_element(*self.invalidRegistration)
            if invalid_reg.is_displayed():
                print(invalid_reg.text)
        except Exception as e:
            print(f"Exception occurred while checking invalid registration: {e}")
