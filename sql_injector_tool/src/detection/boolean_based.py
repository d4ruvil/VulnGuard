import requests

class BooleanBasedDetection:
    def __init__(self, url):
        self.url = url

    def is_vulnerable(self, param):
        # Test payloads
        true_payload = {param: "1 OR 1=1"}
        false_payload = {param: "1 OR 1=2"}

        # Send requests
        true_response = requests.get(self.url, params=true_payload)
        false_response = requests.get(self.url, params=false_payload)

        # Compare responses
        if true_response.text != false_response.text:
            return True
        return False
