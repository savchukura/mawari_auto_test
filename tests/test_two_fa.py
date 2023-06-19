import time
import requests
from pages.login_page import LoginPage

from pages.two_fa_page import TwoFA


class TestTwoFa:

    def test_check_two_fa_on(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("chronicletest103@gmail.com", "213456qaZ", "node_runner")
        login.click_sign_in_button()

        get_totp = TwoFA(driver)
        totp = get_totp.totp()

        token_code = TwoFA(driver)
        token_first = token_code.get_two_fa_code(totp)
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

        login.log_out()

        login.log_in("chronicletest103@gmail.com", "213456qaZ", "node_runner")
        login.click_sign_in_button()

        get_totp.verify_totp_code(one, two, three, four, five, six)
        get_totp.verify_totp_after_login()

        time.sleep(1)
        url = driver.current_url.split("/")[-2]
        assert url == "developers", "User log in under wrong role"

        get_totp.off_two_fa()
        get_totp.verify_totp_code(one, two, three, four, five, six)
        get_totp.verify_code_delete()

        #assert alert == "2FA has been reset", "Two FA code didn't reset"
        time.sleep(1)
        url = driver.current_url.split("/")[-1]
        assert url == "login", "User Doesn't do log out"

    def test_get_all_users(self):
        url = 'https://dev-mn-admin.zpoken.dev/api/v1/users'
        r = requests.get(url=url)
        print(r.status_code)

    def test_delete_user(self):
        url = 'https://dev.catlabs.zpoken.io/api/v1/users/167'
        r = requests.delete(url=url)
        print(r.text)
