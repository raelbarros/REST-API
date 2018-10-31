import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Config(object):

    def __init__(self, nsIp, cookieId, nsHostname, subIP, subMask, timezone):
        self.nsIp = nsIp
        self.cookieId = cookieId

        self.nsHostname = nsHostname

        self.subIp = subIP
        self.subMask = subMask

        self.time = timezone

    def initialConf(self):
        self.nsip()
        self.hostname()
        self.timezone()

    def hostname(self):
        apiUrl = 'http://' + self.nsIp + '/nitro/v1/config/nshostname'
        headers = {
            'Cookie': 'NITRO_AUTH_TOKEN=' + self.cookieId,
            'Content-Type': 'application/json'
        }

        try:
            r = requests.put(apiUrl, headers=headers, json={
                "nshostname": {
                    "hostname": self.nsHostname,
                }
            }, verify=False)
            print('hostname success')
        except:
            print('ds fail')


    def timezone(self):
        apiUrl = 'http://' + self.nsIp + '/nitro/v1/config/nsconfig'
        headers = {
            'Cookie': 'NITRO_AUTH_TOKEN=' + self.cookieId,
            'Content-Type': 'application/vnd.com.citrix.netscaler.nsconfig+json'
        }

        try:
            r = requests.put(apiUrl, headers=headers, json={
                "nsconfig": {
                    "timezone": self.time,
                }
            }, verify=False)
            print('timezone success')
        except:
            print('timezone fail')

    def nsip(self):
        apiUrl = 'http://' + self.nsIp + '/nitro/v1/config/nsip'

        headers = {
            'Cookie': 'NITRO_AUTH_TOKEN=' + self.cookieId,
            'Content-Type': 'application/vnd.com.citrix.netscaler.nsip+json'
        }

        try:
            requests.post(apiUrl, headers=headers, json={
                "nsip": {
                    "ipaddress": self.subIp,
                    "netmask": self.subMask,
                }
            }, verify=False)
            print('nsip success')
        except:
            print('nsip fail')