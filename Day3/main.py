from log_time_decorator import log_time
from date_time_reminder import run_date_reminder
from email_validator import run_email_validator
from os_file_manager import run_os_file_manager
from product_data_transformer import run_product_data_transform
from random_data_gen import run_rand_data_gen
# import math_automation when ready

# Apply decorator to some functions here (or decorate inside their modules)
run_date_reminder = log_time(run_date_reminder)
run_email_validator = log_time(run_email_validator)

def main():
    tasks = {
        "1": ("Date Reminder", run_date_reminder),
        "2": ("Email Validator", run_email_validator),
        "3": ("OS File Manager", run_os_file_manager),
        "4": ("Product Data Transformer", run_product_data_transform),
        "5": ("Random Data Generator", run_rand_data_gen),
        "6": ("Math Automation", run_math_automation),
    }

    print("=== Task Menu ===")
    for num, (name, _) in tasks.items():
        print(f"{num}) {name}")

    while True:
        choice = input("Select task number: ").strip()
        if choice in tasks:
            print(f"\nRunning '{tasks[choice][0]}'...\n")
            tasks[choice][1]()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
