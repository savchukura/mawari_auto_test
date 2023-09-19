import allure

from locators.developer.my_projects_locators import MyProjectsLocators
from pages.base_page import NextPage
from datetime import datetime
import time
import random
import allure


class MyProjectPage(NextPage):

    @allure.step('Click on add project button')
    def click_on_add_project_button(self):
        self.element_is_visible(MyProjectsLocators.ADD_PROJECT_BUTTON).click()

    @allure.step('First Modal Window')
    def add_project_first_modal(self, name, category, region, description):
        with allure.step('Fill Project name'):
            self.element_is_visible(MyProjectsLocators.NAME_INPUT).send_keys(name)

        with allure.step('Select Category'):
            self.element_is_visible(MyProjectsLocators.CATEGORY_DROP).click()
            categories = {"entertainment": MyProjectsLocators.ENTERTAINMENT_CATEGORY,
                          "game": MyProjectsLocators.GAME_CATEGORY,
                          "other": MyProjectsLocators.OTHER_CATEGORY}
            self.element_is_visible(categories[category]).click()

        with allure.step('Select Region'):
            region_drop = self.elements_are_visible(MyProjectsLocators.CATEGORY_DROP)
            region_drop[1].click()
            regions = {"europe": MyProjectsLocators.EUROPE_REGION,
                       "us": MyProjectsLocators.US_REGION,
                       "asia": MyProjectsLocators.ASIA_REGION}
            self.element_is_visible(regions[region]).click()

        with allure.step('Select Country'):
            country_drop = self.elements_are_visible(MyProjectsLocators.CATEGORY_DROP)
            country_drop[2].click()
            countries = self.elements_are_present(MyProjectsLocators.COUNTRY)
            #countries_count = len(countries)
            #country = countries[random.randint(0, countries_count)].click()
            countries[2].click()

        with allure.step('Select State'):
            state_drop = self.elements_are_visible(MyProjectsLocators.CATEGORY_DROP)
            state_drop[3].click()
            states = self.elements_are_present(MyProjectsLocators.COUNTRY)
            #states_count = len(states)
            #self.go_to_element(states[10])
            #state = states[random.randint(0, states_count - 1)].click()
            states[1].click()

        with allure.step('Fill Description'):
            self.element_is_visible(MyProjectsLocators.DESCRIPTION_TEXT_AREA).send_keys(description)

    @allure.step('Click Next Button')
    def click_next_button(self):
        self.element_is_visible(MyProjectsLocators.NEXT_BUTTON).click()

    @allure.step('Click Cancel button')
    def click_cancel_button(self):
        self.element_is_visible(MyProjectsLocators.CANCEL_BUTTON).click()

    @allure.step('Second Modal window')
    def add_project_second_modal(self, gpu, cpu, ram):
        gpu_cpu_ram_drop = self.elements_are_visible(MyProjectsLocators.GPU_CPU_RAM_DROP)
        with allure.step('Select GPU'):
            gpu_cpu_ram_drop[0].click()
            gpu_drop = {"entry": MyProjectsLocators.GPU_ENTRY,
                        "lower_mid": MyProjectsLocators.GPU_LOWER_MID,
                        "mid": MyProjectsLocators.GPU_MID,
                        "upper_mid": MyProjectsLocators.GPU_UPPER_MID,
                        "high": MyProjectsLocators.GPU_HIGH}
            self.element_is_visible(gpu_drop[gpu]).click()
        with allure.step('Select CPU'):
            gpu_cpu_ram_drop[1].click()
            cpu_drop = {"1-4": MyProjectsLocators.CPU_1_4,
                        "5-8": MyProjectsLocators.CPU_5_8,
                        "9-16": MyProjectsLocators.CPU_9_16,
                        "16+": MyProjectsLocators.CPU_16}
            self.element_is_visible(cpu_drop[cpu]).click()

        with allure.step('Select RAM'):
            gpu_cpu_ram_drop[2].click()
            ram_drop = {"8-16": MyProjectsLocators.RAM_8_16,
                        "17-32": MyProjectsLocators.RAM_17_32,
                        "33-64": MyProjectsLocators.RAM_33_64,
                        "64+": MyProjectsLocators.RAM_64}
            self.element_is_visible(ram_drop[ram]).click()

        with allure.step('Select Simultaneous Users'):
            simulation_users_input = self.element_is_visible(MyProjectsLocators.SIMULATIONS_USERS)
            self.action_double_click(simulation_users_input)
            simulation_users_input.send_keys(random.randint(1, 100))

    @allure.step('click Next Button on Second Modal')
    def click_next_button_second(self):
        self.element_is_visible(MyProjectsLocators.NEXT_BUTTON_SECOND).click()

    @allure.step('Click back Button')
    def click_back_button(self):
        self.element_is_visible(MyProjectsLocators.BACK_BUTTON).click()

    @allure.step('Third modal Window')
    def add_project_third_modal(self, fixed_amount):
        self.element_is_visible(MyProjectsLocators.TOGGLE_ON_BUTTON).click()
        self.element_is_visible(MyProjectsLocators.FIXED_INPUT).send_keys(fixed_amount)

    @allure.step('Upload File')
    def upload_file(self, file_path):
        self.element_is_present(MyProjectsLocators.FILE_INPUT).send_keys(file_path)

    @allure.step('Check file name')
    def check_file_name(self):
        file_name = self.element_is_visible(MyProjectsLocators.FILE_NAME).text
        return file_name

    @allure.step('click upload button')
    def click_upload_button(self):
        self.element_is_visible(MyProjectsLocators.UPLOAD_BUTTON).click()

    @allure.step('Check Created data')
    def get_created_project_data(self):
        project_names = self.elements_are_visible(MyProjectsLocators.PROJECT_NAME)
        project_name = project_names[0].text
        project_descriptions = self.elements_are_visible(MyProjectsLocators.PROJECT_DESCRIPTION)
        project_description = project_descriptions[0].text
        return project_name, project_description

    @allure.step('Get Project ID')
    def get_created_project_id(self):
        project_ids = self.elements_are_visible(MyProjectsLocators.PROJECT_ID)
        project_id = project_ids[0].text
        return project_id

    @allure.step('Get Project Name')
    def get_created_project_name(self):
        project_names = self.elements_are_visible(MyProjectsLocators.PROJECT_NAME)
        project_name = project_names[0].text
        return project_name

    @allure.step('Get Project Region')
    def get_created_project_project_region(self):
        project_regions = self.elements_are_visible(MyProjectsLocators.PROJECT_REGION)
        project_region = project_regions[2].text
        return project_region

    @allure.step('Get Project Status')
    def get_created_project_project_status(self):
        project_statuses = self.elements_are_visible(MyProjectsLocators.PROJECT_STATUS_FIELDS)
        project_status = project_statuses[0].text
        return project_status

    @allure.step('Get project created date')
    def get_created_project_project_date(self):
        project_dates = self.elements_are_visible(MyProjectsLocators.PROJECT_DATE)
        project_date = project_dates[3].text
        return project_date.split(' ')[1]

    @allure.step('Get created project description')
    def get_created_project_project_description(self):
        project_descriptions = self.elements_are_visible(MyProjectsLocators.PROJECT_DESCRIPTION)
        project_description = project_descriptions[0].text
        return project_description

    @allure.step('Get all project data')
    def get_all_project_data(self):
        project_ids = self.elements_are_visible(MyProjectsLocators.PROJECT_ID)
        project_id = project_ids[0].text
        project_names = self.elements_are_visible(MyProjectsLocators.PROJECT_NAME)
        project_name = project_names[0].text
        project_statuses = self.elements_are_visible(MyProjectsLocators.PROJECT_STATUS_FIELDS)
        project_status = project_statuses[0].text
        project_dates = self.elements_are_visible(MyProjectsLocators.PROJECT_DATE)
        project_date = project_dates[2].text
        project_descriptions = self.elements_are_visible(MyProjectsLocators.PROJECT_DESCRIPTION)
        project_description = project_descriptions[0].text
        data = [project_id, project_name, project_status, project_date, project_description]
        return data

    @allure.step('Click on Delete button')
    def delete_project(self):
        delete = self.elements_are_visible(MyProjectsLocators.DELETE_PROJECT_BUTTON)
        delete[1].click()

    @allure.step('Update project Data')
    def update_project_data(self):
        update_data_button = self.elements_are_visible(MyProjectsLocators.UPDATE_PROJECT_DATA_BUTTON)
        update_data_button[2].click()

    @allure.step('Get Alert')
    def get_alert(self):
        alert_text = self.element_is_visible(MyProjectsLocators.ALERT, 50).text
        return alert_text

    @allure.step('Fill in Search Input')
    def search_input(self, search):
        self.element_is_visible(MyProjectsLocators.SEARCH_INPUT).send_keys(search)

    @allure.step('Get current date')
    def get_current_date(self):
        # Get the current date and time
        current_date_time = datetime.now()

        # Extract the current date (year, month, day)
        current_date = current_date_time.date()

        # Format the date if needed (optional)
        formatted_date = current_date.strftime("%d.%m.%Y")

        return formatted_date

    @allure.step('Check project uploading in %')
    def get_project_uploading_progress_in_percent(self):
        time.sleep(1)
        upload_progress_in_percent_before = self.element_is_visible(MyProjectsLocators.PROGRESS_STATUS_BY_PERCENT).text
        time.sleep(random.randint(2, 5))
        upload_progress_in_percent_after = self.element_is_visible(
            MyProjectsLocators.PROGRESS_STATUS_BY_PERCENT).text
        return upload_progress_in_percent_before.replace('%', ''), upload_progress_in_percent_after.replace('%', '')

    @allure.step('Check Project Uploading progress bar')
    def get_project_uploading_progress_bar(self):
        time.sleep(1)
        upload_progress_in_percent_before = self.element_is_visible(MyProjectsLocators.PROGRESS_STATUS_BAR).get_attribute('style')
        time.sleep(random.randint(2, 5))
        upload_progress_in_percent_after = self.element_is_visible(
            MyProjectsLocators.PROGRESS_STATUS_BAR).get_attribute('style')
        return upload_progress_in_percent_before, upload_progress_in_percent_after

    @allure.step('Update Project File')
    def update_project(self, file_path):
        update = self.elements_are_visible(MyProjectsLocators.DELETE_PROJECT_BUTTON)
        update[1].click()
        self.element_is_present(MyProjectsLocators.FILE_INPUT).send_keys(file_path)
        self.element_is_visible(MyProjectsLocators.UPLOAD_BUTTON).click()

