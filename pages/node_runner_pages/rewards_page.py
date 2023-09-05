from pages.base_page import NextPage
from locators.node_runner.rewards_page_locators import RewardsPageLocators
from selenium.webdriver import Keys


class RewardsPage(NextPage):

    def check_balance(self):
        balance = self.element_is_visible(RewardsPageLocators.BALANCE_FIELD).text
        return balance.replace("$", '').replace(',', '')

    def click_on_withdraw_button_on_page(self):
        self.element_is_visible(RewardsPageLocators.WITHDRAW_BUTTON).click()

    def fill_amount_field(self, amount):
        self.element_is_visible(RewardsPageLocators.AMOUNT_INPUT).send_keys(amount)

    def click_on_withdraw_button_in_modal(self):
        self.element_is_visible(RewardsPageLocators.WITHDRAW_IN_MODAL_BUTTON).click()

    def check_disabled_withdraw_button(self):
        self.element_is_visible(RewardsPageLocators.DISABLE_WITHDRAW_IN_MODAL_BUTTON)

    def get_alert(self):
        alert = self.element_is_visible(RewardsPageLocators.ALERT).text
        return alert

    def refresh_page_one(self):
        self.refresh_page()

    def click_on_amount_input(self):
        self.element_is_visible(RewardsPageLocators.AMOUNT_INPUT).click()
        self.element_is_visible(RewardsPageLocators.AMOUNT_INPUT).send_keys(Keys.TAB)

    def get_error_message_from_amount_input(self):
        error_text = self.element_is_visible(RewardsPageLocators.AMOUNT_INPUT_ERROR).text
        return error_text

    def get_amount_input_text(self):
        amount_input_text = self.element_is_visible(RewardsPageLocators.AMOUNT_INPUT).get_attribute('value')
        return amount_input_text
