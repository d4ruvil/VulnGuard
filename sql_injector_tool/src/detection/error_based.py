import requests

class ErrorBasedDetection:
    def __init__(self, url):
        self.url = url

    def is_vulnerable(self, param):
        # Test payload
        payload = {param: "1'"}

        # Send request
        response = requests.get(self.url, params=payload)

        # Check for common SQL error messages
        error_messages = [
            "You have an error in your SQL syntax;",
            "Warning: mysql_fetch_array()",
            "Unclosed quotation mark after the character string",
            "quoted string not properly terminated"
        ]

        for error in error_messages:
            if error in response.text:
                return True
        return False
