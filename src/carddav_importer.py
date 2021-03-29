import os
import shutil
from webdav3.client import Client
from webdav3.exceptions import WebDavException


class CardDavImporter:
    def __init__(self, web_dav_host, web_dav_login, web_dav_password, card_dav_path):
        self.web_dav_host = web_dav_host
        self.web_dav_login = web_dav_login
        self.web_dav_password = web_dav_password
        self.card_dav_path = card_dav_path

        self.client: Client = None

    def connect(self):
        options = {
            'webdav_hostname': self.web_dav_host,
            'webdav_login': self.web_dav_login,
            'webdav_password': self.web_dav_password,
            'webdav_override_methods': {
                'check': 'GET'
            }
        }

        self.client = Client(options)

    def download_contacts(self):
        if not self.client:
            raise Exception("You have to connect first")

        local_path = os.getcwd() + "/tmp"

        if os.path.exists(local_path):
            shutil.rmtree(local_path)

        os.makedirs(local_path)

        for resource_name in self.client.list(self.card_dav_path):
            _remote_path = "{parent}/{name}".format(parent=self.card_dav_path, name=resource_name)
            _local_path = os.path.join(local_path, resource_name)

            if not _remote_path.endswith(".vcf"):
                continue

            try:
                print("Downloading " + _remote_path)
                self.client.download(local_path=_local_path, remote_path=_remote_path)
            except WebDavException as ex:
                print("Could not download " + resource_name)
