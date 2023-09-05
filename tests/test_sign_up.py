import allure
from generator.generator import generated_person
from pages.sign_up_page import SignUpPage
import time


@allure.feature("Sign up")
class TestSignUpPage:

    @allure.title('Sign up as Node runner valid data')
    def test_sign_up_node_runner_account_valid_data(self, driver):
        sign_up = SignUpPage(driver, "https://dev-mawari.zpoken.dev/login")
        sign_up.open()
        sign_up.user_role("node_runner")
        sign_up.click_on_sign_up_button()
        person_info = next(generated_person())
        email = person_info.email
        sign_up.fill_email_and_password_inputs(email, '12345678', 'node_runner')
        sign_up.click_register_button()
        get_text_after_register, get_email_after_register = sign_up.get_info_after_registration()
        assert get_text_after_register == "Verify your email", "text doesn't present"
        assert get_email_after_register == email, "invalid email"

    @allure.title('Sign up as Developer valid data')
    def test_sign_up_developer_account_valid_data(self, driver):
        sign_up = SignUpPage(driver, "https://dev-mawari.zpoken.dev/login")
        sign_up.open()
        sign_up.user_role("developer")
        sign_up.click_on_sign_up_button()
        person_info = next(generated_person())
        email = person_info.email
        sign_up.fill_email_and_password_inputs(email, '12345678', 'developer')
        sign_up.click_register_button()
        get_text_after_register, get_email_after_register = sign_up.get_info_after_registration()
        assert get_text_after_register == "Verify your email", "text doesn't present"
        assert get_email_after_register == email, "invalid email"

    @allure.title('Sign up as Validator valid data')
    def test_sign_up_validator_account_valid_data(self, driver):
        sign_up = SignUpPage(driver, "https://dev-mawari.zpoken.dev/login")
        sign_up.open()
        sign_up.user_role("validator")
        sign_up.click_on_sign_up_button()
        person_info = next(generated_person())
        email = person_info.email
        sign_up.fill_email_and_password_inputs(email, '12345678', 'validator')
        sign_up.click_register_button()
        get_text_after_register, get_email_after_register = sign_up.get_info_after_registration()
        assert get_text_after_register == "Verify your email", "text doesn't present"
        assert get_email_after_register == email, "invalid email"

    @allure.title('Leave email input empty')
    def test_sign_up_user_leave_email_input_empty(self, driver):
        sign_up = SignUpPage(driver, "https://dev-mawari.zpoken.dev/login")
        sign_up.open()
        sign_up.user_role("node_runner")
        sign_up.click_on_sign_up_button()
        sign_up.fill_email_and_password_inputs('', '12345678', 'developer')
        error_message = sign_up.get_error_message()
        assert error_message == "The field email is required", "invalid error message"

    @allure.title('Leave password input Empty')
    def test_sign_up_user_leave_password_input_empty(self, driver):
        sign_up = SignUpPage(driver, "https://dev-mawari.zpoken.dev/login")
        sign_up.open()
        sign_up.user_role("node_runner")
        sign_up.click_on_sign_up_button()
        sign_up.fill_email_and_password_inputs('testemail@gmail.com', '', 'developer')
        sign_up.click_tab_key_on_input()
        error_message = sign_up.get_error_message()
        assert error_message == "The field password is required", "invalid error message"

    @allure.title('Fill week password')
    def test_sign_up_user_enter_week_password(self, driver):
        sign_up = SignUpPage(driver, "https://dev-mawari.zpoken.dev/login")
        sign_up.open()
        sign_up.user_role("node_runner")
        sign_up.click_on_sign_up_button()
        sign_up.fill_email_and_password_inputs('testemail@gmail.com', '123', 'developer')
        sign_up.click_tab_key_on_input()
        error_message = sign_up.get_error_message()
        assert error_message == "password must be at least 6 characters", "invalid error message"

    @allure.title("Fill Email without @")
    def test_sign_up_user_enter_email_without_at(self, driver):
        sign_up = SignUpPage(driver, "https://dev-mawari.zpoken.dev/login")
        sign_up.open()
        sign_up.user_role("node_runner")
        sign_up.click_on_sign_up_button()
        sign_up.fill_email_and_password_inputs('testemailgmail.com', '12345678', 'developer')

        error_message = sign_up.get_error_message()
        assert error_message == "The email is incorrect", "invalid error message"
