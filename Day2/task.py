import random


def five_numbers():
    print("Hello, Please Enter 5 Numbers")
    lst = []
    while len(lst) != 5:
        x = input(f"Please Enter The {len(lst) + 1} Number\n")
        if x.isdigit() is False:
            print("Please Enter A Valid Number")
            continue
        lst.append(int(x))
    print("Ascending Order")

    srted = sorted(lst)
    for index, value in enumerate(srted):
        print(f"The number with index:{index} is equal to {value}")

    srted = sorted(lst, reverse=True)

    print("Descending Order")
    for index, value in enumerate(sorted(lst, reverse=True)):
        print(f"The number with index:{index} is equal to {value}")


def len_and_start():
    while True:
        lngth = input("Please Enter The Length: ")
        st = input("Please Enter The Starting Point: ")
        if lngth.isdigit() and st.isdigit():
            st = int(st)
            lngth = int(lngth)

            for i in range(st, st + lngth):
                print(i, end=" ")
            break


def until_done():
    count_of_numbers = 0
    sum_of_numbers = 0
    while True:
        num = input("Pleae Enter A Valid Number, If you Want to Exit type 'done': ")
        if num == "done":
            break
        if num.isdigit():
            sum_of_numbers += int(num)
            count_of_numbers += 1
        else:
            print("The Number Is Not Valid Try Again!!")

    print(
        f"Total of all number entered: {sum_of_numbers}\nThe Count of Valid Enteries: {count_of_numbers}\nThe Average:{sum_of_numbers / count_of_numbers}"
    )


# until_done()


def no_duplicate_sorted():
    lst = []
    while True:
        num = input("Pleae Enter A Valid Number, If you Want to Exit type 'done': ")
        if num == "done":
            break
        if num.isdigit():
            lst.append(int(num))
        else:
            print("The Number Is Not Valid Try Again!!")

    lst.sort()
    nwlst = []
    for x in lst:
        if nwlst and x == nwlst[-1]:
            continue
        nwlst.append(x)

    print("sorted non duplicated list:")
    print(nwlst)


def sentence_count():
    while True:
        sentence = input("PLeae Enter A Sentence: ")
        if sentence:
            mp = dict()
            lst_of_words = sentence.split(" ")
            for word in lst_of_words:
                if word in mp:
                    mp[word] += 1
                else:
                    mp[word] = 1

            for x in mp:
                print(f'The word "{x}" appeard {mp[x]} times.')
            break
        print("Invalid Sentence Pleae Try Again")


def grade_book():
    lst_of_scores = []
    while len(lst_of_scores) != 5:
        x = input(
            f"\nPlease Enter The Score of The Student Number {len(lst_of_scores) + 1}: "
        )
        if (
            (x.count(".") > 1)
            or (len(x.strip()) != len(x))
            or x(any(ch.isalpha for ch in x))
        ):
            print("Invalid Score Please Try Again")
            continue
        lst_of_scores.append(int(x))

    print(
        f"Max score is {max(lst_of_scores)}\nMin Score is {min(lst_of_scores)}\nAverage Score is {sum(lst_of_scores) / len(lst_of_scores)}\n"
    )


def add_item(hashmap):
    while True:
        item_name = input("Enter your Item Name: ")
        item_price = input("Enter your Item Price: ")

        if not item_price.isdigit() or not item_name.isalpha():
            print("Invalid Item. Please Try Again.")
            continue

        hashmap[item_name] = int(item_price)
        break


def remove_item(hashmap):
    while True:
        item_name = input("Enter your Item Name: ")

        if not item_name.isalpha() or item_name not in hashmap:
            print("Invalid Item. Please Try Again.")
            continue

        del hashmap[item_name]
        print("Item Removed Successfully")
        break


def view_all(hashmap):
    for item, price in hashmap.items():
        print(f"Item name: {item}, Price: {price}")


def display_total(hashmap):
    tot = sum(hashmap.values())
    print(f"Total Price is {tot}")


def shopping_cart():
    hashmap = dict()

    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Add an Item")
        print("2. Remove an Item")
        print("3. View All Items With Their Prices")
        print("4. Display The Total Cost")

        option = input("Enter your choice: ")

        if option.isdigit() and 1 <= int(option) <= 4:
            option = int(option)  # convert before match
            match option:
                case 1:
                    add_item(hashmap)
                case 2:
                    remove_item(hashmap)
                case 3:
                    view_all(hashmap)
                case 4:
                    display_total(hashmap)
        else:
            print("Invalid choice. Please select 1–4.")


def guessing_game():
    random_number = random.randint(1, 20)

    while True:
        sel = input("Please Select A Number between 1 and 20: ")
        if sel and sel.isdigit():
            sel = int(sel)
            if sel < 1 or sel > 20:
                print("Number out of range! Try again.")
                continue

            if sel > random_number:
                print("Too High")
            elif sel < random_number:
                print("Too Low")
            else:
                print("Congratulations! You guessed it right!!!")
                break
        else:
            print("Invalid input. Please enter a number.")


functions = {
    1: ("Five Numbers (sort ascending/descending)", five_numbers),
    2: ("Length and Start sequence", len_and_start),
    3: ("Until Done (sum, count, avg)", until_done),
    4: ("No Duplicate Sorted List", no_duplicate_sorted),
    5: ("Sentence Word Count", sentence_count),
    6: ("Grade Book", grade_book),
    7: ("Shopping Cart", shopping_cart),
    8: ("Guessing Game", guessing_game),
}


def main_menu():
    while True:
        print("\n--- Main Menu ---")
        for fun in functions:
            print(f"{fun}. {functions[fun][0]}")
        print("9. Exit")

        choice = input("Select an option: ")
        if choice.isdigit():
            choice = int(choice)
            if choice in functions:
                print(f"\nRunning: {functions[choice][0]}\n")
                functions[choice][1]()
            elif choice == 9:
                print("Exiting Right Now!")
                break
            else:
                print("Invalid choice. Try again.")
        else:
            print("Please enter a number.")


main_menu()
