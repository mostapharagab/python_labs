import random

def run_rand_data_gen():
    def user_input():
        while True:
            num = input("Please Enter The Number Of Random Numbers You Want To Generate:  ")
            try:
                num = int(num)
                return num
            except Exception:
                print("Invalid Number Please Try Again!!!")


    num = user_input()


    sum_of_rands = 0

    with open('random_numbers.csv', 'w') as file:

        for i in range(1,num+1):
            x = random.randint(1, 100000)
            sum_of_rands+=x
            file.writelines(f"{i}, {x}\n")

    print(f"count of generated number={num}\navg of generated number={sum_of_rands/num}")