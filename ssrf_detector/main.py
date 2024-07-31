import requests
from colorama import init, Fore
import os
from payloads import payloads  # Import payloads from payloads.py

# Initialize colorama
init(autoreset=True)

# Define a function to send the payload and log the result
def send_payload(url, payload, headers=None):
    try:
        response = requests.get(url, params={"url": payload}, headers=headers)
        return response.status_code, response.text
    except requests.RequestException as e:
        return None, str(e)

# Define the main function
def main():
    target_url = input("Enter the target URL: ")

    results = []

    # Test each payload
    for attack_type, payload_list in payloads.items():
        for payload in payload_list:
            if attack_type == "referer_header":
                headers = {"Referer": payload}
                status_code, response_text = send_payload(target_url, "", headers)
            else:
                status_code, response_text = send_payload(target_url, payload)

            if status_code and status_code < 500:
                results.append({
                    "vulnerability_found": True,
                    "attack_type": attack_type,
                    "payload": payload,
                    "status_code": status_code,
                    "response": response_text
                })

    # Display results
    for result in results:
        if result["vulnerability_found"]:
            print(Fore.RED + "Vulnerability found!")
            print(Fore.RED + f"Attack Type: {result['attack_type']}")
            print(Fore.RED + f"Payload: {result['payload']}")

if __name__ == "__main__":
    main()
