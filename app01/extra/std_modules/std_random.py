import random

while True:
    try:
        low_bound = int(input("Enter the lower bound: "))
        upper_bound = int(input("Enter the upper bound: "))
        random_number = random.randint(low_bound, upper_bound)
        print(random_number)
    except ValueError as err:
        print("Error! Please enter a valid number.")
        print("Error Message:", err)
    except NameError as err:
        print("Error! Please enter a valid number.")
        print("Error Message:", err)

    status = input("Enter x to exit: ")
    if status == "x":
        break
