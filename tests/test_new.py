import time

from pages.login_page import LoginPage
from pages.user_page import NodeRunnerPage


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

    def test_three(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        time.sleep(2)
        login.log_in("", "213456qaZ", "node_runner")

        message = login.get_email_validate_error()
        print(message)
