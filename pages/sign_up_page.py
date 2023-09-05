import allure

from locators.login_page_locators import SignUpPageLocators
from pages.base_page import BasePage
import time
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver import Keys


class SignUpPage(BasePage):

    @allure.step('Click on sign up Button')
    def click_on_sign_up_button(self):
        self.element_is_visible(SignUpPageLocators.SIGN_UP_BUTTON).click()

    @allure.step('Fill email and password')
    def fill_email_and_password_inputs(self, email, password, role):
        time.sleep(1)
        with allure.step('select role'):
            roles = {"node_runner": SignUpPageLocators.NODE_RUNNER_RADIO,
                     "developer": SignUpPageLocators.DEVELOPER_RADIO,
                     "validator": SignUpPageLocators.VALIDATOR_RADIO
                     }
            self.element_is_visible(roles[role]).click()
            self.element_is_visible(LoginPageLocators.CONFIRM_BUTTON).click()
        with allure.step('Fill Inputs'):
            self.element_is_visible(SignUpPageLocators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(SignUpPageLocators.PASSWORD_INPUT).send_keys(password)
        time.sleep(2)

    @allure.step('Click Register button')
    def click_register_button(self):
        self.element_is_visible(SignUpPageLocators.REGISTER_BUTTON).click()

    @allure.step("Get Error")
    def get_error_message(self):
        error_message = self.element_is_visible(SignUpPageLocators.ERROR_MESSAGE).text
        return error_message

    @allure.step('Select User role')
    def user_role(self, role):
        roles = {"node_runner": LoginPageLocators.NODE_RUNNER_RADIO,
                 "developer": LoginPageLocators.DEVELOPER_RADIO,
                 "validator": SignUpPageLocators.VALIDATOR_RADIO}
        self.element_is_visible(roles[role]).click()
        self.element_is_visible(LoginPageLocators.CONFIRM_BUTTON).click()

    @allure.step('get info')
    def get_info_after_registration(self):
        get_text_after_register = self.element_is_visible(SignUpPageLocators.VERIFY_EMAIL).text
        get_email_after_register = self.element_is_visible(SignUpPageLocators.CHECK_EMAIL).text
        return get_text_after_register, get_email_after_register

    @allure.step('Click TAB key button')
    def click_tab_key_on_input(self):
        self.element_is_visible(SignUpPageLocators.PASSWORD_INPUT).send_keys(Keys.TAB)


