from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def log_in(self, login, password, role):
        self.element_is_visible(LoginPageLocators.EMAIL_INPUT).send_keys(login)
        self.element_is_visible(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        roles = {"node_runner": LoginPageLocators.NODE_RUNNER_RADIO,
                 "developer": LoginPageLocators.DEVELOPER_RADIO}
        self.element_is_visible(roles[role]).click()

    def click_sign_in_button(self):
        self.element_is_visible(LoginPageLocators.SIGN_IN_BUTTON).click()

    def log_out(self):
        self.element_is_visible(LoginPageLocators.LOG_OUT_BUTTON).click()

    def get_email_validate_error(self):
        email_validation_message = self.element_is_visible(LoginPageLocators.EMAIL_INPUT).get_attribute("validationMessage")
        return email_validation_message

    def get_error_message(self):
        error_message = self.elements_are_visible(LoginPageLocators.ERROR_MESSAGE)
        return error_message

    def click_back_browser_button(self):
        self.click_back_browser()
