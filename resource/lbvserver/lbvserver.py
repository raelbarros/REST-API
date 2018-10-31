import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.exceptions.disable_warnings(InsecureRequestWarning)

class Lbvserver(object):

    def __init__(self, name, serviceType, vip):
        self.name = name
        self.serviceType = serviceType
        self.vip = vip

    # def lbvserver(self):
