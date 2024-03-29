from pages.developer_pages.balance_page import BalancePage
from pages.user_page import DeveloperPage
from pages.login_page import LoginPage
import time
from tests.data_for_tests import Url


class TestBalancePage:

    def test_make_deposit(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        user_page = DeveloperPage(driver)
        user_page.click_on_tab_button("wallet")

        balance_page = BalancePage(driver)
        balance_before_deposit = balance_page.get_balance_count()
        balance_page.click_on_deposit_button()
        deposit_amount = '55.55'
        balance_page.enter_deposit_amount(deposit_amount)
        time.sleep(1)
        balance_page.click_deposit_button_in_modal()
        balance_page.stripe("savcukura866@gmail.com", '4242424242424242', '1224', '123', "name surname")
        balance_page.get_balance_count()
        expected_balance_after = float(balance_before_deposit) + float(deposit_amount)
        balance_page.refresh_page_one()
        time.sleep(1)
        balance_after_deposit = balance_page.get_balance_count()

        assert round(expected_balance_after, 2) == float(balance_after_deposit), "deposit wrong"

    def test_check_description_after_transaction(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        user_page = DeveloperPage(driver)
        user_page.click_on_tab_button("wallet")

        balance_page = BalancePage(driver)

        balance_page.click_on_deposit_button()

        balance_page.enter_deposit_amount('50')
        time.sleep(1)
        balance_page.click_deposit_button_in_modal()
        balance_page.stripe("savcukura866@gmail.com", '4242424242424242', '1224', '123', "name surname")
        balance_page.get_balance_count()

        balance_page.refresh_page_one()
        time.sleep(1)
        description = balance_page.get_transaction_info(0)
        assert "Top up wallet" in description

    def test_check_amount_after_transaction(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        user_page = DeveloperPage(driver)
        user_page.click_on_tab_button("wallet")

        balance_page = BalancePage(driver)

        balance_page.click_on_deposit_button()

        balance_page.enter_deposit_amount('60')
        time.sleep(1)
        balance_page.click_deposit_button_in_modal()
        balance_page.stripe("savcukura866@gmail.com", '4242424242424242', '1224', '123', "name surname")
        balance_page.get_balance_count()

        balance_page.refresh_page_one()
        time.sleep(1)
        amount = balance_page.get_transaction_info(1)
        assert round(amount, 2) == '60'

    def test_make_deposit_less_than_one_dollar(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        user_page = DeveloperPage(driver)
        user_page.click_on_tab_button("wallet")

        balance_page = BalancePage(driver)
        balance_before_deposit = balance_page.get_balance_count()
        balance_page.click_on_deposit_button()
        deposit_amount = 0.99
        balance_page.enter_deposit_amount(deposit_amount)
        time.sleep(1)
        balance_page.click_deposit_button_in_modal()
        balance_page.stripe("savcukura866@gmail.com", '4242424242424242', '1224', '123', "name surname")
        balance_page.get_balance_count()
        expected_balance_after = float(balance_before_deposit) + float(deposit_amount)
        balance_page.refresh_page_one()
        time.sleep(1)
        balance_after_deposit = balance_page.get_balance_count()

        assert round(expected_balance_after, 2) == float(balance_after_deposit), "deposit wrong"

    def test_make_deposit_minimum(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        user_page = DeveloperPage(driver)
        user_page.click_on_tab_button("wallet")

        balance_page = BalancePage(driver)
        balance_before_deposit = balance_page.get_balance_count()
        balance_page.click_on_deposit_button()
        deposit_amount = 0.01
        balance_page.enter_deposit_amount(deposit_amount)
        time.sleep(1)
        balance_page.click_deposit_button_in_modal()
        balance_page.stripe("savcukura866@gmail.com", '4242424242424242', '1224', '123', "name surname")
        balance_page.get_balance_count()
        expected_balance_after = float(balance_before_deposit) + float(deposit_amount)
        balance_page.refresh_page_one()
        time.sleep(1)
        balance_after_deposit = balance_page.get_balance_count()

        assert round(expected_balance_after, 2) == float(balance_after_deposit), "deposit wrong"

    def test_leave_amount_field_empty(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        user_page = DeveloperPage(driver)
        user_page.click_on_tab_button("wallet")

        balance_page = BalancePage(driver)
        balance_page.click_on_deposit_button()
        deposit_amount = ' '
        balance_page.click_on_amount_input()
        balance_page.enter_deposit_amount(deposit_amount)
        error_message = balance_page.get_error()

        assert error_message == "Amount is required"

    def test_enter_zero_in_amount_field(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        user_page = DeveloperPage(driver)
        user_page.click_on_tab_button("wallet")

        balance_page = BalancePage(driver)
        balance_page.click_on_deposit_button()
        deposit_amount = 0
        balance_page.click_on_amount_input()
        balance_page.enter_deposit_amount(deposit_amount)
        error_message = balance_page.get_error()

        assert error_message == "amount must be greater than or equal to 0.01"

    def test_fill_in_amount_input_symbols(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        user_page = DeveloperPage(driver)
        user_page.click_on_tab_button("wallet")

        balance_page = BalancePage(driver)
        balance_page.click_on_deposit_button()
        deposit_amount = 'abc !@#$%^&*()'
        balance_page.click_on_amount_input()
        balance_page.enter_deposit_amount(deposit_amount)
        value_input_text = balance_page.get_amount_input_text()

        assert value_input_text == ""

    def test_fill_in_amount_input_negative_values(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        user_page = DeveloperPage(driver)
        user_page.click_on_tab_button("wallet")

        balance_page = BalancePage(driver)
        balance_page.click_on_deposit_button()
        deposit_amount = '-10'
        balance_page.click_on_amount_input()
        balance_page.enter_deposit_amount(deposit_amount)
        value_input_text = balance_page.get_amount_input_text()

        assert value_input_text == "10"
