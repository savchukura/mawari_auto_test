from pages.admin_pages.admin_login_page import AdminLoginPage
from pages.admin_pages.admin_account_page import AdminAccountPage
import allure
import time


@allure.feature("Admin sign in")
class TestAdminLogin:

    @allure.title("Check Admin login use valid data")
    def test_admin_login_valid_data(self, driver):
        admin_login = AdminLoginPage(driver, "https://dev-mn-admin.zpoken.dev/login")
        admin_login.open()
        admin_login.login_enter_email_and_password('alex+i@zpoken.io', '12345678')
        admin_login.login_click_sign_in_button()

        admin_account = AdminAccountPage(driver)
        get_dashboard_title = admin_account.get_dashboard_title()
        assert get_dashboard_title == "Admin", "Wrong title text"

    @allure.title("Check Admin log out use valid data")
    def test_admin_login_valid_data(self, driver):
        admin_login = AdminLoginPage(driver, "https://dev-mn-admin.zpoken.dev/login")
        admin_login.open()
        admin_login.login_enter_email_and_password('alex+i@zpoken.io', '12345678')
        admin_login.login_click_sign_in_button()

        admin_account = AdminAccountPage(driver)
        admin_account.click_log_out_button()
        time.sleep(2)
        url = driver.current_url.split("/")[-1]
        assert url == "login", "User Doesn't do log out"

    @allure.title("Check error message if the user enter invalid email")
    def test_user_use_not_registered_email_invalid_data(self, driver):
        admin_login = AdminLoginPage(driver, "https://dev-mn-admin.zpoken.dev/login")
        admin_login.open()
        admin_login.login_enter_email_and_password('testemail9999@zpoken.io', '12345678')
        admin_login.login_click_sign_in_button()

        error_text = admin_login.get_error()

        assert error_text == "Email not found", "Wrong error message"

    @allure.title("Check error message if the user enter valid email without @")
    def test_user_use_not_registered_email_invalid_data(self, driver):
        admin_login = AdminLoginPage(driver, "https://dev-mn-admin.zpoken.dev/login")
        admin_login.open()
        admin_login.login_enter_email_and_password('alex+izpoken.io', '12345678')

        error_text = admin_login.get_error()

        assert error_text == "The email is incorrect", "Wrong error message"

    @allure.title("Check error message if the user leave email input empty ")
    def test_user_use_not_registered_email_invalid_data(self, driver):
        admin_login = AdminLoginPage(driver, "https://dev-mn-admin.zpoken.dev/login")
        admin_login.open()
        admin_login.login_enter_email_and_password('', '12345678')

        error_text = admin_login.get_error()

        assert error_text == "The field email is required", "Wrong error message"

    @allure.title("Check error message if the user leave password input empty ")
    def test_user_use_not_registered_email_invalid_data(self, driver):
        admin_login = AdminLoginPage(driver, "https://dev-mn-admin.zpoken.dev/login")
        admin_login.open()
        admin_login.login_enter_email_and_password('alex+i@zpoken.io', '')
        admin_login.click_tab_key()
        error_text = admin_login.get_error()

        assert error_text == "The field password is required", "Wrong error message"

    @allure.title("Check error message if the user enter invalid password")
    def test_user_use_not_registered_email_invalid_data(self, driver):
        admin_login = AdminLoginPage(driver, "https://dev-mn-admin.zpoken.dev/login")
        admin_login.open()
        admin_login.login_enter_email_and_password('alex+i@zpoken.io', '147852')
        admin_login.login_click_sign_in_button()
        error_text = admin_login.get_error()

        assert error_text == "Wrong password", "Wrong error message"

