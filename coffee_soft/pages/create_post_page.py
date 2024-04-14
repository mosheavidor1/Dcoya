from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Optional


class CreatePostPage:
    def __init__(self, driver: WebDriver, timeout: Optional[int] = 10):
        self.driver = driver
        self.timeout = timeout
        self.ABOUT_TAB = (By.XPATH, "//a[normalize-space()='About']")
        self.CREATE_POST_TAB = (By.XPATH, "//a[normalize-space()='Create Post']")
        self.SET_TITLE = (By.XPATH, "//input[@id='id_title']")
        self.SET_CONTENT = (By.XPATH, "//textarea[@id='id_content']")
        self.SUBMIT_POST = (By.XPATH, "//button[normalize-space()='Post!']")
        self.TITLE_VERIFIED = (By.XPATH, "//h2[@class='article-title']")
        self.DELETE_POST = (By.XPATH, "//a[normalize-space()='Delete Post']")
        self.APPROVE_DELETE = (By.CSS_SELECTOR, "button[type='submit']")

    def create_post(self):
        about_tab = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.ABOUT_TAB)
        )
        if about_tab.is_displayed():
            about_tab.click()
            create_post_tab = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(self.CREATE_POST_TAB)
            )
            if create_post_tab.is_displayed():
                create_post_tab.click()
            else:
                print("Create post is not clickable")
        else:
            print("About tab is not clickable")

    def set_title(self, title):
        title_field = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.SET_TITLE)
        )
        title_field.send_keys(title)

    def set_content(self, content):
        content_field = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.SET_CONTENT)
        )
        content_field.send_keys(content)

    def submit_post(self):
        submit_button = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.SUBMIT_POST)
        )
        submit_button.click()

    def test_article_title(self):
        article_title = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.TITLE_VERIFIED)
        )
        print(f"Article title text: {article_title.text}")

    def delete_post(self):
        delete_post_link = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.DELETE_POST)
        )
        delete_post_link.click()
        approve_delete_button = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.APPROVE_DELETE)
        )
        approve_delete_button.click()

    def create_new_post(self, title, content):
        self.create_post()
        self.set_title(title)
        self.set_content(content)
        self.submit_post()
        self.test_article_title()
        self.delete_post()
