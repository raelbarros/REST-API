import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Auth(object):
    def __init__(self, ip):
        self.ip = ip

    def login(self, username, password):
        apiUrlLogin = 'https://' + self.ip + '/nitro/v1/config/login'

        headersLogin = {
            'Content-Type': 'application/vnd.com.citrix.netscaler.login+json'
        }

        try:
            r = requests.post(apiUrlLogin, headers=headersLogin, json={
                "login":
                    {
                        "password": username,
                        "username": password,
                        "timeout": 3000
                    }
            }, verify=False)

            # Get just cookie ID
            for item in r.cookies.items():
                for i in item:
                    id = i

            # return cookieID
            return id
        except:
            print('Error ao Logar')

    def logoff(self, cookieId):
        apiUrlLogout = 'https://' + self.ip + '/nitro/v1/config/logout'

        headersLogoff = {
            'Cookie': 'NITRO_AUTH_TOKEN=' + cookieId,
            'Content-Type': 'application/vnd.com.citrix.netscaler.logout+json'
        }

        try:
            requests.post(apiUrlLogout, headers=headersLogoff, json={
                "logout": {}
            }, verify=False)
            print('logoff Success')
        except:
            print('Logoff Error')
