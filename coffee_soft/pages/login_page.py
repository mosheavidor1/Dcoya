from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.REGISTER_BUTTON = (By.XPATH, "//a[normalize-space()='Login']")

    def click_on_login(self):
        try:
            register_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.REGISTER_BUTTON)
            )
            register_button.click()
        except Exception:
            print("Button is not clickable")
