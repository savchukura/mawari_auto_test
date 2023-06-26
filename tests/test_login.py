import time

from pages.login_page import LoginPage
from pages.user_page import NodeRunnerPage
from pages.two_fa_page import TwoFA


class TestCaseNew:

    def test_login_as_node_runner(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "node_runner")
        login.click_sign_in_button()
        time.sleep(2)
        url = driver.current_url.split("/")[-2]
        login.log_out()
        assert url == "runners", "User log in under wrong role"

    def test_login_as_developer(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()
        time.sleep(2)
        url = driver.current_url.split("/")[-2]
        login.log_out()
        assert url == "developers", "User log in under wrong role"

    def test_log_out(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()
        login.log_out()
        time.sleep(2)
        url = driver.current_url.split("/")[-1]
        assert url == "login", "User Doesn't do log out"

    def test_leave_email_input_empty(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("", "213456qaZ", "developer")

        error = login.get_error_message()
        assert error[0].text == "The field email is required", "ERROR message incorrect"

    def test_leave_password_input_empty(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "", "developer")
        error = login.get_error_message()
        assert error[0].text == "The field password is required", "ERROR message incorrect"

    def test_fill_email_without_at(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("yurazpoken.io", "213456qaZ", "developer")
        error = login.get_error_message()
        assert error[0].text == "The email is incorrect", "ERROR message incorrect"

    def test_fill_not_registered_email(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("test999@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()
        error = login.get_error_message()
        assert error[0].text == "Email not found", "ERROR message incorrect"

    def test_fill_not_valid_password(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456", "developer")
        login.click_sign_in_button()
        error = login.get_error_message()
        assert error[0].text == "Wrong password", "ERROR message incorrect"

    def test_fill_not_valid_password_letters_only_in_upper_case(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456QAZ", "developer")
        login.click_sign_in_button()
        error = login.get_error_message()
        assert error[0].text == "Wrong password", "ERROR message incorrect"

    def test_fill_not_valid_password_letters_only_in_lower_case(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaz", "developer")
        login.click_sign_in_button()
        error = login.get_error_message()
        assert error[0].text == "Wrong password", "ERROR message incorrect"

    def test_fill_not_valid_password_fill_space_before_password(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", " 213456qaZ", "developer")
        login.click_sign_in_button()
        error = login.get_error_message()
        assert error[0].text == "Wrong password", "ERROR message incorrect"

    def test_fill_not_valid_password_fill_space_after_password(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ  ", "developer")
        login.click_sign_in_button()
        error = login.get_error_message()
        assert error[0].text == "Wrong password", "ERROR message incorrect"

    def test_fill_not_valid_password_fill_space_in_the_middle_password(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456 qaZ", "developer")

        login.click_sign_in_button()

        error = login.get_error_message()
        assert error[0].text == "Wrong password", "ERROR message incorrect"

    def test_fill_not_valid_password_add_one_symbol(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ@", "developer")
        login.click_sign_in_button()
        error = login.get_error_message()
        assert error[0].text == "Wrong password", "ERROR message incorrect"

    def test_click_back_browser_button_after_user_made_logout(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "node_runner")
        time.sleep(0.5)
        login.click_sign_in_button()
        time.sleep(2)
        login.log_out()
        time.sleep(2)
        login.click_back_browser_button()
        time.sleep(2)
        url = driver.current_url.split("/")[-1]
        assert url == "login", "User Doesn't do log out"
        time.sleep(2)









