import requests
import json
import time

AUTH_URL = "https://dev-mn-admin.zpoken.dev/api/v1/auth"


class GetAccessToken:

    def get_access_token(self):
        data = {
            'email': 'glib@zpoken.io',
            'password': '12345678',
            'returnSecureToken': True
        }
        response_one = requests.post(
            url='https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyA_hu8mFWnFC3huZ_hctQiA3Q918PAbnBo',
            data=json.dumps(data))
        time.sleep(3)
        data = {
            'idToken': response_one.json()['idToken'],
            'fingerprint': '7f16ce8a1738428678922bb80cf1b5b1478da0b3',
            'role': 'node_runner'
        }
        headers = {"Content-Type": "application/json"}

        res = json.loads(
            requests.post(url="https://dev-mawari.zpoken.dev/api/v1/auth", json=data, headers=headers).text)

        token = res['tokens']['access_token']
        return token

    def get_admin_access_token(self):
        data = {
            'email': 'yura@zpoken.io',
            'password': '12345678',
            'returnSecureToken': True
        }
        response_one = requests.post(
            url='https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyA_hu8mFWnFC3huZ_hctQiA3Q918PAbnBo',
            data=json.dumps(data))
        time.sleep(3)
        data = {
            'idToken': response_one.json()['idToken'],
            'fingerprint': '7f16ce8a1738428678922bb80cf1b5b1478da0b3',
            'role': 'admin'
        }
        headers = {"Content-Type": "application/json"}

        res = json.loads(
            requests.post(url="https://dev-mawari.zpoken.dev/api/v1/auth", json=data, headers=headers).text)

        token = res['tokens']['access_token']
        return token


class Alert:

    def create_alert(self, token):
        data = {
            "guid": "418bbeb3-db24-4d65-b077-eda138de1c16",
            "status": "resolved",
            "alert_type": "node_start",
            "severity": "information"
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = json.loads(requests.post(
            url="https://dev-mawari.zpoken.dev/api/v1/alerts",
            json=data,
            headers=headers).text)
        #print(response)
        print(response['id'])

    def get_all_alerts(self, token):
        headers = {

            "Authorization": f"Bearer {token}"
        }

        r = requests.get(url="https://dev-mawari.zpoken.dev/api/v1/alerts", headers=headers)
        print(r.text)