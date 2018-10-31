from auth.auth import Auth
from feature.features import Features
from mode.mode import Mode
from config.config import Config


class Main(object):
    def __init__(self):
        self.ip = '192.168.220.49'
        self.cookieId = None

    def main(self):
        auth = Auth(self.ip)
        self.cookieId = auth.login('nsroot', 'nsroot')

        config = Config('192.168.220.49', self.cookieId, 'nsRest', '192.168.50', '255.255.255.0', 'GTM-03:00-BRT-America/Sao_paulo')
        config.initialConf()

        # feature = Features(self.ip, self.cookieId)
        # feature.enableAppFirewall()

        # mode = Mode(self.ip, self.cookieId)
        # mode.enableULFD()

        auth.logoff(self.cookieId)


if __name__ == '__main__':
    Main().main()
