import time
import requests
import json

from pages.developer_pages.my_project_page import MyProjectPage
from pages.login_page import LoginPage
from pages.user_page import NodeRunnerPage
from api.activities import GetAccessToken, GetUser, Wallets
from tests.data_for_tests import Project


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

    def test_add_new_project_check_project_name_valid_data(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        add_project_page = MyProjectPage(driver)
        add_project_page.click_on_add_project_button()
        # first modal window
        add_project_page.add_project_first_modal(Project.NAME, Project.CATEGORIES, Project.DESCRIPTION)
        add_project_page.click_next_button()
        # second modal window
        add_project_page.add_project_second_modal(Project.GPU, Project.CPU, Project.RAM)
        add_project_page.click_next_button_second()
        # third modal window
        add_project_page.click_next_button_second()
        # fourth modal window
        add_project_page.upload_file(Project.TEST_FILE)
        add_project_page.click_upload_button()
        alert_text = add_project_page.get_alert()
        add_project_page.refresh_page()
        time.sleep(1)

        data = add_project_page.get_all_project_data()

        print(data[0])
        print(data[1])
        print(data[2])
        print(data[3])
        print(data[4])

    def test_get_current_time(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()
        add_project_page = MyProjectPage(driver)
        current_date = add_project_page.get_current_date()
        print(current_date)

