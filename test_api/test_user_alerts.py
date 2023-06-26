from api.activities import GetAccessToken, Alert


class TestAlerts:

    def test_get_token(self):
        access = GetAccessToken()
        token = access.get_access_token()

        alert = Alert()
        alert.create_alert(token)
