from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, *locator, timeout=None):
        if not timeout:
            timeout = self.timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Element not found within {timeout} seconds: {locator}")
        except NoSuchElementException:
            raise NoSuchElementException(f"Element not found: {locator}")

    def find_elements(self, *locator, timeout=None):
        if not timeout:
            timeout = self.timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Elements not found within {timeout} seconds: {locator}")

    def navigate_to(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url