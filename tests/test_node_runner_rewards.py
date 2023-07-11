import time
from pages.user_page import NodeRunnerPage
from pages.login_page import LoginPage
from pages.node_runner_pages.rewards_page import RewardsPage
from api.activities import GetAccessToken, Wallets


class TestRewardsPage:

    def test_do_withdraw_valid_data(self, driver):
        # top up node runner wallet
        get_token = GetAccessToken()
        user_id, token = get_token.get_access_token_and_user_id()
        wallets = Wallets()
        wallets.top_up(token, 22, 100)
        # Execute test
        # Login
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "node_runner")
        login.click_sign_in_button()
        # go to rewards page
        user_page = NodeRunnerPage(driver)
        user_page.click_on_tab_button("rewards")
        # Rewards page
        rewards_page = RewardsPage(driver)
        balance_before_withdraw = rewards_page.check_balance()
        rewards_page.click_on_withdraw_button_on_page()
        amount_for_withdraw = float(balance_before_withdraw) / 2
        rewards_page.fill_amount_field(amount_for_withdraw)
        time.sleep(1)
        rewards_page.click_on_withdraw_button_in_modal()
        expected_balance_after_withdraw = float(balance_before_withdraw) - float(amount_for_withdraw)
        rewards_page.refresh_page()
        time.sleep(1)
        balance_after_withdraw = rewards_page.check_balance()
        assert round(expected_balance_after_withdraw, 2) == float(balance_after_withdraw), "withdraw wrong"

    def test_do_withdraw_minimum_valid_data(self, driver):
        # top up node runner wallet
        get_token = GetAccessToken()
        user_id, token = get_token.get_access_token_and_user_id()
        wallets = Wallets()
        wallets.top_up(token, 22, 100)
        # Execute test
        # Login
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "node_runner")
        login.click_sign_in_button()
        # go to rewards page
        user_page = NodeRunnerPage(driver)
        user_page.click_on_tab_button("rewards")
        # Rewards page
        rewards_page = RewardsPage(driver)
        balance_before_withdraw = rewards_page.check_balance()
        rewards_page.click_on_withdraw_button_on_page()
        amount_for_withdraw = 0.01
        rewards_page.fill_amount_field(amount_for_withdraw)
        time.sleep(1)
        rewards_page.click_on_withdraw_button_in_modal()
        expected_balance_after_withdraw = float(balance_before_withdraw) - float(amount_for_withdraw)
        rewards_page.refresh_page()
        time.sleep(1)
        balance_after_withdraw = rewards_page.check_balance()
        assert round(expected_balance_after_withdraw, 2) == float(balance_after_withdraw), "withdraw wrong"

    def test_do_withdraw_maximum_valid_data(self, driver):
        # top up node runner wallet
        get_token = GetAccessToken()
        user_id, token = get_token.get_access_token_and_user_id()
        wallets = Wallets()
        wallets.top_up(token, 22, 100)
        # Execute test
        # Login
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "node_runner")
        login.click_sign_in_button()
        # go to rewards page
        user_page = NodeRunnerPage(driver)
        user_page.click_on_tab_button("rewards")
        # Rewards page
        rewards_page = RewardsPage(driver)
        balance_before_withdraw = rewards_page.check_balance()
        rewards_page.click_on_withdraw_button_on_page()
        amount_for_withdraw = float(balance_before_withdraw)
        rewards_page.fill_amount_field(amount_for_withdraw)
        time.sleep(1)
        rewards_page.click_on_withdraw_button_in_modal()
        rewards_page.refresh_page()
        time.sleep(1)
        balance_after_withdraw = rewards_page.check_balance()
        assert float(balance_after_withdraw) == 0, "withdraw wrong"

    def test_do_withdraw_check_alert_after_withdraw_valid_data(self, driver):
        # top up node runner wallet
        get_token = GetAccessToken()
        user_id, token = get_token.get_access_token_and_user_id()
        wallets = Wallets()
        wallets.top_up(token, 22, 100)
        # Execute test
        # Login
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "node_runner")
        login.click_sign_in_button()
        # go to rewards page
        user_page = NodeRunnerPage(driver)
        user_page.click_on_tab_button("rewards")
        # Rewards page
        rewards_page = RewardsPage(driver)
        balance_before_withdraw = rewards_page.check_balance()
        rewards_page.click_on_withdraw_button_on_page()
        amount_for_withdraw = float(balance_before_withdraw) / 2
        rewards_page.fill_amount_field(amount_for_withdraw)
        time.sleep(1)
        rewards_page.click_on_withdraw_button_in_modal()
        alert = rewards_page.get_alert()
        assert alert == 'Success', 'wrong alert'

    def test_do_withdraw_leave_amount_field_empty_invalid_data(self, driver):
        # top up node runner wallet
        get_token = GetAccessToken()
        user_id, token = get_token.get_access_token_and_user_id()
        wallets = Wallets()
        wallets.top_up(token, 22, 10)
        # Execute test
        # Login
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "node_runner")
        login.click_sign_in_button()
        # go to rewards page
        user_page = NodeRunnerPage(driver)
        user_page.click_on_tab_button("rewards")
        # Rewards page
        rewards_page = RewardsPage(driver)
        rewards_page.click_on_withdraw_button_on_page()
        rewards_page.click_on_amount_input()
        error = rewards_page.get_error_message_from_amount_input()

        assert error == "Amount is required", 'error not visible'

    def test_do_withdraw_in_amount_field_enter_zero_invalid_data(self, driver):
        # top up node runner wallet
        get_token = GetAccessToken()
        user_id, token = get_token.get_access_token_and_user_id()
        wallets = Wallets()
        wallets.top_up(token, 22, 10)
        # Execute test
        # Login
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "node_runner")
        login.click_sign_in_button()
        # go to rewards page
        user_page = NodeRunnerPage(driver)
        user_page.click_on_tab_button("rewards")
        # Rewards page
        rewards_page = RewardsPage(driver)
        rewards_page.click_on_withdraw_button_on_page()
        rewards_page.fill_amount_field(0)
        rewards_page.click_on_amount_input()
        time.sleep(1)
        error = rewards_page.get_error_message_from_amount_input()

        assert error == "amount must be greater than or equal to 0.01", 'error not visible'

    def test_do_withdraw_in_amount_field_enter_more_than_user_has_on_balance_invalid_data(self, driver):
        # top up node runner wallet
        get_token = GetAccessToken()
        user_id, token = get_token.get_access_token_and_user_id()
        wallets = Wallets()
        wallets.top_up(token, 22, 10)
        # Execute test
        # Login
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "node_runner")
        login.click_sign_in_button()
        # go to rewards page
        user_page = NodeRunnerPage(driver)
        user_page.click_on_tab_button("rewards")
        # Rewards page
        rewards_page = RewardsPage(driver)
        balance_before_withdraw = rewards_page.check_balance()
        rewards_page.click_on_withdraw_button_on_page()
        amount_for_withdraw = float(balance_before_withdraw) + 0.01
        rewards_page.fill_amount_field(amount_for_withdraw)
        disable_button = rewards_page.check_disabled_withdraw_button()
        assert disable_button is None

    def test_do_withdraw_in_amount_field_enter_symbols_invalid_data(self, driver):
        # top up node runner wallet
        get_token = GetAccessToken()
        user_id, token = get_token.get_access_token_and_user_id()
        wallets = Wallets()
        wallets.top_up(token, 22, 10)
        # Execute test
        # Login
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "node_runner")
        login.click_sign_in_button()
        # go to rewards page
        user_page = NodeRunnerPage(driver)
        user_page.click_on_tab_button("rewards")
        # Rewards page
        rewards_page = RewardsPage(driver)
        rewards_page.click_on_withdraw_button_on_page()
        rewards_page.fill_amount_field('abc !@#$%^&*()')
        get_value_from_input = rewards_page.get_amount_input_text()
        assert get_value_from_input == ''

    def test_do_withdraw_in_amount_field_enter_negative_values_invalid_data(self, driver):
        # top up node runner wallet
        get_token = GetAccessToken()
        user_id, token = get_token.get_access_token_and_user_id()
        wallets = Wallets()
        wallets.top_up(token, 22, 10)
        # Execute test
        # Login
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "node_runner")
        login.click_sign_in_button()
        # go to rewards page
        user_page = NodeRunnerPage(driver)
        user_page.click_on_tab_button("rewards")
        # Rewards page
        rewards_page = RewardsPage(driver)
        rewards_page.click_on_withdraw_button_on_page()
        rewards_page.fill_amount_field('-10')
        get_value_from_input = rewards_page.get_amount_input_text()
        assert get_value_from_input == '10'





