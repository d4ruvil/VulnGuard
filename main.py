import os
import subprocess

def print_logo():
    logo = """
    .___ _____                    .__.__   
  __| _//  |  |_______ __ _____  _|__|  |  
 / __ |/   |  |\_  __ \  |  \  \/ /  |  |  
/ /_/ /    ^   /|  | \/  |  /\   /|  |  |__
\____ \____   | |__|  |____/  \_/ |__|____/
     \/    |__|                            
    """

    print(logo)


MAX_WORKERS = 20

def run_xxe():
    print("Running XXE Detection...")
    xxe_detector_main_path = 'xxe_detector/main.py'
    subprocess.run(['python', xxe_detector_main_path], check=True)

def run_csrf():
    print("Running CSRF Detection...")
    csrf_detector_path = 'csrf_detector/main.py'
    subprocess.run(['python', csrf_detector_path], check=True)

def run_ssrf():
    print("Running SSRF Detection...")
    ssrf_detector_main_path = 'ssrf_detector/main.py'
    subprocess.run(['python', ssrf_detector_main_path], check=True)

def run_sql_injection():
    print("Running SQL Injection Detection...")
    # Specify the path to the SQL injection main.py file inside sql_injector_tool/src/detection
    sql_injection_main_path = 'sql_injector_tool/src/detection/main.py'
    subprocess.run(['python', sql_injection_main_path], check=True)

def main():
    print_logo()
    print("Select the tools to run:")
    print("1. XXE Detection")
    print("2. CSRF Detection")
    print("3. SSRF Detection")
    print("4. SQL Injection Detection")
    print("5. All")
    
    choice = input("Enter your choice (1/2/3/4/5): ").strip()

    if choice == '1':
        run_xxe()
    elif choice == '2':
        run_csrf()
    elif choice == '3':
        run_ssrf()
    elif choice == '4':
        run_sql_injection()
    elif choice == '5':
        run_xxe()
        run_csrf()
        run_ssrf()
        run_sql_injection()
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
