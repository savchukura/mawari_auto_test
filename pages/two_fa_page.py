import time
import pyotp

from locators.two_fa_locators import TwoFaLocators
from pages.base_page import NextPage


class TwoFA(NextPage):

    def get_two_fa_code(self, totp_code):

        totp = pyotp.TOTP(totp_code)
        token = totp.now()
        return token

    def totp(self):
        self.element_is_visible(TwoFaLocators.USER_DETAIL).click()
        self.element_is_visible(TwoFaLocators.TWO_FA_TOGGLE).click()
        totp_code = self.element_is_visible(TwoFaLocators.TOTP_CODE)


        return totp_code.text

    def continue_fa_button(self):
        self.element_is_visible(TwoFaLocators.CONTINUE_FA_BUTTON).click()

    def verify_totp_code(self, one, two, three, four, five, six):

        self.element_is_visible(TwoFaLocators.VERIFY_INPUT_ONE).send_keys(one)
        self.element_is_visible(TwoFaLocators.VERIFY_INPUT_TWO).send_keys(two)
        self.element_is_visible(TwoFaLocators.VERIFY_INPUT_THREE).send_keys(three)
        self.element_is_visible(TwoFaLocators.VERIFY_INPUT_FOUR).send_keys(four)
        self.element_is_visible(TwoFaLocators.VERIFY_INPUT_FIVE).send_keys(five)
        self.element_is_visible(TwoFaLocators.VERIFY_INPUT_SIX).send_keys(six)

    def verify_totp_before_login(self):
        self.element_is_visible(TwoFaLocators.VERIFY_CODE_BUTTON).click()

    def verify_totp_after_login(self):
        self.element_is_visible(TwoFaLocators.VERIFY_TWO_FA_AFTER_LOGIN).click()

    def verify_code_delete(self):
        self.element_is_visible(TwoFaLocators.VERIFY_TWO_FA_DELETE).click()

    def get_alert(self):
        alert = self.element_is_visible(TwoFaLocators.VALIDATION_ALERT)
        return alert.text

    def off_two_fa(self):
        self.element_is_visible(TwoFaLocators.USER_DETAIL).click()
        self.element_is_visible(TwoFaLocators.TWO_FA_TOGGLE_ON).click()