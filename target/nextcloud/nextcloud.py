import owncloud
import os
from cronohub import target_plugin
from multiprocessing import Pool


class TargetPlugin(target_plugin.CronohubTargetPlugin):
    ownClient = None

    def __init__(self):
        print('initialising next cloud target plugin')

    def validate(self):
        for v in [
            'CRONOHUB_NEXTCLOUD_URL',
            'CRONOHUB_NEXTCLOUD_USERNAME',
            'CRONOHUB_NEXTCLOUD_PASSWORD'
        ]:
            if v not in os.environ:
                print("Please set %s environment variable." % v)
                return False
        return True

    def help(self):
        print('''
        NextCloud location URL: CRONOHUB_NEXTCLOUD_URL (https://username.ocloud.de)
        NextCloud Username: CRONOHUB_NEXTCLOUD_USERNAME (admin)
        NextCloud Password: CRONOHUB_NEXTCLOUD_PASSWORD (admin)
        ''')

    def upload(self, f):
        print("uploading %s..." % f[0])
        self.owncloud.put_file(f[0], f[1])

    def archive(self, files):
        url = os.environ['CRONOHUB_NEXTCLOUD_URL']
        user = os.environ['CRONOHUB_NEXTCLOUD_USERNAME']
        password = os.environ['CRONOHUB_NEXTCLOUD_PASSWORD']
        self.ownClient = owncloud.Client(url)
        self.ownClient.login(user, password)
        with Pool(5) as p:
            p.map(self.upload, files)
