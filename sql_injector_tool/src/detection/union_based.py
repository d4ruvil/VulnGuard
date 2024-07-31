# src/detection/union_based.py

import requests

class UnionBasedDetection:
    def __init__(self, url):
        self.url = url

    def is_vulnerable(self, param):
        # Test payload
        payload = {param: "1' UNION SELECT NULL-- "}

        # Send request
        response = requests.get(self.url, params=payload)

        # Check for successful injection
        if "error" in response.text.lower():
            return True
        return False
