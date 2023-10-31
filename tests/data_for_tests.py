import random
import os


class Project:

    NAME = f"project{random.randint(1, 999)}"
    CATEGORIES = random.choice(["entertainment", "game", "other"])
    REGIONS = random.choice(["europe", "us", "asia", "global"])
    DESCRIPTION = f"description{random.randint(1, 999)}"

    GPU = random.choice(["lower_mid", "mid", "upper_mid", "high"])
    CPU = random.choice(["5-8", "9-16", "16+"])
    RAM = random.choice(["17-32", "33-64", "64+"])

    FILE = os.path.abspath("../tests/files/test_file.zip")
    TEST_FILE = os.path.abspath("../tests/files/17.zip")
    REL_PATH = os.path.abspath(os.path.join(os.path.abspath(os.curdir), "tests/files/17.zip"))
    TEST_FILE_70 = os.path.abspath('../tests/files/test_app_70.zip')
    TEST_FILE_PATH = os.path.abspath('../mawari_auto_test/tests/files/17.zip')
    UPDATE_FILE_ONE = os.path.abspath("../tests/files/file_for_update_one.zip")
    UPDATE_FILE_TWO = os.path.abspath("../tests/files/file_for_update_two.zip")

    NAME_FOR_SEARCH = f"project{random.randint(1, 999)}"


class Url:
    USER_URL = "https://mawari.network/login"

    ADMIN_URL = "https://admin.mawari.network/login"

    USER_DEV = "https://dev-mawari.zpoken.dev/login"
    USER_PROD = "https://mawari.network/login"
    ADMIN_DEV = "https://dev-mn-admin.zpoken.dev/login"
    ADMIN_PROD = "https://admin.mawari.network/login"

    def user_url(self, env):
        url = {"dev": "https://dev-mawari.zpoken.dev/login",
               "prod": "https://mawari.network/login"}

        print(url[env])


