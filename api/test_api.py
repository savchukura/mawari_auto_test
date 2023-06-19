import requests
import json
from api.activities import GetAccessToken


class TestApi:

    def test_get_all_users(self):
        auth_url = "https://dev-mn-admin.zpoken.dev/api/v1/auth"
        body = {"email": "alex+i@zpoken.io", "password": "12345678", "fingerprint": "aaaa"}
        headers = {"Content-Type": "application/json"}
        res = json.loads(requests.post(auth_url, json=body, headers=headers).text)
        #r = requests.post(auth_url, json=body, headers=headers)
        #token = res['tokens']['access_token']
        print(res)
