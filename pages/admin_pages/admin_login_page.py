from locators.admin.admin_login_page_locators import AdminLoginPageLocators
from pages.base_page import BasePage


class AdminLoginPage(BasePage):

    def admin_login(self, login='alex+i@zpoken.io', password='12345678'):
        self.element_is_visible(AdminLoginPageLocators.LOGIN_INPUT).send_keys(login)
        self.element_is_visible(AdminLoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.element_is_visible(AdminLoginPageLocators.SIGN_IN_BUTTON).click()
        