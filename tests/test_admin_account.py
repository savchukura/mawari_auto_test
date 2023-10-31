from pages.admin_pages.admin_login_page import AdminLoginPage
from pages.admin_pages.admin_account_page import AdminAccountPage
import allure
import time
from tests.data_for_tests import Url


@allure.suite('Admin account tests')
class TestAdminAccount:

    @allure.feature('Dashboard page tests')
    class TestDashboardPage:

        @allure.title('Check Node runners count')
        def test_check_node_runners_count(self, driver):
            admin_login = AdminLoginPage(driver, Url.ADMIN_URL)
            admin_login.open()
            admin_login.login_enter_email_and_password('alex+i@zpoken.io', '12345678')
            admin_login.login_click_sign_in_button()

            admin_account = AdminAccountPage(driver)
            node_runners_counts_on_dashboard = admin_account.get_indicators(0)
            admin_account.click_side_menu_tab("node runners tab")

            node_runners_counts_on_nodes_runners_tab = admin_account.count_node_runners()

            assert node_runners_counts_on_dashboard == node_runners_counts_on_nodes_runners_tab, "invalid node runners count"

        @allure.title('Check navigate from dashboard to node runners tab')
        def test_check_navigate_to_node_runners_page(self, driver):
            admin_login = AdminLoginPage(driver, Url.ADMIN_URL)
            admin_login.open()
            admin_login.login_enter_email_and_password('alex+i@zpoken.io', '12345678')
            admin_login.login_click_sign_in_button()

            admin_account = AdminAccountPage(driver)
            admin_account.click_on_indicators_button(0)
            url = driver.current_url.split("/")[0]
            assert url == "node_runners", "wrong page"

        @allure.title('Check Nodes count')
        def test_check_nodes_count(self, driver):
            admin_login = AdminLoginPage(driver, Url.ADMIN_URL)
            admin_login.open()
            admin_login.login_enter_email_and_password('alex+i@zpoken.io', '12345678')
            admin_login.login_click_sign_in_button()

            admin_account = AdminAccountPage(driver)
            nodes_counts_on_dashboard = admin_account.get_indicators(1)
            admin_account.click_side_menu_tab("nodes tab")

            node_runners_counts_on_nodes_runners_tab = admin_account.count_nodes()

            assert nodes_counts_on_dashboard == node_runners_counts_on_nodes_runners_tab, "invalid nodes count"

        @allure.title('Check navigate from dashboard to nodes tab')
        def test_check_navigate_to_nodes_page(self, driver):
            admin_login = AdminLoginPage(driver, Url.ADMIN_URL)
            admin_login.open()
            admin_login.login_enter_email_and_password('alex+i@zpoken.io', '12345678')
            admin_login.login_click_sign_in_button()

            admin_account = AdminAccountPage(driver)
            admin_account.click_on_indicators_button(1)
            url = driver.current_url.split("/")[-1]
            assert url == "nodes", "wrong page"

        @allure.title('Check Node runners balances')
        def test_check_node_runners_balances(self, driver):
            admin_login = AdminLoginPage(driver, Url.ADMIN_URL)
            admin_login.open()
            admin_login.login_enter_email_and_password('alex+i@zpoken.io', '12345678')
            admin_login.login_click_sign_in_button()

            admin_account = AdminAccountPage(driver)
            node_runners_balance_counts_on_dashboard = admin_account.get_indicators(2)

            admin_account.click_side_menu_tab("node runners tab")

            node_runners_balance_on_nodes_runners_tab = sum(admin_account.count_node_runners_balance())
            assert round(node_runners_balance_on_nodes_runners_tab, 2) == round(node_runners_balance_counts_on_dashboard, 2), "invalid balances"

        @allure.title('Check XR DEVELOPERS count')
        def test_check_xr_developers_count(self, driver):
            admin_login = AdminLoginPage(driver, Url.ADMIN_URL)
            admin_login.open()
            admin_login.login_enter_email_and_password('alex+i@zpoken.io', '12345678')
            admin_login.login_click_sign_in_button()

            admin_account = AdminAccountPage(driver)
            developers_counts_on_dashboard = admin_account.get_indicators(3)
            admin_account.click_side_menu_tab("developers tab")

            developers_counts_on_developers_tab = admin_account.count_node_runners()

            assert developers_counts_on_dashboard == developers_counts_on_developers_tab, "invalid developers count"

        @allure.title('Check navigate from dashboard to Xr developers list tab')
        def test_check_navigate_to_developers_page(self, driver):
            admin_login = AdminLoginPage(driver, Url.ADMIN_URL)
            admin_login.open()
            admin_login.login_enter_email_and_password('alex+i@zpoken.io', '12345678')
            admin_login.login_click_sign_in_button()

            admin_account = AdminAccountPage(driver)
            admin_account.click_on_indicators_button(2)
            url = driver.current_url.split("/")[-1]
            assert url == "developers", "wrong page"

        @allure.title('Check Projects count')
        def test_check_projects_count(self, driver):
            admin_login = AdminLoginPage(driver, Url.ADMIN_URL)
            admin_login.open()
            admin_login.login_enter_email_and_password('alex+i@zpoken.io', '12345678')
            admin_login.login_click_sign_in_button()

            admin_account = AdminAccountPage(driver)
            projects_counts_on_dashboard = admin_account.get_indicators(4)
            admin_account.click_side_menu_tab("project tab")

            projects_counts_on_projects_tab = admin_account.count_nodes()

            assert projects_counts_on_dashboard == projects_counts_on_projects_tab, "invalid projects count"

        @allure.title('Check Developers balances')
        def test_check_developers_balances(self, driver):
            admin_login = AdminLoginPage(driver, Url.ADMIN_URL)
            admin_login.open()
            admin_login.login_enter_email_and_password('alex+i@zpoken.io', '12345678')
            admin_login.login_click_sign_in_button()

            admin_account = AdminAccountPage(driver)
            developers_balance_counts_on_dashboard = admin_account.get_indicators(5)

            admin_account.click_side_menu_tab("developers tab")

            developers_balance_on_nodes_runners_tab = sum(admin_account.count_node_runners_balance())
            assert round(developers_balance_on_nodes_runners_tab, 2) == round(
                developers_balance_counts_on_dashboard, 2), "invalid balances"

        @allure.title('Check Streams count')
        def test_check_streams_count(self, driver):
            admin_login = AdminLoginPage(driver, Url.ADMIN_URL)
            admin_login.open()
            admin_login.login_enter_email_and_password('alex+i@zpoken.io', '12345678')
            admin_login.login_click_sign_in_button()

            admin_account = AdminAccountPage(driver)
            streams_counts_on_dashboard = admin_account.get_streams_count()
            admin_account.click_side_menu_tab("streams tab")

            streams_counts_on_streams_tab = admin_account.count_nodes()

            assert int(streams_counts_on_dashboard) == streams_counts_on_streams_tab, "invalid streams count"
