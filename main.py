import json
import random


def print_op_info(op, guess):
    with open("data.json") as f:
        data = json.load(f)

    attrs = ["Sex", "Position", "Organization", "Role", "Speed", "Armor", "Year", "Secondary Gadgets"]

    for operator in data["operators"]:
        if operator["name"] == guess:
            for attr in attrs:
                if attr == "Secondary Gadgets" or attr == "Role":
                    counter = 0
                    for gadget in operator[attr.lower()]:
                        if gadget in op[attr.lower()]:
                            counter = counter + 1

                    if counter == len(op[attr.lower()]):
                        color = "\033[1;32m"
                    elif counter > 0:
                        color = "\033[1;93m"
                    else:
                        color = "\033[1;31m"
                elif attr == "Year":
                    if op[attr.lower()] == operator[attr.lower()]:
                        color = "\033[1;32m"
                    elif op[attr.lower()] > operator[attr.lower()]:
                        color = "\033[1;31m (too old) "
                    else:
                        color = "\033[1;31m (too new) "
                else:
                    if str(op[attr.lower()]) == str(operator[attr.lower()]):
                        color = "\033[1;32m"
                    else:
                        color = "\033[1;31m"
                print(attr + ": " + color + str(operator[attr.lower()]) + "\033[0;0m") # , end = '\t')
            print("\033[0;0m")
            break


def op_of_the_day():
    with open("data.json") as f:
        data = json.load(f)


    random_number = random.randint(0, len(data["operators"]) - 1)
    selected_op = data["operators"][random_number]


    guess = "NULL"
    while guess != selected_op["name"]:
        guess = input("Guess the operator: ")
        print_op_info(selected_op, guess)
    print("\033[1;32mYou guessed correctly!\033[0;0m")


def quotes():
    with open("data.json") as f:
        data = json.load(f)


    random_number = random.randint(0, len(data["operators"]) - 1)
    selected_op = data["operators"][random_number]
    while len(selected_op["quotes"]) < 4:
        random_number = random.randint(0, len(data["operators"]) - 1)
        selected_op = data["operators"][random_number]


    quotes = []
    guess = "NULL"
    mod = True
    while guess != selected_op["name"] or len(quotes) == 0:
        if len(quotes) < 4 and mod:
            random_number = random.randint(0, len(selected_op["quotes"]) - 1)
            while random_number in quotes:
                random_number = random.randint(0, len(selected_op["quotes"]) - 1)
            quotes.append(random_number)
            
            mod = False
            print("Quote: \033[1;94m" + selected_op["quotes"][random_number] + "\033[0;0m")
        else:
            mod = True
        guess = input("Guess the operator: ")
    print("\033[1;32mYou guessed correctly!\033[0;0m")


def main():
    print("Welcome to the Rainbow Six Siege Operator Database!")
    print("Please select an option:")
    print("1. Operator of the Day")
    print("2. Quotes")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        print("\n\n")
        op_of_the_day()
    elif choice == "2":
        print("\n\n")
        quotes()
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()