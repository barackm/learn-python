import random

secret_number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == secret_number:
            print("You got it, congrats 👏👏")
            break
        elif guess > secret_number:
            print("Too high")
        else:
            print("Too low")
            
    except ValueError:
        print("Please enter valid number")
    
    