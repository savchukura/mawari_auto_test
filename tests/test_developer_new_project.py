import time
import random
from pages.login_page import LoginPage
import os
from tests.data_for_tests import Project

from pages.user_page import NodeRunnerPage
from pages.developer_pages.my_project_page import MyProjectPage
from pages.admin_pages.admin_login_page import AdminLoginPage
from pages.admin_pages.admin_account_page import AdminAccountPage


class TestNewProjectPage:

    def test_add_new_project_valid_data(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        add_project_page = MyProjectPage(driver)
        add_project_page.click_on_add_project_button()
        # first modal window
        add_project_page.add_project_first_modal(Project.NAME, Project.CATEGORIES, Project.DESCRIPTION)
        add_project_page.click_next_button()
        # second modal window
        add_project_page.add_project_second_modal(Project.GPU, Project.CPU, Project.RAM)
        add_project_page.click_next_button_second()
        # third modal window
        add_project_page.add_project_third_modal("10")
        add_project_page.click_next_button_second()
        # fourth modal window
        add_project_page.upload_file(Project.FILE)
        add_project_page.click_upload_button()

        project_name, project_description = add_project_page.get_created_project_data()

        assert project_name == Project.NAME, "Project name incorrect"
        assert project_description == Project.DESCRIPTION, "Project description incorrect"

    def test_add_new_project_check_uploaded_file(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        add_project_page = MyProjectPage(driver)
        add_project_page.click_on_add_project_button()
        # first modal window
        add_project_page.add_project_first_modal(Project.NAME, Project.CATEGORIES, Project.DESCRIPTION)
        add_project_page.click_next_button()
        # second modal window
        add_project_page.add_project_second_modal(Project.GPU, Project.CPU, Project.RAM)
        add_project_page.click_next_button_second()
        # third modal window
        add_project_page.add_project_third_modal("10")
        add_project_page.click_next_button_second()
        # fourth modal window
        add_project_page.upload_file(Project.FILE)
        time.sleep(4)
        add_project_page.click_upload_button()
        alert_text = add_project_page.get_alert()

        assert alert_text == "Files have been uploaded"

    def test_delete_project(self, driver):
        self.test_add_new_project_valid_data(driver)

        add_project_page = MyProjectPage(driver)
        time.sleep(4)
        add_project_page.delete_project()
        alert_text = add_project_page.get_alert()
        assert alert_text == "Project deleted", "Alert incorrect"

    def test_check_search(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        add_project_page = MyProjectPage(driver)
        add_project_page.click_on_add_project_button()
        # first modal window
        add_project_page.add_project_first_modal(Project.NAME_FOR_SEARCH, Project.CATEGORIES, Project.DESCRIPTION)
        add_project_page.click_next_button()
        # second modal window
        add_project_page.add_project_second_modal(Project.GPU, Project.CPU, Project.RAM)
        add_project_page.click_next_button_second()
        # third modal window
        add_project_page.add_project_third_modal("10")
        add_project_page.click_next_button_second()
        # fourth modal window
        add_project_page.upload_file(Project.FILE)
        add_project_page.click_upload_button()
        login.log_out()

        self.test_add_new_project_valid_data(driver)

        add_project_page.search_input(Project.NAME_FOR_SEARCH)
        project_name, project_description = add_project_page.get_created_project_data()

        assert project_name == Project.NAME, "search don't work"

    def test_check_project_status_after_creation(self, driver):
        self.test_add_new_project_valid_data(driver)
        add_project_page = MyProjectPage(driver)
        project_status = add_project_page.get_project_status()

        assert project_status == "New"

    def test_check_project_status_after_admin_approve_project(self, driver):
        self.test_add_new_project_valid_data(driver)

        admin_login = AdminLoginPage(driver, "https://dev-mn-admin.zpoken.dev/login")
        admin_login.open()
        admin_login.admin_login()

        admin_account = AdminAccountPage(driver)
        admin_account.click_side_menu_tab("project tab")
        admin_account.click_on_approve_button()

        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()

        add_project_page = MyProjectPage(driver)
        project_status = add_project_page.get_project_status()

        assert project_status == "Approved"

    def test_check_project_status_after_admin_decline_project(self, driver):
        self.test_add_new_project_valid_data(driver)

        admin_login = AdminLoginPage(driver, "https://dev-mn-admin.zpoken.dev/login")
        admin_login.open()
        admin_login.admin_login()

        admin_account = AdminAccountPage(driver)
        admin_account.click_side_menu_tab("project tab")
        admin_account.click_on_decline_button()

        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()

        add_project_page = MyProjectPage(driver)
        project_status = add_project_page.get_project_status()

        assert project_status == "Declined"
