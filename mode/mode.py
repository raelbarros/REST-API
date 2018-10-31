import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Mode(object):
    def __init__(self, ip, cookieId):
        self.ip = ip
        self.apiUrlEnable = 'http://' + ip + '/nitro/v1/config/nsmode?action=enable'
        self.headers = {
            'Cookie': 'NITRO_AUTH_TOKEN=' + cookieId,
            'Content-Type': 'application/vnd.com.citrix.netscaler.nsmode+json'
        }

    def enableLayer2(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "L2"
                    ]
                }
            }, verify=False)
            print('L2 Success')
        except:
            print('L2 Fail')

    def enableUseSourceIP(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "USIP"
                    ]
                }
            }, verify=False)
            print('USIP Success')
        except:
            print('USIP Fail')

    def enableFastRamp(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "FR"
                    ]
                }
            }, verify=False)
            print('FR Success')
        except:
            print('FR Fail')

    def enableClientKeepAlive(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "CKA"
                    ]
                }
            }, verify=False)
            print('CKA Success')
        except:
            print('CKA Fail')

    def enableTCPBuffering(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "TCPB"
                    ]
                }
            }, verify=False)
            print('TCPB Success')
        except:
            print('TCPB Fail')

    def enableMACBasedFowarding(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "MBF"
                    ]
                }
            }, verify=False)
            print('MBF Success')
        except:
            print('MBF Fail')

    def enableEdgeConfiguration(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "Edge"
                    ]
                }
            }, verify=False)
            print('Edge Success')
        except:
            print('Edge Fail')

    def enableUseSubnetIP(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "USNIP"
                    ]
                }
            }, verify=False)
            print('USNIP Success')
        except:
            print('USNIP Fail')

    def enableLayer3(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "L3"
                    ]
                }
            }, verify=False)
            print('L3 Success')
        except:
            print('L3 Fail')

    def enablePathMTUDiscovery(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "PMTUD"
                    ]
                }
            }, verify=False)
            print('PMTUD Success')
        except:
            print('PMTUD Fail')

    def enableStaticRouterAdvertisement(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "SRADV"
                    ]
                }
            }, verify=False)
            print('SRADV Success')
        except:
            print('SRADV Fail')

    def enableDirectRouterAdvertisement(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "DRADV"
                    ]
                }
            }, verify=False)
            print('DRADV Success')
        except:
            print('DRADV Fail')

    def enableIntranetRouterAdvertisement(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "IRADV"
                    ]
                }
            }, verify=False)
            print('IRADV Success')
        except:
            print('IRADV Fail')

    def enableIPV6StaticRouterAdvertisement(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "SRADV6"
                    ]
                }
            }, verify=False)
            print('SRADV6 Success')
        except:
            print('SRADV6 Fail')

    def enableIPV6DirectRouterAdvertisement(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "DRADV6"
                    ]
                }
            }, verify=False)
            print('DRADV6 Success')
        except:
            print('DRADV6 Fail')

    def enableBridgeBPDUs(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "BridgeBPDUs"
                    ]
                }
            }, verify=False)
            print('BridgeBPDUs Success')
        except:
            print('BridgeBPDUs Fail')

    def enableMediaClassification(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "mediaclassification"
                    ]
                }
            }, verify=False)
            print('Media Classification Success')
        except:
            print('Media Classification Fail')

    def enableULFD(self):
        try:
            requests.post(self.apiUrlEnable, headers=self.headers, json={
                "nsmode": {
                    "mode": [
                        "ULFD"
                    ]
                }
            }, verify=False)
            print('ULFD Success')
        except:
            print('ULFD Fail')
