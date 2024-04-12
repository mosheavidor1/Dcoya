from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from coffee_soft.infra import error_handling


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

    def set_username(self):
        try:
            user_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.USER_FIELD)
            )
            user_field.send_keys("Chris")
        except Exception as e:
            print(f"Exception occurred while setting the username: {e}")

    def set_password(self):
        try:
            password_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.PASSWORD_FIELD)
            )
            password_field.send_keys("Smile2008@")
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