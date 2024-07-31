# src/detection/blind_boolean_based.py

import requests

class BlindBooleanBasedDetection:
    def __init__(self, url):
        self.url = url

    def is_vulnerable(self, param):
        payload = f"{param}=' AND 1=1-- "

        true_payload = {param: payload}
        false_payload = {param: payload.replace("1=1", "1=2")}

        true_response = requests.get(self.url, params=true_payload)
        false_response = requests.get(self.url, params=false_payload)

        if self._is_different(true_response, false_response):
            return True
        return False

    def _is_different(self, response1, response2):
        # Implement logic to compare responses for differences
        return response1.text != response2.text
