# -*- coding: utf-8 -*-
"""
钉钉群自定义机器人
"""

import json
import requests
import time
import hmac
import hashlib
from urllib.parse import quote_plus
import base64


class DingTalkRobot(object):
    """docstring for DtRobot"""
    url = "https://oapi.dingtalk.com/robot/send?access_token="

    token: str = ""
    secret: str = ""

    def __init__(self, token: str, secret: str = ""):
        # super(DingTalkRobot, self).__init__()
        self.url = self.url + token
        self.token = token
        self.secret = secret

    def set_secret(self, secret: str = ""):
        self.secret = secret

    def _sign(self, timestamp):
        secret_enc = bytes(self.secret, 'utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        string_to_sign_enc = bytes(string_to_sign, 'utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        return quote_plus(base64.b64encode(hmac_code))

    def send_text(self, msg, is_at_all=False, at_mobiles=[]):
        data = {"msgtype": "text", "text": {"content": msg}, "at": {"atMobiles": at_mobiles, "isAtAll": is_at_all}}
        return self.post(data)

    def send_markdown(self, title, text):
        data = {"msgtype": "markdown", "markdown": {"title": title, "text": text}}
        return self.post(data)

    def post(self, data):
        msg = json.dumps(data)
        if self.secret:
            timestamp = int(round(time.time() * 1000))
            url = "{url}&timestamp={timestamp}&sign={sign}".format(url=self.url, timestamp=timestamp, sign=self._sign(timestamp))
        else:
            url = self.url

        header = {"content-type": "application/json"}
        response = requests.post(url, data=msg, headers=header, timeout=3)
        if response.status_code is not 200:
            raise Exception("send dingTalk message failed, status_code: {}, result: {}".
                               format(response.status_code, response.text))
        ret = json.loads(response.text)
        if ret.get("errcode") == 0 and ret.get("errmsg") == "ok":
            return True
        else:
            raise Exception("send dingTalk message failed, result: " + response.text)
