from pages.base_page import NextPage
from locators.admin.admin_account_page_locators import AdminAccountPageLocators


class AdminAccountPage(NextPage):

    def click_side_menu_tab(self, tab):
        side_menu_tabs = {"dashboard tab": AdminAccountPageLocators.DASHBOARD_TAB,
                          "admins tab": AdminAccountPageLocators.ADMINS_TAB,
                          "alerts tab": AdminAccountPageLocators.ALERTS_TAB,
                          "project tab": AdminAccountPageLocators.PROJECTS_TAB,
                          "developers tab": AdminAccountPageLocators.XR_DEVELOPERS_LIST_TAB}
        self.element_is_visible(side_menu_tabs[tab]).click()

    # Project tab

    def click_on_approve_button(self):
        self.element_is_visible(AdminAccountPageLocators.FIRST_APPROVE_BUTTON).click()

    def click_on_decline_button(self):
        self.element_is_visible(AdminAccountPageLocators.FIRST_DECLINE_BUTTON).click()
