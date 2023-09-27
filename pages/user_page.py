from pages.base_page import NextPage
from locators.user_accaunt_locators import NodeRunnerAccountLocators
from locators.user_accaunt_locators import DeveloperLocators


class NodeRunnerPage(NextPage):

    def click_on_tab_button(self, tab):
        tabs = {"dashboard": NodeRunnerAccountLocators.DASHBOARD_TAB,
                "nodes list": NodeRunnerAccountLocators.NODES_LIST_TAB,
                "rewards": NodeRunnerAccountLocators.REWARDS_TAB,
                "system alerts": NodeRunnerAccountLocators.SYSTEM_ALERTS_TAB,
                "terms and policies": NodeRunnerAccountLocators.TERMS_AND_POLICIES_TAB,
                "api keys": NodeRunnerAccountLocators.API_KEY_TAB}

        self.element_is_visible(tabs[tab]).click()

    def click_filtering_drop(self):
        self.element_is_visible(NodeRunnerAccountLocators.FILTERING_BY_DROP_DOWN).click()

        self.element_is_visible(NodeRunnerAccountLocators.PAUSED_FILTER).click()

    def totp(self):
        self.element_is_visible(NodeRunnerAccountLocators.USER_DETAIL).click()
        self.element_is_visible(NodeRunnerAccountLocators.TWO_FA_TOGGLE).click()
        totp_code = self.element_is_visible(NodeRunnerAccountLocators.TOTP_CODE)

        return totp_code.text

    def continue_fa_button(self):
        self.element_is_visible(NodeRunnerAccountLocators.CONTINUE_FA_BUTTON).click()

    def verify_totp_code(self, one, two, three, four, five, six):

        self.element_is_visible(NodeRunnerAccountLocators.VERIFY_INPUT_ONE).send_keys(one)
        self.element_is_visible(NodeRunnerAccountLocators.VERIFY_INPUT_TWO).send_keys(two)
        self.element_is_visible(NodeRunnerAccountLocators.VERIFY_INPUT_THREE).send_keys(three)
        self.element_is_visible(NodeRunnerAccountLocators.VERIFY_INPUT_FOUR).send_keys(four)
        self.element_is_visible(NodeRunnerAccountLocators.VERIFY_INPUT_FIVE).send_keys(five)
        self.element_is_visible(NodeRunnerAccountLocators.VERIFY_INPUT_SIX).send_keys(six)

    def verify_totp_before_login(self):
        self.element_is_visible(NodeRunnerAccountLocators.VERIFY_CODE_BUTTON).click()

    def verify_totp_after_login(self):
        self.element_is_visible(NodeRunnerAccountLocators.VERIFY_TWO_FA_AFTER_LOGIN).click()

    def verify_code_delete(self):
        self.element_is_visible(NodeRunnerAccountLocators.VERIFY_TWO_FA_DELETE).click()

    def get_alert(self):
        alert = self.element_is_visible(NodeRunnerAccountLocators.VALIDATION_ALERT)
        return alert.text

    def off_two_fa(self):
        self.element_is_visible(NodeRunnerAccountLocators.USER_DETAIL).click()
        self.element_is_visible(NodeRunnerAccountLocators.TWO_FA_TOGGLE_ON).click()


class DeveloperPage(NextPage):

    def click_on_tab_button(self, tab):
        tabs = {"my projects": DeveloperLocators.MY_PROJECTS_TAB,
                "streams": DeveloperLocators.STREAMS_TAB,
                "wallet": DeveloperLocators.WALLET_TAB,
                "balances": DeveloperLocators.BALANCES_TAB}

        self.element_is_visible(tabs[tab]).click()
