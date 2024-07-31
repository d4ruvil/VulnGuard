# VulnGuard
VulnGuard is a powerful Python-based security tool designed to detect and identify critical web vulnerabilities, including SQL Injection (SQLi), Cross-Site Request Forgery (CSRF), Server-Side Request Forgery (SSRF), and XML External Entity (XXE) attacks.

# VulnGuard

VulnGuard is a Python-based security tool designed to detect if a provided URL has CSRF, SSRF, XXE, or SQLi vulnerabilities. If a vulnerability is found, the tool will provide detailed output.

## Description

VulnGuard is a tool made in Python that detects critical web vulnerabilities including:
- Cross-Site Request Forgery (CSRF)
- Server-Side Request Forgery (SSRF)
- XML External Entity (XXE)  **Note:** XXE detection currently supports only "PortSwigger Labs" XXE challenges.
- SQL Injection (SQLi)

When a vulnerability is detected, VulnGuard provides clear and informative output to help you secure your web applications.

## Installation Instructions

To install VulnGuard, simply clone the repository and run the main file:

```bash
git clone https://github.com/d4ruvil/VulnGuard/
```
```bash
cd VulnGuard
```
```bash
python main.py
```
## Usage

Follow these steps to use VulnGuard:

1. Clone the repository:
    ```bash
    git clone https://github.com/d4ruvil/VulnGuard.git
    ```

2. Navigate to the VulnGuard directory:
    ```bash
    cd VulnGuard
    ```

3. Run the main file:
    ```bash
    python main.py
    ```

## Features

- Detects CSRF, SSRF, XXE, and SQLi vulnerabilities.
- Uses predefined payloads to test for various vulnerabilities.
- Parses and analyzes HTML responses to identify potential security flaws.
- Provides clear and colored console output for better readability.
- Easy integration into existing security workflows.
- **Note:** XXE detection currently supports only "PortSwigger Labs" XXE challenges.


## Requirements

Make sure to install the necessary dependencies before running VulnGuard. You can install them using pip:

```bash
pip install requests colorama beautifulsoup4
