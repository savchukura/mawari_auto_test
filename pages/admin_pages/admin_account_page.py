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

    def get_indicators(self, indicator_count):
        indicators = self.elements_are_visible(AdminAccountPageLocators.INDICATORS)
        indicator = indicators[indicator_count].text.replace('$', '').replace(',', '')
        return float(indicator)

    def get_streams_count(self):
        streams_count = self.elements_are_visible(AdminAccountPageLocators.STREAMS_COUNT)
        stream_count = streams_count[1]
        return stream_count.text

    def click_on_indicators_button(self, indicator_count):
        indicators = self.elements_are_visible(AdminAccountPageLocators.INDICATORS_BUTTON)
        indicator = indicators[indicator_count]
        indicator.click()

    def click_side_menu_tab(self, tab):
        side_menu_tabs = {"dashboard tab": AdminAccountPageLocators.DASHBOARD_TAB,
                          "admins tab": AdminAccountPageLocators.ADMINS_TAB,
                          "streams tab": AdminAccountPageLocators.STREAMS_TAB,
                          "project tab": AdminAccountPageLocators.PROJECTS_TAB,
                          "developers tab": AdminAccountPageLocators.XR_DEVELOPERS_LIST_TAB,
                          "node runners tab": AdminAccountPageLocators.NODE_RUNNERS_TAB,
                          "nodes tab": AdminAccountPageLocators.NODES_TAB,
                          "validators tab": AdminAccountPageLocators.VALIDATORS_TAB,
                          "settings tab": AdminAccountPageLocators.SETTINGS_TAB}
        self.element_is_visible(side_menu_tabs[tab]).click()

    def click_log_out_button(self):
        self.element_is_clickable(AdminAccountPageLocators.LOG_OUT_BUTTON).click()

    # Admins tab

    # Streams tab

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

    # Developers tab

    # Node runners tab

    def count_node_runners(self):
        node_runners = self.elements_are_present(AdminAccountPageLocators.COUNT_OF_NODE_RUNNERS)
        node_runners_count = len(node_runners)
        return node_runners_count

    def count_node_runners_balance(self):

        node_runner_rows = self.elements_are_present(AdminAccountPageLocators.COUNT_OF_NODE_RUNNERS)
        node_runners_balance = []
        for balance in node_runner_rows:
            node_runners_balance.append(float(balance.text.split('$')[1].replace(',', '')))
        return node_runners_balance
    # Nodes tab

    def count_nodes(self):
        nodes = self.elements_are_present(AdminAccountPageLocators.COUNT_OF_NODES)
        nodes_count = len(nodes)
        return nodes_count

    # Validators tab

    # Settings tab

