from pages.developer_pages.balance_page import BalancePage
from pages.user_page import DeveloperPage
from pages.login_page import LoginPage
import time


class TestBalancePage:

    def test_make_deposit(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        user_page = DeveloperPage(driver)
        user_page.click_on_tab_button("balances")

        balance_page = BalancePage(driver)
        balance_before_deposit = balance_page.get_balance_count()
        balance_page.click_on_deposit_button()
        deposit_amount = '55.55'
        balance_page.enter_deposit_amount(deposit_amount)
        time.sleep(1)
        balance_page.click_deposit_button_in_modal()
        balance_page.refresh_page_one()
        time.sleep(1)
        balance_after_deposit = balance_page.get_balance_count()

        assert float(balance_before_deposit) + float(deposit_amount) == float(balance_after_deposit), "deposit wrong"


