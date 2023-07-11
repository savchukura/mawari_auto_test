import time
import requests
import json
from pages.login_page import LoginPage
from pages.user_page import NodeRunnerPage
from api.activities import GetAccessToken, GetUser, Wallets


class TestCaseNew:

    def test_one(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("yura@zpoken.io", "213456qaZ", "node_runner")
        time.sleep(2)
        url = driver.current_url.split("/")[-2]
        login.log_out()
        assert url == "runners", "User log in under wrong role"

    def test_cycle(self, driver):
        for i in range(10):
            self.test_one(driver)

    def test_two(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("yura@zpoken.io", "213456qaZ", "node_runner")

        user_page = NodeRunnerPage(driver)
        user_page.click_on_tab_button("nodes list")
        user_page.click_filtering_drop()
        time.sleep(2)

    def test_auth(self):
        get_token = GetAccessToken()
        user_id, token = get_token.get_access_token_and_user_id()

        user = GetUser()
        user_data = user.get_user_data(token, user_id)
        print(user_id)

    def test_admin_auth(self):
        get_admin_token = GetAccessToken()
        admin_token = get_admin_token.get_admin_access_token()
        print(admin_token)

    def test_get_user_data(self):
        get_admin_token = GetAccessToken()
        admin_token = get_admin_token.get_admin_access_token()

        user = GetUser()
        user_data = user.get_user_data(admin_token, 429)

    def test_top_up_wallet(self):
        get_token = GetAccessToken()
        user_id, token = get_token.get_access_token_and_user_id()

        wallets = Wallets()
        top_up = wallets.top_up(token, 22, 100)

