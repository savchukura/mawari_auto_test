from pages.base_page import NextPage
from locators.user_accaunt_locators import DeveloperLocators


class DeveloperPage(NextPage):

    def click_on_tab_button(self, tab):
        tabs = {"my project": DeveloperLocators.MY_PROJECTS_TAB,
                "manage account": DeveloperLocators.MANAGE_ACCOUNT_TAB,
                "api and documentation": DeveloperLocators.API_AND_DOCUMENTATION_TAB,
                "balances": DeveloperLocators.BALANCES_TAB}

        self.element_is_visible(tabs[tab]).click()

    # My Project page

    def click_on_add_project_button(self):
        self.element_is_visible(DeveloperLocators.ADD_PROJECT_BUTTON).click()

    def create_project(self, project_name, project_category, project_description, file_path):
        self.element_is_visible(DeveloperLocators.PROJECT_NAME_INPUT).send_keys(project_name)
        self.element_is_visible(DeveloperLocators.PROJECT_CATEGORY_INPUT).send_keys(project_category)
        self.element_is_visible(DeveloperLocators.PROJECT_DESCRIPTION_TEXTAREA).send_keys(project_description)
        self.element_is_visible(DeveloperLocators.FILE_INPUT).send_keys(file_path)

    def click_upload_button(self):
        self.element_is_visible(DeveloperLocators.UPLOAD_BUTTON).click()

    def click_cancel_button(self):
        self.element_is_visible(DeveloperLocators.CANCEL_BUTTON).click()

