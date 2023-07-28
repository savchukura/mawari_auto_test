from locators.developer.my_projects_locators import MyProjectsLocators
from pages.base_page import NextPage
from datetime import datetime


class MyProjectPage(NextPage):

    def click_on_add_project_button(self):
        self.element_is_visible(MyProjectsLocators.ADD_PROJECT_BUTTON).click()

    def add_project_first_modal(self, name, category, description):
        self.element_is_visible(MyProjectsLocators.NAME_INPUT).send_keys(name)

        self.element_is_visible(MyProjectsLocators.CATEGORY_DROP).click()
        categories = {"entertainment": MyProjectsLocators.ENTERTAINMENT_CATEGORY,
                      "game": MyProjectsLocators.GAME_CATEGORY,
                      "other": MyProjectsLocators.OTHER_CATEGORY}
        self.element_is_visible(categories[category]).click()

        self.element_is_visible(MyProjectsLocators.DESCRIPTION_TEXT_AREA).send_keys(description)

    def click_next_button(self):
        self.element_is_visible(MyProjectsLocators.NEXT_BUTTON).click()

    def click_cancel_button(self):
        self.element_is_visible(MyProjectsLocators.CANCEL_BUTTON).click()

    def add_project_second_modal(self, gpu, cpu, ram):
        gpu_cpu_ram_drop = self.elements_are_visible(MyProjectsLocators.GPU_CPU_RAM_DROP)
        gpu_cpu_ram_drop[0].click()
        gpu_drop = {"entry": MyProjectsLocators.GPU_ENTRY,
                    "lower_mid": MyProjectsLocators.GPU_LOWER_MID,
                    "mid": MyProjectsLocators.GPU_MID,
                    "upper_mid": MyProjectsLocators.GPU_UPPER_MID,
                    "high": MyProjectsLocators.GPU_HIGH}
        self.element_is_visible(gpu_drop[gpu]).click()

        gpu_cpu_ram_drop[1].click()
        cpu_drop = {"1-4": MyProjectsLocators.CPU_1_4,
                    "5-8": MyProjectsLocators.CPU_5_8,
                    "9-16": MyProjectsLocators.CPU_9_16,
                    "16+": MyProjectsLocators.CPU_16}
        self.element_is_visible(cpu_drop[cpu]).click()

        gpu_cpu_ram_drop[2].click()
        ram_drop = {"8-16": MyProjectsLocators.RAM_8_16,
                    "17-32": MyProjectsLocators.RAM_17_32,
                    "33-64": MyProjectsLocators.RAM_33_64,
                    "64+": MyProjectsLocators.RAM_64}
        self.element_is_visible(ram_drop[ram]).click()

    def click_next_button_second(self):
        self.element_is_visible(MyProjectsLocators.NEXT_BUTTON_SECOND).click()

    def click_back_button(self):
        self.element_is_visible(MyProjectsLocators.BACK_BUTTON).click()

    def add_project_third_modal(self, fixed_amount):
        self.element_is_visible(MyProjectsLocators.TOGGLE_ON_BUTTON).click()
        self.element_is_visible(MyProjectsLocators.FIXED_INPUT).send_keys(fixed_amount)

    def upload_file(self, file_path):
        self.element_is_present(MyProjectsLocators.FILE_INPUT).send_keys(file_path)

    def check_file_name(self):
        file_name = self.element_is_visible(MyProjectsLocators.FILE_NAME).text
        return file_name

    def click_upload_button(self):
        self.element_is_visible(MyProjectsLocators.UPLOAD_BUTTON).click()

    def get_created_project_data(self):
        project_names = self.elements_are_visible(MyProjectsLocators.PROJECT_NAME)
        project_name = project_names[0].text
        project_descriptions = self.elements_are_visible(MyProjectsLocators.PROJECT_DESCRIPTION)
        project_description = project_descriptions[0].text
        return project_name, project_description

    def get_created_project_id(self):
        project_ids = self.elements_are_visible(MyProjectsLocators.PROJECT_ID)
        project_id = project_ids[0].text
        return project_id

    def get_created_project_name(self):
        project_names = self.elements_are_visible(MyProjectsLocators.PROJECT_NAME)
        project_name = project_names[0].text
        return project_name

    def get_created_project_project_status(self):
        project_statuses = self.elements_are_visible(MyProjectsLocators.PROJECT_STATUS_FIELDS)
        project_status = project_statuses[0].text
        return project_status

    def get_created_project_project_date(self):
        project_dates = self.elements_are_visible(MyProjectsLocators.PROJECT_DATE)
        project_date = project_dates[2].text
        return project_date

    def get_created_project_project_description(self):
        project_descriptions = self.elements_are_visible(MyProjectsLocators.PROJECT_DESCRIPTION)
        project_description = project_descriptions[0].text
        return project_description

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

    def delete_project(self):
        delete = self.elements_are_visible(MyProjectsLocators.DELETE_PROJECT_BUTTON)
        delete[1].click()

    def get_alert(self):
        alert_text = self.element_is_visible(MyProjectsLocators.ALERT, 50).text
        return alert_text

    def search_input(self, search):
        self.element_is_visible(MyProjectsLocators.SEARCH_INPUT).send_keys(search)

    def get_current_date(self):
        # Get the current date and time
        current_date_time = datetime.now()

        # Extract the current date (year, month, day)
        current_date = current_date_time.date()

        # Format the date if needed (optional)
        formatted_date = current_date.strftime("%Y-%m-%d")

        return formatted_date

