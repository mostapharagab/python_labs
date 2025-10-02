import re



def run_email_validator():
    def make_log_file():
        lines = [
            "mostafaragab\n",
            "0dfjkdslfd\n",
            "email@gmai.com\n",
            "not@hotmail.com\n",
            "@gmail\n",
            "@gmail.com\n",
            "yes@nu.edu.eg\n",
            "0100@gmail.com\n",
            "facebook.com\n",
            "mymail.com\n"
        ]
        with open('filename.log', 'w') as file:
            file.writelines(lines)

    make_log_file()



    lines_set = set()
    with open('filename.log', 'r') as file:
        for line in file:
            if re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" , line.strip()):
                lines_set.add(line.strip())  



    print(f"Unique Valid Emails Found={len(lines_set)}")



    with open('valid_emails.txt', 'w') as file:
            for valid_email in lines_set:
                file.writelines(valid_email+"\n")


