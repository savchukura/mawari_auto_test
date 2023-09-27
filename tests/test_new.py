import time
import requests
import json
import shutil
from pages.developer_pages.my_project_page import MyProjectPage
from pages.login_page import LoginPage
from pages.user_page import NodeRunnerPage
from api.activities import GetAccessToken, GetUser, Wallets
from tests.data_for_tests import Project
from conftest import *
import zipfile
import os
import base64
import random


class TestCaseNew:

    def test_one(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("yura@zpoken.io", "213456qaZ", "node_runner")
        time.sleep(2)
        url = driver.current_url.split("/")[-2]
        login.log_out()
        assert url == "runners", "User log in under wrong role"

    def test_cycle(self, driver):
        for i in range(10):
            self.test_one(driver)

    def test_two(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("yura@zpoken.io", "213456qaZ", "node_runner")

        user_page = NodeRunnerPage(driver)
        user_page.click_on_tab_button("nodes list")
        user_page.click_filtering_drop()
        time.sleep(2)

    def test_auth(self):
        get_token = GetAccessToken()
        user_id, token = get_token.get_access_token_and_user_id()

        user = GetUser()
        user_data = user.get_user_data(token, user_id)
        print(user_id)

    def test_admin_auth(self):
        get_admin_token = GetAccessToken()
        admin_token = get_admin_token.get_admin_access_token()
        print(admin_token)

    def test_get_user_data(self):
        get_admin_token = GetAccessToken()
        admin_token = get_admin_token.get_admin_access_token()

        user = GetUser()
        user_data = user.get_user_data(admin_token, 429)

    def test_top_up_wallet(self):
        get_token = GetAccessToken()
        user_id, token = get_token.get_access_token_and_user_id()

        wallets = Wallets()
        top_up = wallets.top_up(token, 22, 100)

    def test_add_new_project_check_project_name_valid_data(self, driver):
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
        add_project_page.click_next_button_second()
        # fourth modal window
        add_project_page.upload_file(Project.TEST_FILE)
        add_project_page.click_upload_button()
        alert_text = add_project_page.get_alert()
        add_project_page.refresh_page()
        time.sleep(1)

        data = add_project_page.get_all_project_data()

        print(data[0])
        print(data[1])
        print(data[2])
        print(data[3])
        print(data[4])

    def test_get_current_time(self, driver):
        login = LoginPage(driver, "https://dev-mawari.zpoken.dev/login")
        login.open()
        login.log_in("savcukura866@gmail.com", "213456qaZ", "developer")
        login.click_sign_in_button()
        add_project_page = MyProjectPage(driver)
        current_date = add_project_page.get_current_date()
        print(current_date)

    def test_open_zip(self):
        # zip file handler
        zip = zipfile.ZipFile(os.path.abspath("../tests/files/test_file.zip"))

        # list available files in the container
        print(zip.namelist())

    def test_download_files(self):
        link = "https://dev-mawari.zpoken.dev/p-download/871574335_files.zip"
        link_b = base64.b64decode(link)
        path_name_file = os.path.abspath(f"../tests/files/test{random.randint(0, 999)}.zip")

        zip = zipfile.ZipFile(path_name_file)

        # list available files in the container
        print(zip.namelist())

        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        zip = zipfile.ZipFile(path_name_file)

        # list available files in the container
        print(zip.namelist())
        os.remove(path_name_file)
        #return check_file

    def test_download(self):
        try:
            # Send a GET request to the URL to download the zip file
            response = requests.get("https://dev-mawari.zpoken.dev/p-download/871574335_files.zip", stream=True)
            response.raise_for_status()

            # Extract the filename from the URL
            file_name = "https://dev-mawari.zpoken.dev/p-download/871574335_files.zip".split('/')[-1]

            # Create the save folder if it doesn't exist
            #os.makedirs(f"../tests/files", exist_ok=True)

            # Save the zip file to the specified folder
            save_path = os.path.join(f"../tests/files", file_name)
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            print(f"Zip file downloaded and saved to: {save_path}")
            zip = zipfile.ZipFile(os.path.abspath("../tests/files/test_file.zip"))

            # list available files in the container
            print(zip.namelist())
            os.remove(save_path)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading the zip file: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_url(self):
        env_name = 'prod'
        login_url = Project()
        url = login_url.user_url(env_name)
        print(url)
