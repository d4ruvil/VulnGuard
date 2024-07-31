import os
import requests
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin

# Initialize logging
logging.basicConfig(filename='csrf_detector.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Load CSRF token names from file
def load_csrf_token_names(filename='csrf_tokens.txt'):
    with open(filename, 'r') as file:
        token_names = [line.strip() for line in file if line.strip()]
    return token_names


# Read payloads from file
def load_payloads(filename='csrf_payloads'):
    with open(filename, 'r') as file:
        payloads = [line.strip() for line in file if line.strip()]
    return payloads

def detect_csrf_vulnerability(url, session=None):
    if session is None:
        session = requests.Session()

    try:
        response = session.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f'Error fetching URL: {e}')
        print(f'Error fetching URL: {e}')
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    forms = soup.find_all('form')
    csrf_token_names = load_csrf_token_names()

    vulnerable_forms = []

    for form in forms:
        has_csrf_token = any(form.find('input', {'name': token_name}) for token_name in csrf_token_names)

        if not has_csrf_token:
            vulnerable_forms.append(form)
            if submit_form_and_check(url, form, session):
                print("\033[91m[WARNING] Found CSRF vulnerability in the form!\033[0m")  # Red text for vulnerability
                logging.info(f'Vulnerable form found: {form}')
                print(f'Vulnerable form found: {form}')

    if vulnerable_forms:
        logging.info(f'Found {len(vulnerable_forms)} vulnerable form(s) on {url}')
        print(f'Found {len(vulnerable_forms)} vulnerable form(s) on {url}')
    else:
        logging.info(f'No vulnerable forms found on {url}')
        print('NO CSRF FOUND ON THE SITE')

def submit_form_and_check(base_url, form, session):
    action = form.get('action')
    method = form.get('method', 'get').lower()
    form_data = {input.get('name'): input.get('value') for input in form.find_all('input') if input.get('name')}
    
    # Add CSRF token if not already present
    csrf_token_names = load_csrf_token_names()
    if not any(token_name in form_data for token_name in csrf_token_names):
        csrf_token_name = 'csrf_token'
        csrf_token_value = 'your_csrf_token_value_here'  # Replace with actual CSRF token value
        form_data[csrf_token_name] = csrf_token_value

    url = urljoin(base_url, action)

    try:
        if method == 'post':
            response = session.post(url, data=form_data)
        else:
            response = session.get(url, params=form_data)
        response.raise_for_status()
        logging.info(f'Successful {method.upper()} request to {url}')
        print(f'Successful {method.upper()} request to {url}')
        return response.status_code == 200
    except requests.RequestException as e:
        logging.error(f'Error submitting form to {url}: {e}')
        print(f'Error submitting form to {url}: {e}')
        return False

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='CSRF Vulnerability Detector')
    parser.add_argument('--url', help='The URL to test for CSRF vulnerabilities')
    args = parser.parse_args()

    url = args.url if args.url else input("Enter the URL to test for CSRF vulnerabilities: ")

    detect_csrf_vulnerability(url)
