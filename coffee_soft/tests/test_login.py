from coffee_soft.pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_login_page()
    login_page.enter_username("testuser")
    login_page.enter_password("testpassword")
    login_page.click_login_button()
    assert login_page.is_logged_in()