from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DriverFactory:
    @staticmethod
    def get_driver(browser_name):
        if browser_name.lower() == "chrome":
            chrome_options = webdriver.ChromeOptions()

            driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        return driver