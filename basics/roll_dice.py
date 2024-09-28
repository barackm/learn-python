import random

while True:
    choice = input("Roll the dice? (y/n): ").lower()

    if choice == 'y':
        number_1 = random.randint(1, 6)
        number_2 = random.randint(1, 6)
        print(f"({number_1}, {number_2})")

    elif choice == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid number, choose between (y/n): ")