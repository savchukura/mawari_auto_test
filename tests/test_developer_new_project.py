import time
import random
from datetime import datetime
from pages.developer_pages.balance_page import BalancePage
from pages.login_page import LoginPage
import os
from tests.data_for_tests import Project, Url
import allure
from pages.user_page import NodeRunnerPage, DeveloperPage
from pages.developer_pages.my_project_page import MyProjectPage
from pages.admin_pages.admin_login_page import AdminLoginPage
from pages.admin_pages.admin_account_page import AdminAccountPage
#from conftest import *


@allure.feature('Create New Project')
class TestNewProjectPage:
    @allure.title('Create Project valid data')
    def test_add_new_project_valid_data_check_creating_project(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        add_project_page = MyProjectPage(driver)
        add_project_page.click_on_add_project_button()
        # first modal window
        add_project_page.add_project_first_modal(Project.NAME, Project.CATEGORIES, Project.REGIONS, Project.DESCRIPTION)
        add_project_page.click_next_button()
        # second modal window
        add_project_page.add_project_second_modal(Project.GPU, Project.CPU, Project.RAM)
        add_project_page.click_next_button_second()
        # third modal window
        add_project_page.click_next_button_second()
        # fourth modal window
        add_project_page.upload_file(Project.TEST_FILE)
        add_project_page.click_upload_button()

        alert_text = add_project_page.get_alert()
        add_project_page.refresh_page()
        time.sleep(1)

        # project_name, project_description = add_project_page.get_created_project_data()

        assert alert_text == "Create success"

        # assert project_name == Project.NAME, "Project name incorrect"
        # assert project_description == Project.DESCRIPTION, "Project description incorrect"

    @allure.title('Create Project On-Demand off')
    def test_add_new_project_on_demand_off_valid_data(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        # top up the User Balance before creating project
        user_page = DeveloperPage(driver)
        user_page.click_on_tab_button("wallet")
        balance_page = BalancePage(driver)
        balance_page.click_on_deposit_button()
        deposit_amount = '100'
        balance_page.enter_deposit_amount(deposit_amount)
        time.sleep(1)
        balance_page.click_deposit_button_in_modal()
        balance_page.stripe("savcukura866@gmail.com", '4242424242424242', '1224', '123', "name surname")
        balance_page.get_balance_count()

        user_page.click_on_tab_button("my projects")
        time.sleep(4)

        add_project_page = MyProjectPage(driver)
        add_project_page.click_on_add_project_button()
        # first modal window
        add_project_page.add_project_first_modal(Project.NAME, Project.CATEGORIES, Project.REGIONS, Project.DESCRIPTION)
        add_project_page.click_next_button()
        # second modal window
        add_project_page.add_project_second_modal(Project.GPU, Project.CPU, Project.RAM)
        add_project_page.click_next_button_second()
        # third modal window
        add_project_page.add_project_third_modal("100")
        add_project_page.click_next_button_second()
        # fourth modal window
        add_project_page.upload_file(Project.TEST_FILE)
        add_project_page.click_upload_button()

        alert_text = add_project_page.get_alert()
        add_project_page.refresh_page()
        time.sleep(1)

        assert alert_text == "Create success", "The Project has not created"

    @allure.title('Check Project ID after Creating')
    def test_add_new_project_check_project_id_valid_data(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        add_project_page = MyProjectPage(driver)
        add_project_page.click_on_add_project_button()
        # first modal window
        add_project_page.add_project_first_modal(Project.NAME, Project.CATEGORIES, Project.REGIONS, Project.DESCRIPTION)
        add_project_page.click_next_button()
        # second modal window
        add_project_page.add_project_second_modal(Project.GPU, Project.CPU, Project.RAM)
        add_project_page.click_next_button_second()
        # third modal window
        add_project_page.click_next_button_second()
        # fourth modal window
        add_project_page.upload_file(Project.TEST_FILE)
        add_project_page.click_upload_button()

        alert_text = add_project_page.get_alert()
        add_project_page.refresh_page()
        time.sleep(1)
        project_id = add_project_page.get_created_project_id()

        assert project_id is not None, "Project id incorrect"

    @allure.title('Check Project name after creating')
    def test_add_new_project_check_project_name_valid_data(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        add_project_page = MyProjectPage(driver)
        add_project_page.click_on_add_project_button()
        # first modal window
        add_project_page.add_project_first_modal(Project.NAME, Project.CATEGORIES, Project.REGIONS, Project.DESCRIPTION)
        add_project_page.click_next_button()
        # second modal window
        add_project_page.add_project_second_modal(Project.GPU, Project.CPU, Project.RAM)
        add_project_page.click_next_button_second()
        # third modal window
        add_project_page.click_next_button_second()
        # fourth modal window
        add_project_page.upload_file(Project.TEST_FILE)
        add_project_page.click_upload_button()

        alert_text = add_project_page.get_alert()
        add_project_page.refresh_page()
        time.sleep(1)
        project_name = add_project_page.get_created_project_name()

        assert project_name == Project.NAME, "Project name incorrect"

    @allure.title('Check Project status after creating')
    def test_add_new_project_check_project_status_valid_data(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        add_project_page = MyProjectPage(driver)
        add_project_page.click_on_add_project_button()
        # first modal window
        add_project_page.add_project_first_modal(Project.NAME, Project.CATEGORIES, Project.REGIONS, Project.DESCRIPTION)
        add_project_page.click_next_button()
        # second modal window
        add_project_page.add_project_second_modal(Project.GPU, Project.CPU, Project.RAM)
        add_project_page.click_next_button_second()
        # third modal window
        add_project_page.click_next_button_second()
        # fourth modal window
        add_project_page.upload_file(Project.TEST_FILE)
        add_project_page.click_upload_button()

        alert_text = add_project_page.get_alert()
        add_project_page.refresh_page()
        time.sleep(1)
        project_status = add_project_page.get_created_project_project_status()

        assert project_status == "Preprocessing", "Project status incorrect"

    @allure.title('Check Project status after creating')
    def test_add_new_project_check_project_region_valid_data(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        add_project_page = MyProjectPage(driver)
        add_project_page.click_on_add_project_button()
        # first modal window
        add_project_page.add_project_first_modal(Project.NAME, Project.CATEGORIES, Project.REGIONS, Project.DESCRIPTION)
        add_project_page.click_next_button()
        # second modal window
        add_project_page.add_project_second_modal(Project.GPU, Project.CPU, Project.RAM)
        add_project_page.click_next_button_second()
        # third modal window
        add_project_page.click_next_button_second()
        # fourth modal window
        add_project_page.upload_file(Project.TEST_FILE)
        add_project_page.click_upload_button()

        alert_text = add_project_page.get_alert()
        add_project_page.refresh_page()
        time.sleep(1)
        project_region = add_project_page.get_created_project_project_region()
        assert project_region.lower() == Project.REGIONS, "Project status incorrect"

    @allure.title('Check Project Created date after creating')
    def test_add_new_project_check_project_created_date_valid_data(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        add_project_page = MyProjectPage(driver)
        add_project_page.click_on_add_project_button()
        # first modal window
        add_project_page.add_project_first_modal(Project.NAME, Project.CATEGORIES, Project.REGIONS, Project.DESCRIPTION)
        add_project_page.click_next_button()
        # second modal window
        add_project_page.add_project_second_modal(Project.GPU, Project.CPU, Project.RAM)
        add_project_page.click_next_button_second()
        # third modal window
        add_project_page.click_next_button_second()
        # fourth modal window
        add_project_page.upload_file(Project.TEST_FILE)
        add_project_page.click_upload_button()

        alert_text = add_project_page.get_alert()
        add_project_page.refresh_page()
        time.sleep(1)
        project_date = add_project_page.get_created_project_project_date()

        current_date = add_project_page.get_current_date()

        assert project_date == current_date, "Project date incorrect"

    @allure.title('Check Project Details After Creating')
    def test_add_new_project_check_project_details_valid_data(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        add_project_page = MyProjectPage(driver)
        add_project_page.click_on_add_project_button()
        # first modal window
        add_project_page.add_project_first_modal(Project.NAME, Project.CATEGORIES, Project.REGIONS, Project.DESCRIPTION)
        add_project_page.click_next_button()
        # second modal window
        add_project_page.add_project_second_modal(Project.GPU, Project.CPU, Project.RAM)
        add_project_page.click_next_button_second()
        # third modal window
        add_project_page.click_next_button_second()
        # fourth modal window
        add_project_page.upload_file(Project.TEST_FILE)
        add_project_page.click_upload_button()

        alert_text = add_project_page.get_alert()
        add_project_page.refresh_page()
        time.sleep(1)
        project_details = add_project_page.get_created_project_project_description()

        assert project_details == Project.DESCRIPTION, "Project details incorrect"

    @allure.title('Check upload progress in %')
    def test_add_new_project_check_upload_progress_in_percent_valid_data(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        add_project_page = MyProjectPage(driver)
        add_project_page.click_on_add_project_button()
        # first modal window
        add_project_page.add_project_first_modal(Project.NAME, Project.CATEGORIES, Project.REGIONS, Project.DESCRIPTION)
        add_project_page.click_next_button()
        # second modal window
        add_project_page.add_project_second_modal(Project.GPU, Project.CPU, Project.RAM)
        add_project_page.click_next_button_second()
        # third modal window
        add_project_page.click_next_button_second()
        # fourth modal window
        add_project_page.upload_file(Project.TEST_FILE_70)
        add_project_page.click_upload_button()

        before, after = add_project_page.get_project_uploading_progress_in_percent()

        assert float(before) < float(after), "The Progress has not changed"

    @allure.title('Cher Upload progres bar')
    def test_add_new_project_check_upload_progress_bar_valid_data(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        add_project_page = MyProjectPage(driver)
        add_project_page.click_on_add_project_button()
        # first modal window
        add_project_page.add_project_first_modal(Project.NAME, Project.CATEGORIES, Project.REGIONS, Project.DESCRIPTION)
        add_project_page.click_next_button()
        # second modal window
        add_project_page.add_project_second_modal(Project.GPU, Project.CPU, Project.RAM)
        add_project_page.click_next_button_second()
        # third modal window
        add_project_page.click_next_button_second()
        # fourth modal window
        add_project_page.upload_file(Project.TEST_FILE_70)
        add_project_page.click_upload_button()

        before, after = add_project_page.get_project_uploading_progress_in_percent()

        assert float(before) < float(after), "The Progress has not changed"

    @allure.title('Delete Project')
    def test_delete_project(self, driver):
        self.test_add_new_project_valid_data_check_creating_project(driver)

        add_project_page = MyProjectPage(driver)
        add_project_page.delete_project()
        alert_text = add_project_page.get_alert()
        assert alert_text == "Project deleted", "Alert incorrect"

    @allure.title('Check Search Project')
    def test_check_search(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        add_project_page = MyProjectPage(driver)
        add_project_page.click_on_add_project_button()
        # first modal window
        add_project_page.add_project_first_modal(Project.NAME_FOR_SEARCH, Project.CATEGORIES, Project.REGIONS, Project.DESCRIPTION)
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
        add_project_page.get_alert()
        login.log_out()

        self.test_add_new_project_valid_data_check_creating_project(driver)

        add_project_page.search_input(Project.NAME_FOR_SEARCH)
        time.sleep(2)
        project_name, project_description = add_project_page.get_created_project_data()

        assert project_name == Project.NAME_FOR_SEARCH, "search don't work"

    @allure.title('Check Project status when Admin approve Project')
    def test_check_project_status_after_admin_approve_project(self, driver):
        self.test_add_new_project_valid_data_check_creating_project(driver)

        admin_login = AdminLoginPage(driver, Url.ADMIN_URL)
        admin_login.open()
        admin_login.login_enter_email_and_password('alex+i@zpoken.io', '12345678')
        admin_login.login_click_sign_in_button()

        admin_account = AdminAccountPage(driver)
        admin_account.click_side_menu_tab("project tab")
        admin_account.click_on_approve_button()

        login = LoginPage(driver, Url.USER_URL)
        login.open()

        add_project_page = MyProjectPage(driver)
        project_status = add_project_page.get_created_project_project_status()

        assert project_status == "Approved"

    @allure.title('Check Project status when Admin decline Project')
    def test_check_project_status_after_admin_decline_project(self, driver):
        self.test_add_new_project_valid_data_check_creating_project(driver)

        admin_login = AdminLoginPage(driver, Url.ADMIN_URL)
        admin_login.open()
        admin_login.login_enter_email_and_password('alex+i@zpoken.io', '12345678')
        admin_login.login_click_sign_in_button()

        admin_account = AdminAccountPage(driver)
        admin_account.click_side_menu_tab("project tab")
        admin_account.click_on_decline_button()

        login = LoginPage(driver, Url.USER_URL)
        login.open()

        add_project_page = MyProjectPage(driver)
        project_status = add_project_page.get_created_project_project_status()

        assert project_status == "Declined"

    @allure.title('Update Project File')
    def test_update_project(self, driver):
        login = LoginPage(driver, Url.USER_URL)
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()

        add_project_page = MyProjectPage(driver)
        add_project_page.click_on_add_project_button()
        # first modal window
        add_project_page.add_project_first_modal(Project.NAME, Project.CATEGORIES, Project.REGIONS, Project.DESCRIPTION)
        add_project_page.click_next_button()
        # second modal window
        add_project_page.add_project_second_modal(Project.GPU, Project.CPU, Project.RAM)
        add_project_page.click_next_button_second()
        # third modal window
        add_project_page.click_next_button_second()
        # fourth modal window
        add_project_page.upload_file(Project.UPDATE_FILE_ONE)
        add_project_page.click_upload_button()

        add_project_page.get_alert()

        admin_login = AdminLoginPage(driver, Url.ADMIN_URL)
        admin_login.open()
        admin_login.login_enter_email_and_password('alex+i@zpoken.io', '12345678')
        admin_login.login_click_sign_in_button()

        admin_account = AdminAccountPage(driver)
        admin_account.click_side_menu_tab("project tab")
        time.sleep(2)

        project_file_before, file_path = admin_account.download_file()
        print(project_file_before)
        admin_account.remove_file(file_path)

        login = LoginPage(driver, Url.USER_URL)
        login.open()
        time.sleep(1)
        add_project_page.update_project(Project.UPDATE_FILE_TWO)
        add_project_page.get_alert()
        time.sleep(2)
        admin_login = AdminLoginPage(driver, Url.ADMIN_URL)
        admin_login.open()

        admin_account = AdminAccountPage(driver)
        admin_account.click_side_menu_tab("project tab")
        admin_account.refresh_page()
        time.sleep(2)

        project_file_after, file_path_two = admin_account.download_file()
        print(project_file_after)
        admin_account.remove_file(file_path_two)

        assert project_file_before != project_file_after
        assert project_file_after == ['USBSTOR.reg']

