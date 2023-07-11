import requests
import json
import time

AUTH_URL = "https://dev-mn-admin.zpoken.dev/api/v1/auth"


class GetAccessToken:

    def get_access_token_and_user_id(self):
        data = {
            'email': 'savcukura866@gmail.com',
            'password': '213456qaZ',
            'returnSecureToken': True
        }
        response_one = requests.post(
            url='https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyA_hu8mFWnFC3huZ_hctQiA3Q918PAbnBo',
            data=json.dumps(data))
        time.sleep(3)
        data = {
            'idToken': response_one.json()['idToken'],
            'fingerprint': 'd1c8f9185507f41eef029f10f2fd939acc2d4a61',
            'role': 'node_runner'
        }
        headers = {"Content-Type": "application/json"}

        res = json.loads(
            requests.post(url="https://dev-mawari.zpoken.dev/api/v1/auth", json=data, headers=headers).text)

        user_id = res['user']['id']
        token = res['tokens']['access_token']
        return user_id, token

    def get_admin_access_token(self):
        data = {
            'email': 'alex+i@zpoken.io',
            'password': '12345678',
            'returnSecureToken': True
        }
        response_one = requests.post(
            url='https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyBY8jiWYgMx0o-NJwvMAGR6g8_uWIjVRHs',
            data=json.dumps(data))
        time.sleep(3)
        data = {
            'idToken': response_one.json()['idToken'],
            'fingerprint': '94832c9f5df8f4cc668f3b5450fac2fa9b6aaa3b',
            'role': 'admin'
        }
        headers = {"Content-Type": "application/json"}

        res = json.loads(
            requests.post(url="https://dev-mn-admin.zpoken.dev/api/v1/auth", json=data, headers=headers).text)
        admin_token = res['tokens']['access_token']
        return admin_token


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


class GetUser:

    def get_user_data(self, token, user_id):
        headers = {

            "Authorization": f"Bearer {token}"
        }

        r = requests.get(url=f"https://dev-mawari.zpoken.dev/api/v1/users/{user_id}", headers=headers)
        print(r.status_code)


class Wallets:

    def top_up(self, token, wallet_id, amount):

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        data = {
            "wallet_id": wallet_id,
            "amount": amount,
            "source": 0
        }
        r = requests.post(url=f"https://dev-mawari.zpoken.dev/api/v1/wallets/top_up", json=data, headers=headers)
