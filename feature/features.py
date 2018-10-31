import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Features(object):
    def __init__(self, ip, cookieId):
        self.ip = ip
        self.apiUrlEnable = 'http://' + ip + '/nitro/v1/config/nsfeature?action=enable'
        self.headers = {
            'Cookie': 'NITRO_AUTH_TOKEN=' + cookieId,
            'Content-Type': 'application/vnd.com.citrix.netscaler.nsfeature+json'
        }

    def enableLoadBalance(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsfeature": {
                    "feature": [
                        "LB"
                    ]
                }
            }, verify=False)
            print('LB Success')
        except:
            print('LB Fail')

    def enableContentSwitching(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsfeature": {
                    "feature": [
                        "CS"
                    ]
                }
            }, verify=False)
            print('CS Success')
        except:
            print('CS Fail')

    def enableSSLOffloading(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsfeature": {
                    "feature": [
                        "SSL"
                    ]
                }
            }, verify=False)
            print('SSL Success')
        except:
            print('SSL Fail')

    def enableContentFilter(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsfeature": {
                    "feature": [
                        "CF"
                    ]
                }
            }, verify=False)
            print('CF Success')
        except:
            print('CF Fail')

    def enableRewrite(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsfeature": {
                    "feature": [
                        "Rewrite"
                    ]
                }
            }, verify=False)
            print('Rewrite Success')
        except:
            print('Rewrite Fail')

    #  --------- Disable ----------
    # def enableAAA(self):
    #     try:
    #         requests.post(self.apiUrlEnable, headers=self.headers, json={
    #             "nsfeature": {
    #                 "feature": [
    #                     "AAA"
    #                 ]
    #             }
    #         }, verify=False)
    #         print('AAA Success')
    #     except:
    #         print('AAA Fail')
    #
    # def enableHTTP(self):
    #     try:
    #         requests.post(self.apiUrlEnable, headers=self.headers, json={
    #             "nsfeature": {
    #                 "feature": [
    #                     "HC"
    #                 ]
    #             }
    #         }, verify=False)
    #         print('HTTP Success')
    #     except:
    #         print('HTTP Fail')
    #
    # def enableIntegratedCaching(self):
    #     try:
    #         requests.post(self.apiUrlEnable, headers=self.headers, json={
    #             "nsfeature": {
    #                 "feature": [
    #                     "IC"
    #                 ]
    #             }
    #         }, verify=False)
    #         print('IC Success')
    #     except:
    #         print('IC Fail')
    #
    # def enableGateway(self):
    #     try:
    #         requests.post(self.apiUrlEnable, headers=self.headers, json={
    #             "nsfeature": {
    #                 "feature": [
    #                     "NG"
    #                 ]
    #             }
    #         }, verify=False)
    #         print('Gateway Success')
    #     except:
    #         print('Gateway Fail')
    #
    # def enableAppFirewall(self):
    #     try:
    #         requests.post(self.apiUrlEnable, headers=self.headers, json={
    #             "nsfeature": {
    #                 "feature": [
    #                     "AppFw"
    #                 ]
    #             }
    #         }, verify=False)
    #         print('Firewall Success')
    #     except:
    #         print('Firewall Fail')
