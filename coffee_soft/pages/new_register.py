
from coffee_soft.utils.users.user_credentials import NEW_USER,NEW_PASSWORD,EMAIL

class NewRegister:

    def __init__(self, driver):
        self.driver = driver

        self.first_name_input = "//input[@id='id_username']"
        self.email_input = "//input[@id='id_email']"
        self.password_input = "//input[@id='id_password1']"
        self.password_input_conf = "//input[@id='id_password2']"
        self.register_button = "//button[normalize-space()='Sign Up!']"
        self.register_tab = "//a[normalize-space()='Register']"

    def navigate_to_page(self):
        self.driver.find_element_by_xpath(self.register_tab)

    def enter_username(self, first_name):
        self.driver.find_element_by_xpath(self.first_name_input).send_keys(first_name)

    def enter_email(self, email):
        self.driver.find_element_by_xpath(self.email_input).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_input).send_keys(password)

    def password_confirmation(self, password):
        self.driver.find_element_by_xpath(self.password_input_conf).send_keys(password)

    def click_register(self):
        self.driver.find_element_by_xpath(self.register_button).click()

    def register(self, name, password, email):
        navigate_to_page(self)
        enter_username(self, first_name)
        enter_email(self, email)
        enter_password(self, password)
        password_confirmation(self, password)
        click_register(self)

    def valid_register(self):
        NewRegister.register(self, NEW_USER, NEW_PASSWORD, EMAIL)
