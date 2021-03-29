import requests
import time
import json


class DocspellApi:
    def __init__(self, host):
        self.host = host

        self.api_token = ""
        self.token_created_time = -1
        self.token_valid_ms = -1

    def api_route(self, path):
        return self.host + "/api/v1" + path

    def auth_headers(self):
        if self.token_valid_ms == -1:
            raise RuntimeError("Not authenticated")

        if self.token_created_time + self.token_valid_ms > time.time():
            self.refresh_token()

        return {
            "X-Docspell-Auth": self.api_token
        }

    def authenticate(self, username, password):
        r = requests.post(self.api_route("/open/auth/login"), json={
            "account": username,
            "password": password,
            "rememberMe": True
        }).json()

        self.api_token = r["token"]
        self.token_created_time = time.time()
        self.token_valid_ms = r["validMs"]

        print("Authenticated with Docspell, user " + r["user"])

    def refresh_token(self):
        pass
