import time
import allure
from pages.login_page import LoginPage, UserPersonalPage
from pages.user_page import NodeRunnerPage
from pages.two_fa_page import TwoFA
from tests.data_for_tests import Url


@allure.feature("Login")
class TestLogInPage:

    @allure.title("Login as Node runner")
    def test_login_as_node_runner(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "node_runner")
        login.click_sign_in_button()
        login.wait_user_personal_button()
        url = driver.current_url.split("/")[-2]
        login.log_out()

        assert url == "runners", "User log in under wrong role"

    @allure.title("Login Developer")
    def test_login_as_developer(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("yura@zpoken.io", "213456qaZ", "developer")
        login.click_sign_in_button()
        login.wait_user_personal_button()
        url = driver.current_url.split("/")[-2]
        login.log_out()
        assert url == "developers", "User log in under wrong role"

    @allure.title("Login Validator")
    def test_login_as_validator(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("yura@zpoken.io", "213456qaZ", "validator")
        login.click_sign_in_button()
        login.wait_user_personal_button()
        url = driver.current_url.split("/")[-2]
        login.log_out()
        assert url == "validators", "User log in under wrong role"

    @allure.title("Test log out")
    def test_log_out(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()
        login.log_out()
        time.sleep(2)
        url = driver.current_url.split("/")[-1]
        assert url == "login", "User Doesn't do log out"

    @allure.title("Test Leave email empty")
    def test_leave_email_input_empty(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("", "213456qaZ", "developer")

        error = login.get_error_message()
        assert error[0].text == "The field email is required", "ERROR message incorrect"

    @allure.title("Test Leave password empty")
    def test_leave_password_input_empty(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("yura@zpoken.io", "", "developer")
        login.click_tab_key_on_input()
        error = login.get_error_message()
        assert error[0].text == "The field password is required", "ERROR message incorrect"

    @allure.title("Test Email without @")
    def test_fill_email_without_at(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("yurazpoken.io", "213456qaZ", "developer")
        error = login.get_error_message()
        assert error[0].text == "The email is incorrect", "ERROR message incorrect"

    @allure.title("Test not registered email")
    def test_fill_not_registered_email(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("test999@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()
        error = login.get_error_message()
        assert error[0].text == "Email not found", "ERROR message incorrect"

    @allure.title("Test Invalid password")
    def test_fill_not_valid_password(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456", "developer")
        login.click_sign_in_button()
        error = login.get_error_message()
        assert error[0].text == "Wrong password", "ERROR message incorrect"

    @allure.title("Test password letters only in upper case")
    def test_fill_not_valid_password_letters_only_in_upper_case(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("yura@zpoken.io", "213456QAZ", "developer")
        login.click_sign_in_button()
        error = login.get_error_message()
        assert error[0].text == "Wrong password", "ERROR message incorrect"

    @allure.title("Test password letters only in lower case")
    def test_fill_not_valid_password_letters_only_in_lower_case(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaz", "developer")
        login.click_sign_in_button()
        error = login.get_error_message()
        assert error[0].text == "Wrong password", "ERROR message incorrect"

    @allure.title("Test white space before password")
    def test_fill_not_valid_password_fill_space_before_password(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("yura@zpoken.io", " 213456qaZ", "developer")
        login.click_sign_in_button()
        error = login.get_error_message()
        assert error[0].text == "Wrong password", "ERROR message incorrect"

    @allure.title("Test white space after password")
    def test_fill_not_valid_password_fill_space_after_password(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ  ", "developer")
        login.click_sign_in_button()
        error = login.get_error_message()
        assert error[0].text == "Wrong password", "ERROR message incorrect"

    @allure.title("Test white space in the middle password")
    def test_fill_not_valid_password_fill_space_in_the_middle_password(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("yura@zpoken.io", "213456 qaZ", "developer")

        login.click_sign_in_button()

        error = login.get_error_message()
        assert error[0].text == "Wrong password", "ERROR message incorrect"

    @allure.title("Test invalid password? add one symbol")
    def test_fill_not_valid_password_add_one_symbol(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ@", "developer")
        login.click_sign_in_button()
        error = login.get_error_message()
        assert error[0].text == "Wrong password", "ERROR message incorrect"

    @allure.title("Test click back button after log out")
    def test_click_back_browser_button_after_user_made_logout(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("yura@zpoken.io", "213456qaZ", "node_runner")
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


@allure.feature("Change password")
class TestChangePassword:

    @allure.title("Test only digit")
    def test_change_password_use_only_digit_valid_data(self, driver):
        password_before = '213456qaZ'
        new_password = '12345678'
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", password_before, "node_runner")
        time.sleep(0.5)
        login.click_sign_in_button()

        change_password_page = UserPersonalPage(driver)
        change_password_page.click_on_user_personal_button()
        change_password_page.click_on_change_password_button_on_page()
        change_password_page.fill_password_fields(password_before, new_password, new_password)
        change_password_page.click_on_change_in_modal_button()
        alert_text = change_password_page.get_alert_text()

        assert alert_text == 'Password changed'

        login.log_out()

        login.log_in("savcukura866@gmail.com", new_password, "node_runner")
        time.sleep(0.5)
        login.click_sign_in_button()

        change_password_page.return_password(new_password, password_before, password_before)
        alert_text = change_password_page.get_alert_text()

        assert alert_text == 'Password changed'
        time.sleep(2)

    @allure.title("Test only letters")
    def test_change_password_use_only_letters_valid_data(self, driver):
        password_before = '213456qaZ'
        new_password = 'qwertyui'
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", password_before, "node_runner")
        time.sleep(0.5)
        login.click_sign_in_button()

        change_password_page = UserPersonalPage(driver)
        change_password_page.click_on_user_personal_button()
        change_password_page.click_on_change_password_button_on_page()
        change_password_page.fill_password_fields(password_before, new_password, new_password)
        change_password_page.click_on_change_in_modal_button()
        alert_text = change_password_page.get_alert_text()

        assert alert_text == 'Password changed'

        login.log_out()

        login.log_in("savcukura866@gmail.com", new_password, "node_runner")
        time.sleep(0.5)
        login.click_sign_in_button()

        change_password_page.return_password(new_password, password_before, password_before)
        alert_text = change_password_page.get_alert_text()

        assert alert_text == 'Password changed'
        time.sleep(2)

    @allure.title("Test letters and digits")
    def test_change_password_use_letters_and_digits_valid_data(self, driver):
        password_before = '213456qaZ'
        new_password = '123789zAq'
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", password_before, "node_runner")
        time.sleep(0.5)
        login.click_sign_in_button()

        change_password_page = UserPersonalPage(driver)
        change_password_page.click_on_user_personal_button()
        change_password_page.click_on_change_password_button_on_page()
        change_password_page.fill_password_fields(password_before, new_password, new_password)
        change_password_page.click_on_change_in_modal_button()
        alert_text = change_password_page.get_alert_text()

        assert alert_text == 'Password changed'

        login.log_out()

        login.log_in("savcukura866@gmail.com", new_password, "node_runner")
        time.sleep(0.5)
        login.click_sign_in_button()

        change_password_page.return_password(new_password, password_before, password_before)
        alert_text = change_password_page.get_alert_text()

        assert alert_text == 'Password changed'
        time.sleep(2)

    @allure.title("Test leave old password input empty")
    def test_change_password_leave_old_password_input_empty_invalid_data(self, driver):
        password_before = '213456qaZ'
        new_password = '123789zAq'
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", password_before, "node_runner")
        time.sleep(0.5)
        login.click_sign_in_button()

        change_password_page = UserPersonalPage(driver)
        change_password_page.click_on_user_personal_button()
        change_password_page.click_on_change_password_button_on_page()
        change_password_page.fill_password_fields('', new_password, new_password)
        error_message = change_password_page.get_error()

        assert error_message == "Password is required"

    @allure.title("Test leave new input empty")
    def test_change_password_leave_new_password_input_empty_invalid_data(self, driver):
        password_before = '213456qaZ'
        new_password = '123789zAq'
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", password_before, "node_runner")
        time.sleep(0.5)
        login.click_sign_in_button()

        change_password_page = UserPersonalPage(driver)
        change_password_page.click_on_user_personal_button()
        change_password_page.click_on_change_password_button_on_page()
        change_password_page.fill_password_fields(password_before, '', new_password)
        error_message = change_password_page.get_error()

        assert error_message == "New password is required"

    @allure.title("Test leave confirm input empty")
    def test_change_password_leave_confirm_new_password_input_empty_invalid_data(self, driver):
        password_before = '213456qaZ'
        new_password = '123789zAq'
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", password_before, "node_runner")
        time.sleep(0.5)
        login.click_sign_in_button()

        change_password_page = UserPersonalPage(driver)
        change_password_page.click_on_user_personal_button()
        change_password_page.click_on_change_password_button_on_page()
        change_password_page.fill_password_fields(password_before, new_password, '')
        change_password_page.click_tab_key_on_input()
        error_message = change_password_page.get_error()

        assert error_message == "Confirm password is required"

    @allure.title("Test enter wrong password in pld input")
    def test_change_password_enter_wrong_old_password_invalid_data(self, driver):
        password_before = '213456qaZ'
        new_password = '123789zAq'
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", password_before, "node_runner")
        time.sleep(0.5)
        login.click_sign_in_button()

        change_password_page = UserPersonalPage(driver)
        change_password_page.click_on_user_personal_button()
        change_password_page.click_on_change_password_button_on_page()
        change_password_page.fill_password_fields('123456789', new_password, new_password)
        change_password_page.click_on_change_in_modal_button()
        error_message = change_password_page.get_error()

        assert error_message == "Wrong password"

    @allure.title("Test new password ot equal to confirm ")
    def test_change_password_new_password_not_equal_to_confirm_invalid_data(self, driver):
        password_before = '213456qaZ'
        new_password = '123789zAq'
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", password_before, "node_runner")
        time.sleep(0.5)
        login.click_sign_in_button()

        change_password_page = UserPersonalPage(driver)
        change_password_page.click_on_user_personal_button()
        change_password_page.click_on_change_password_button_on_page()
        change_password_page.fill_password_fields(password_before, new_password, 'qWe123456')
        change_password_page.click_tab_key_on_input()
        error_message = change_password_page.get_error()

        assert error_message == "Passwords must match"








