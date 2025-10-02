import os
import re

def run_os_file_manager():
    def user_input():
        while True:
            user_path = input("Enter the directory path where you want to create 'backup': ")
            backup_path = os.path.join(user_path, "backup")
            try:
                os.mkdir(backup_path)
                print(f"'backup' folder created successfully at: {backup_path}")
                return backup_path
            except FileExistsError:
                print(f"'backup' folder already exists at: {backup_path}")
                return backup_path
            except Exception:
                print("Invalid path. Please try again.")

    backup_path = user_input()
    current_path = "."
    all_entries = os.listdir(current_path)
    files = [f for f in all_entries if os.path.isfile(os.path.join(current_path, f))]
    lst_of_txt = list(filter(lambda name: re.match(r"^.+\.txt$", name, re.IGNORECASE), files))
    print("Text files found:", lst_of_txt)

    for txt_file in lst_of_txt:
        src = os.path.join(current_path, txt_file)
        dst = os.path.join(backup_path, txt_file)
        try:
            with open(src, "rb") as f_src:
                content = f_src.read()
            with open(dst, "wb") as f_dst:
                f_dst.write(content)
            print(f"Copied: {txt_file} → {backup_path}")
        except Exception as e:
            print(f"Failed to copy {txt_file}: {e}")
