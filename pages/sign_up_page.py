from locators.login_page_locators import SignUpPageLocators
from pages.base_page import BasePage
import time


class SignUpPage(BasePage):

    def click_on_sign_up_button(self):
        self.element_is_visible(SignUpPageLocators.SIGN_UP_BUTTON).click()

    def fill_email_and_password_inputs(self, email, password, role):
        time.sleep(1)
        self.element_is_visible(SignUpPageLocators.EMAIL_INPUT).send_keys(email)
        self.element_is_visible(SignUpPageLocators.PASSWORD_INPUT).send_keys(password)
        roles = {"node_runner": SignUpPageLocators.NODE_RUNNER_RADIO,
                 "developer": SignUpPageLocators.DEVELOPER_RADIO}
        self.element_is_visible(roles[role]).click()

    def click_register_button(self):
        self.element_is_visible(SignUpPageLocators.REGISTER_BUTTON).click()

    def get_error_message(self):
        error_message = self.element_is_visible(SignUpPageLocators.ERROR_MESSAGE).text
        return error_message
