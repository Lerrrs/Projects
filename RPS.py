import random
draw = 0
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input in options:

        random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
        options = ["rock", "paper", "scissors"]
        computer_pick = options[random_number]
        print("computer picked", computer_pick + ".")

    if user_input == ("rock") and computer_pick == ("scissors"):
        print("You won!")
        user_wins += 1

    elif user_input == ("paper") and computer_pick == ("rock"):
        print("You won!")
        user_wins += 1

    elif user_input == ("scissors") and computer_pick == ("paper"):
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("Draw!")

    else:
        print("You lose!!")
        computer_wins += 1
