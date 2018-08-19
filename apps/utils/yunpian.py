import requests
import json

class YunPian(object):
    def __init__(self,api_key):
        self.api_key = api_key
        self.single_send_url = ""

    def send_sms(self,code,mobile):
        parmas = {
            "api_key":self.api_key,
            "mobile":mobile,
            "text":"",
        }
        request = requests.post(self.single_send_url,data=parmas)

        re = json.loads(request.text)