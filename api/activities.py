import requests
import json

AUTH_URL = "https://dev-mn-admin.zpoken.dev/api/v1/auth"


class GetAccessToken:

    def get_access_token(self, auth_url):
        body = {"email": "alex+i@zpoken.io", "password": "12345678", "fingerprint": "aaaa"}
        headers = {"Content-Type": "application/json"}
        res = json.loads(requests.post(auth_url, json=body, headers=headers).text)

        token = res['tokens']['access_token']
        return token



