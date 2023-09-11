import time

from pages.base_page import NextPage
from locators.admin.admin_account_page_locators import AdminAccountPageLocators
import base64
import os
import random
import zipfile
import requests
import shutil


class AdminAccountPage(NextPage):

    # Dashboard
    def get_dashboard_title(self):
        dashboard_title_text = self.element_is_visible(AdminAccountPageLocators.DASHBOARD_TITLE)
        return dashboard_title_text.text

    def click_side_menu_tab(self, tab):
        side_menu_tabs = {"dashboard tab": AdminAccountPageLocators.DASHBOARD_TAB,
                          "admins tab": AdminAccountPageLocators.ADMINS_TAB,
                          "alerts tab": AdminAccountPageLocators.ALERTS_TAB,
                          "project tab": AdminAccountPageLocators.PROJECTS_TAB,
                          "developers tab": AdminAccountPageLocators.XR_DEVELOPERS_LIST_TAB}
        self.element_is_visible(side_menu_tabs[tab]).click()

    def click_log_out_button(self):
        self.element_is_clickable(AdminAccountPageLocators.LOG_OUT_BUTTON).click()

    # Project tab

    def click_on_approve_button(self):
        self.element_is_visible(AdminAccountPageLocators.FIRST_APPROVE_BUTTON).click()

    def click_on_decline_button(self):
        self.element_is_visible(AdminAccountPageLocators.FIRST_DECLINE_BUTTON).click()

    def get_project_href(self):
        confirm_download = self.elements_are_visible(AdminAccountPageLocators.CONFIRM_DOWNLOAD_BUTTON)
        confirm_download[0].click()
        time.sleep(15)
        link = self.element_is_visible(AdminAccountPageLocators.DOWNLOAD_BUTTON).get_attribute('href')
        return link

    def download_file(self):
        global file_in_archive
        confirm_download = self.elements_are_visible(AdminAccountPageLocators.CONFIRM_DOWNLOAD_BUTTON)
        confirm_download[0].click()
        time.sleep(12)
        link = self.element_is_visible(AdminAccountPageLocators.DOWNLOAD_BUTTON).get_attribute('href')
        response = requests.get(link, stream=True)
        response.raise_for_status()
        # Extract the filename from the URL
        file_name = link.split('/')[-1]
        # Save the zip file to the specified folder
        save_path = os.path.join("../tests/files/", file_name)
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        zip = zipfile.ZipFile(os.path.abspath(save_path))

        file_in_archive = zip.namelist()

        return file_in_archive, save_path

    @staticmethod
    def remove_file(save_path):
        os.remove(save_path)
