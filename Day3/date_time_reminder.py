from datetime import datetime
from datetime import date
import re



def run_date_reminder():
    def date_input():
        while True:

            parsed_date = input("Please Enter The date you want YYYY-MM-DD:  ")
            pattern = r"^\d{4}-\d{2}-\d{2}$"

            if re.match(pattern, parsed_date):
                print("Valid date format")
                parsed_date = datetime.strptime(parsed_date, "%Y-%m-%d").date()
                break
            else:
                print("Invalid date format")
        return parsed_date

    today = date.today()
    pdate = date_input()
    days_left = (pdate - today).days
    if days_left >= 0:
        with open('reminders.txt', 'a') as file:
            file.writelines(f"{pdate} -> {days_left} days left\n")

    else:
        print("This date has already passed.")

