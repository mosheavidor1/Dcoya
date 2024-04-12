from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from coffee_soft.utils.users.user_credentials import VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD
from coffee_soft.infra.error_handling import ErrorHandling


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.LOGIN_TAB = (By.XPATH, "//a[normalize-space()='Login']")
        self.USER_FIELD = (By.XPATH, "//input[@id='id_username']")
        self.PASSWORD_FIELD = (By.XPATH, "//input[@id='id_password']")
        self.LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login!']")
        self.SUBMIT_ERROR = (By.XPATH, "//li[contains(text(),'Please enter a correct username and password. Note')]")

    @ErrorHandling.handle_exception
    def click_on_login(self):
        login_tab = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LOGIN_TAB)
        )
        login_tab.click()

    @ErrorHandling.handle_exception
    def set_username(self, username):
        user_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USER_FIELD)
        )
        user_field.send_keys(username)

    @ErrorHandling.handle_exception
    def set_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD_FIELD)
        )
        password_field.send_keys(password)

    @ErrorHandling.handle_exception
    def submit(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LOGIN_BUTTON)
        )
        submit_button.click()

    def user_login(self, username, password):
        self.click_on_login()
        self.set_username(username)
        self.set_password(password)
        self.submit()

    def valid_user_login(self):
        self.user_login(VALID_USERNAME, VALID_PASSWORD)

    def invalid_user_credentials(self):
        self.user_login(INVALID_USERNAME, INVALID_PASSWORD)

        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//li[contains(text(),'Please enter a correct username and password. Note')]"))
            )
            print(f"Invalid credentials!!!!!")
            print(error_message.text)
        except Exception as e:
            print(f"Error: {e}")
