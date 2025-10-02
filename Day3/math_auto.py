import math

def run_math_automation():
    st = input("Please Enter The Numbers Comma Separated: ")
    lst = st.split(',')
    nwlst = []

    for x in lst:
        try:
            nwlst.append(float(x))
        except Exception:
            print(f"{x} is not a valid number")

    with open('math_report.txt', 'w') as file:
        file.write("number,floor,ceil,squareroot,area_of_a_circle\n")
        for x in nwlst:
            line = f"{x},{math.floor(x)},{math.ceil(x)},{math.sqrt(x)},{math.pi * (x**2)}\n"
            file.write(line)

    try:
        with open('math_report.txt', 'r') as file:
            print("File Was Created Successfully")
            all_content = file.read()
            print(all_content)
    except FileNotFoundError:
        print("File Not Found!!")

