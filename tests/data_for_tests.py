import random
import os


class Project:

    NAME = f"project{random.randint(1, 999)}"
    CATEGORIES = random.choice(["entertainment", "game", "other"])
    DESCRIPTION = f"description{random.randint(1, 999)}"

    GPU = random.choice(["entry", "lower_mid", "mid", "upper_mid", "high"])
    CPU = random.choice(["1-4", "5-8", "9-16", "16+"])
    RAM = random.choice(["8-16", "17-32", "33-64", "64+"])

    FILE = os.path.abspath("../tests/files/test_file.zip")
    TEST_FILE = os.path.abspath("../tests/files/17.zip")
    TEST_FILE_70 = os.path.abspath("../tests/files/test_app_70.zip")

    UPDATE_FILE_ONE = os.path.abspath("../tests/files/file_for_update_one.zip")
    UPDATE_FILE_TWO = os.path.abspath("../tests/files/file_for_update_two.zip")

    NAME_FOR_SEARCH = f"project{random.randint(1, 999)}"
