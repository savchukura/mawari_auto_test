from selenium.webdriver import Keys

from pages.base_page import BasePage, NextPage
from locators.login_page_locators import LoginPageLocators, UserPersonalPageLocators


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
        error_message = self.elements_are_visible(LoginPageLocators.ERROR_MESSAGE, 20)
        return error_message

    def click_back_browser_button(self):
        self.click_back_browser()


class UserPersonalPage(NextPage):

    def click_on_user_personal_button(self):
        self.element_is_visible(UserPersonalPageLocators.USER_PERSONAL).click()

    def click_on_change_password_button_on_page(self):
        self.element_is_visible(UserPersonalPageLocators.CHANGE_PASSWORD_BUTTON).click()

    def fill_password_fields(self, old_password, new_password, confirm_new_password):
        self.element_is_visible(UserPersonalPageLocators.OLD_PASSWORD_INPUT).send_keys(old_password)
        self.element_is_visible(UserPersonalPageLocators.NEW_PASSWORD_INPUT).send_keys(new_password)
        self.element_is_visible(UserPersonalPageLocators.CONFIRM_NEW_PASSWORD_INPUT).send_keys(confirm_new_password)

    def click_on_change_in_modal_button(self):
        self.element_is_visible(UserPersonalPageLocators.CHANGE_PASSWORD_IN_MODAL_BUTTON).click()

    def get_alert_text(self):
        alert_text = self.element_is_visible(UserPersonalPageLocators.ALERT).text
        return alert_text

    def get_error(self):
        error_text = self.element_is_visible(UserPersonalPageLocators.ERROR_UNDER_INPUT).text
        return error_text

    def return_password(self, old_password, new_password, confirm_new_password):
        self.element_is_visible(UserPersonalPageLocators.USER_PERSONAL).click()
        self.element_is_visible(UserPersonalPageLocators.CHANGE_PASSWORD_BUTTON).click()
        self.element_is_visible(UserPersonalPageLocators.OLD_PASSWORD_INPUT).send_keys(old_password)
        self.element_is_visible(UserPersonalPageLocators.NEW_PASSWORD_INPUT).send_keys(new_password)
        self.element_is_visible(UserPersonalPageLocators.CONFIRM_NEW_PASSWORD_INPUT).send_keys(confirm_new_password)
        self.element_is_visible(UserPersonalPageLocators.CHANGE_PASSWORD_IN_MODAL_BUTTON).click()

    def click_tab_key_on_input(self):
        self.element_is_visible(UserPersonalPageLocators.CONFIRM_NEW_PASSWORD_INPUT).send_keys(Keys.TAB)
