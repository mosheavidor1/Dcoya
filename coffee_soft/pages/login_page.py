from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from coffee_soft.utils.users.user_credentials import VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.LOGIN_TAB = (By.XPATH, "//a[normalize-space()='Login']")
        self.USER_FIELD = (By.XPATH, "//input[@id='id_username']")
        self.PASSWORD_FIELD = (By.XPATH, "//input[@id='id_password']")
        self.LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login!']")
        self.SUBMIT_ERROR = (By.XPATH, "//li[contains(text(),'Please enter a correct username and password. Note')]")

    def click_on_login(self):
        try:
            login_tab = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.LOGIN_TAB)
            )
            login_tab.click()
        except Exception as e:
            print(f"Exception occurred while clicking the Login tab: {e}")

    def set_username(self, username):
        try:
            user_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.USER_FIELD)
            )
            user_field.send_keys(username)
        except Exception as e:
            print(f"Exception occurred while setting the username: {e}")

    def set_password(self, password):
        try:
            password_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.PASSWORD_FIELD)
            )
            password_field.send_keys(password)
        except Exception as e:
            print(f"Password field is not clickable: {e}")

    def submit(self):
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.LOGIN_BUTTON)
            )
            submit_button.click()
        except Exception as e:
            print(f"Password field is not clickable: {e}")

    def user_login(self, username, password):
        LoginPage.click_on_login(self)
        LoginPage.set_username(self, username)
        LoginPage.set_password(self, password)
        LoginPage.submit(self)

    def valid_user_login(self):
        LoginPage.user_login(self, VALID_USERNAME, VALID_PASSWORD)

    def invalid_user_credentials(self):
        LoginPage.user_login(self, INVALID_USERNAME, INVALID_PASSWORD)

        try:

            error_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//li[contains(text(),'Please enter a correct username and password. Note')]"))
            )

            print(f"Invalid credentials!!!!!")
            print(error_message.text)
        except Exception as e:
            print(f"Error: {e}")
