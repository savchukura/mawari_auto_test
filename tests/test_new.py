import time
import requests
import json
from pages.login_page import LoginPage
from pages.user_page import NodeRunnerPage


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
        data = {
            'email': 'glib@zpoken.io',
            'password': '12345678',
            'returnSecureToken': True
        }
        response_one = requests.post(
            url='https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyA_hu8mFWnFC3huZ_hctQiA3Q918PAbnBo',
            data=json.dumps(data))
        #ssprint(response_one.text)
        time.sleep(3)
        data = {
            'idToken': response_one.json()['idToken'],
            'fingerprint': '7f16ce8a1738428678922bb80cf1b5b1478da0b3',
            'role': 'node_runner'
        }
        headers = {"Content-Type": "application/json"}
        #response = requests.post(url="https://dev-mawari.zpoken.dev/api/v1/auth", data=json.dumps(data), headers=headers)
        res = json.loads(requests.post(url="https://dev-mawari.zpoken.dev/api/v1/auth", json=data, headers=headers).text)

        token = res['tokens']['access_token']
        #print(response.text)
        print(token)
