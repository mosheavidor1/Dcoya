from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from coffee_soft.utils.users import user_credentials


class EditUserDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.duration = 10
        self.PROFILE_TAB = (By.XPATH, "//a[normalize-space()='Profile']")
        self.USER_NAME_EDIT = (By.XPATH, "//input[@id='id_username']")
        self.EMAIL_ADDRESS_EDIT = (By.XPATH, "//input[@id='id_email']")
        self.UPDATE_BUTTON = (By.XPATH, "//button[normalize-space()='Update']")

    def click_on_profile_tab(self):
        profile_tab = WebDriverWait(self.driver, self.duration).until(
            EC.visibility_of_element_located(self.PROFILE_TAB)
        )
        if profile_tab.is_displayed():
            profile_tab.click()

            create_post_tab = WebDriverWait(self.driver, self.duration).until(
                EC.visibility_of_element_located(self.PROFILE_TAB)
            )
            if create_post_tab.is_displayed():
                create_post_tab.click()
            else:
                print("Profile tab is not clickable")

    def edit_user_name(self, user):
        user_edit = WebDriverWait(self.driver, self.duration).until(
            EC.visibility_of_element_located(self.USER_NAME_EDIT)
        )
        if user_edit.is_displayed():
            user_edit.send_keys(user)
        else:
            print("User element is not clickable")

    def edit_email(self, email):
        email_edit = WebDriverWait(self.driver, self.duration).until(
            EC.visibility_of_element_located(self.EMAIL_ADDRESS_EDIT)
        )
        if email_edit.is_displayed():
            email_edit.send_keys(email)
        else:
            print("Email element is not clickable")

    def update_button(self):
        update_button = WebDriverWait(self.driver, self.duration).until(
            EC.visibility_of_element_located(self.UPDATE_BUTTON)
        )
        if update_button.is_displayed():
            update_button.click()
        else:
            print("Update button is not clickable")

    def edit_user_info(self):
        self.click_on_profile_tab()
        self.edit_user_name(user_credentials.EDIT_USER)
        self.edit_email(user_credentials.EDIT_EMAIL)
        self.update_button()
