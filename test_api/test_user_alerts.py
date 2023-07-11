from api.activities import GetAccessToken, Alert
import requests


class TestAlerts:

    def test_get_token(self):
        access = GetAccessToken()
        token = access.get_access_token_and_user_id()

        alert = Alert()
        alert.create_alert(token)

    def test_create_alert(self):
        access = GetAccessToken()
        token = access.get_access_token_and_user_id()

        alert = Alert()
        alert.create_alert(token)

        alert.get_all_alerts(token)

    def test_delete_user(self):
        access = GetAccessToken()
        token = access.get_access_token_and_user_id()


