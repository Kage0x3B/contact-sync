import requests
import time
import json


class DocspellApi:
    def __init__(self, host: str):
        self.host = host

        self.api_token = ""
        self.token_created_time = -1
        self.token_valid_ms = -1

    def _api_route(self, path: str) -> str:
        return self.host + "/api/v1" + path

    def _auth_headers(self, skip_token_validation=False) -> dict:
        if self.token_valid_ms == -1:
            raise RuntimeError("Not authenticated")

        if not skip_token_validation and self.token_created_time + self.token_valid_ms > time.time():
            self._refresh_token()

        return {
            "X-Docspell-Auth": self.api_token
        }

    def _update_authentication(self, auth_data: dict) -> None:
        self.api_token = auth_data["token"]
        self.token_created_time = time.time()
        self.token_valid_ms = auth_data["validMs"]

    def authenticate(self, username: str, password: str) -> None:
        r = requests.post(self._api_route("/open/auth/login"), json={
            "account": username,
            "password": password,
            "rememberMe": True
        }).json()

        self._update_authentication(r)

        print("Authenticated with Docspell, user " + r["user"])

    def _refresh_token(self) -> None:
        r = requests.post(self._api_route("/sec/auth/session"),
                          headers=self._auth_headers(skip_token_validation=True)).json()

        self._update_authentication(r)
