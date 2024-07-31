# src/main.py

import sys
import os

# Ensure the path includes the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(sys.path)

from http_requests.request_handler import RequestHandler
from http_requests.response_analyzer import ResponseAnalyzer
from detection.boolean_based import BooleanBasedDetection
from detection.error_based import ErrorBasedDetection
from detection.time_based import TimeBasedDetection
from detection.union_based import UnionBasedDetection
from detection.blind_boolean_based import BlindBooleanBasedDetection  # Import the new module

# ANSI escape sequences for text color and formatting
RED = '\033[91m'  # Red color
ENDC = '\033[0m'   # Reset color and formatting

def main():
    url = input("Enter the URL to test: ").strip()  # Ensure no extra spaces or characters
    param = input("Enter the parameter to test: ").strip()

    # Boolean-Based Detection
    print("Testing GET request with boolean-based SQL injection detection...")
    boolean_detection = BooleanBasedDetection(url)
    if boolean_detection.is_vulnerable(param):
        print(RED + "The parameter is vulnerable to boolean-based SQL injection!" + ENDC)
    else:
        print("The parameter is not vulnerable to boolean-based SQL injection.")

    # Error-Based Detection
    print("Testing GET request with error-based SQL injection detection...")
    error_detection = ErrorBasedDetection(url)
    if error_detection.is_vulnerable(param):
        print(RED + "The parameter is vulnerable to error-based SQL injection!" + ENDC)
    else:
        print("The parameter is not vulnerable to error-based SQL injection.")

    # Time-Based Detection
    print("Testing GET request with time-based SQL injection detection...")
    time_detection = TimeBasedDetection(url)
    if time_detection.is_vulnerable(param):
        print(RED + "The parameter is vulnerable to time-based SQL injection!" + ENDC)
    else:
        print("The parameter is not vulnerable to time-based SQL injection.")

    # Union-Based Detection
    print("Testing GET request with union-based SQL injection detection...")
    union_detection = UnionBasedDetection(url)
    if union_detection.is_vulnerable(param):
        print(RED + "The parameter is vulnerable to union-based SQL injection!" + ENDC)
    else:
        print("The parameter is not vulnerable to union-based SQL injection.")

    # Blind Boolean-Based Detection
    print("Testing GET request with blind boolean-based SQL injection detection...")
    blind_boolean_detection = BlindBooleanBasedDetection(url)
    if blind_boolean_detection.is_vulnerable(param):
        print(RED + "The parameter is vulnerable to blind boolean-based SQL injection!" + ENDC)
    else:
        print("The parameter is not vulnerable to blind boolean-based SQL injection.")

if __name__ == "__main__":
    main()
