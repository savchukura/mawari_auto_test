from pages.sign_up_page import SignUpPage
import time


class TestSignUpPage:

    def test_sign_up_node_runner_account_valid_data(self, driver):
        sign_up = SignUpPage(driver, "https://dev-mawari.zpoken.dev/login")
        sign_up.open()
        sign_up.click_on_sign_up_button()
        sign_up.fill_email_and_password_inputs('testemail111@gmail.com', '12345678', 'developer')
        sign_up.click_register_button()
        time.sleep(5)

    def test_sign_up_user_leave_email_input_empty(self, driver):
        sign_up = SignUpPage(driver, "https://dev-mawari.zpoken.dev/login")
        sign_up.open()
        sign_up.click_on_sign_up_button()
        sign_up.fill_email_and_password_inputs('', '12345678', 'developer')
        error_message = sign_up.get_error_message()
        assert error_message == "The field email is required", "invalid error message"

    def test_sign_up_user_leave_password_input_empty(self, driver):
        sign_up = SignUpPage(driver, "https://dev-mawari.zpoken.dev/login")
        sign_up.open()
        sign_up.click_on_sign_up_button()
        sign_up.fill_email_and_password_inputs('testemail@gmail.com', '', 'developer')
        error_message = sign_up.get_error_message()
        assert error_message == "The field password is required", "invalid error message"

    def test_sign_up_user_enter_week_password(self, driver):
        sign_up = SignUpPage(driver, "https://dev-mawari.zpoken.dev/login")
        sign_up.open()
        sign_up.click_on_sign_up_button()
        sign_up.fill_email_and_password_inputs('testemail@gmail.com', '123', 'developer')
        error_message = sign_up.get_error_message()
        assert error_message == "password must be at least 6 characters", "invalid error message"

    def test_sign_up_user_enter_email_without_at(self, driver):
        sign_up = SignUpPage(driver, "https://dev-mawari.zpoken.dev/login")
        sign_up.open()
        sign_up.click_on_sign_up_button()
        sign_up.fill_email_and_password_inputs('testemailgmail.com', '123', 'developer')

        error_message = sign_up.get_error_message()
        assert error_message == "The email is incorrect", "invalid error message"
