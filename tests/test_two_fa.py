import time
import requests
from pages.login_page import LoginPage
from tests.data_for_tests import Url
from pages.two_fa_page import TwoFA


class TestTwoFa:

    def test_check_two_fa_on_valid_data(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("yura@zpoken.io", "213456qaZ", "node_runner")
        login.click_sign_in_button()

        get_totp = TwoFA(driver)
        totp = get_totp.totp()
        token_first = get_totp.get_two_fa_code(totp)
        x = [int(a) for a in str(token_first)]
        one = x[0]
        two = x[1]
        three = x[2]
        four = x[3]
        five = x[4]
        six = x[5]
        get_totp.continue_fa_button()
        get_totp.verify_totp_code(one, two, three, four, five, six)
        get_totp.verify_totp_before_login()

        alert = get_totp.get_alert()
        assert alert == "2FA is successfully set", "Two FA code didn't reset"
        time.sleep(2)
        login.log_out()

        login.log_in("yura@zpoken.io", "213456qaZ", "node_runner")
        login.click_sign_in_button()

        get_totp.verify_totp_code(one, two, three, four, five, six)
        get_totp.verify_totp_after_login()

        get_totp.off_two_fa()
        get_totp.verify_totp_code(one, two, three, four, five, six)
        get_totp.verify_code_delete()

        alert = get_totp.get_alert()
        assert alert == "2FA has been reset", "Two FA code didn't reset"
        time.sleep(1)

    def test_check_two_fa_enter_wrong_totp_on(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("yura@zpoken.io", "213456qaZ", "node_runner")
        login.click_sign_in_button()

        get_totp = TwoFA(driver)
        get_totp.totp()

        get_totp.continue_fa_button()
        get_totp.verify_totp_code('1', '2', '3', '4', '5', '6')
        get_totp.verify_totp_before_login()
        error_message = get_totp.get_error()
        assert error_message == 'TOTP is invalid'




