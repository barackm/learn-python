import random


def check_win(computer=str, user=str) -> bool:
    if (user == "r" and computer == "s" or 
        user == "s" and computer == "p" or
        user == "p" and computer == "r"
        ):
        return True
    else:
        return False

choices_to_emoji = {
    "r": "🪨",
    "p": "📃",
    "s": "✂"
}
choices = tuple(choices_to_emoji.keys())

while True:
    choice = input("Rock, paper, or scissor? (r/p/s): ").lower()
    computer_choice = random.choice(choices)

    if choice not in choices:
        print("Invalid choice!")
        continue
    else:
        final_decision = None
        result = f"You chose {choices_to_emoji[choice]}\nComputer chose {choices_to_emoji[computer_choice]}"
        if check_win(computer=computer_choice, user=choice):
            print(result)
            final_decision = input("You win! \n Continue? (y/n): ").lower()
        else:
            print(result)
            final_decision = input("You loose! \n Continue? (y/n): ").lower()

        if final_decision == "n":
            break
