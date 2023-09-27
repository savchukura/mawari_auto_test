from selenium.webdriver import Keys

from pages.base_page import NextPage
from locators.developer.balance_page_locators import BalancePageLocators


class BalancePage(NextPage):

    def get_balance_count(self):
        balance = self.element_is_visible(BalancePageLocators.BALANCE_COUNT, 15).text
        return balance.replace("$", '').replace(",", "")

    def click_on_deposit_button(self):
        self.element_is_visible(BalancePageLocators.DEPOSIT_BUTTON).click()

    def enter_deposit_amount(self, deposit_amount):
        self.element_is_visible(BalancePageLocators.DEPOSIT_INPUT).send_keys(deposit_amount)

    def click_deposit_button_in_modal(self):
        self.element_is_visible(BalancePageLocators.DEPOSIT_IN_MODAL_BUTTON).click()

    def refresh_page_one(self):
        self.refresh_page()

    def get_error(self):
        error = self.element_is_visible(BalancePageLocators.ERROR).text
        return error

    def click_on_amount_input(self):
        self.element_is_visible(BalancePageLocators.DEPOSIT_INPUT).click()
        self.element_is_visible(BalancePageLocators.DEPOSIT_INPUT).send_keys(Keys.TAB)

    def get_amount_input_text(self):
        amount_input_text = self.element_is_visible(BalancePageLocators.DEPOSIT_INPUT).get_attribute('value')
        return amount_input_text

    def stripe(self, email, card_number, mm_yy, cvc, holder_name):
        self.element_is_visible(BalancePageLocators.EMAIL_INPUT).send_keys(email)
        #self.element_is_visible(BalancePageLocators.CARD_BUTTON).click()
        self.element_is_visible(BalancePageLocators.CARD_NUMBER_INPUT).send_keys(card_number)
        self.element_is_visible(BalancePageLocators.MM_YY).send_keys(mm_yy)
        self.element_is_visible(BalancePageLocators.CVC).send_keys(cvc)
        self.element_is_visible(BalancePageLocators.CARD_HOLDER_NAME_INPUT).send_keys(holder_name)

        self.element_is_visible(BalancePageLocators.PAY_BUTTON).click()