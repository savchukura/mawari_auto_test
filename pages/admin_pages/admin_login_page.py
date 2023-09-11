from locators.admin.admin_login_page_locators import AdminLoginPageLocators
from pages.base_page import BasePage
from selenium.webdriver import Keys

class AdminLoginPage(BasePage):

    def login_enter_email_and_password(self, login, password):
        self.element_is_visible(AdminLoginPageLocators.LOGIN_INPUT).send_keys(login)
        self.element_is_visible(AdminLoginPageLocators.PASSWORD_INPUT).send_keys(password)

    def login_click_sign_in_button(self):
        self.element_is_visible(AdminLoginPageLocators.SIGN_IN_BUTTON).click()

    def get_error(self):
        error_message = self.element_is_visible(AdminLoginPageLocators.ERROR)
        return error_message.text

    def click_tab_key(self):
        self.element_is_visible(AdminLoginPageLocators.PASSWORD_INPUT).click()
        self.element_is_visible(AdminLoginPageLocators.PASSWORD_INPUT).send_keys(Keys.TAB)

