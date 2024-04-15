import random

Comp_w = 0
Player_W = 0
options = ["rock", "paper", "scissors"]

print("Welcome to Rock- Paper - Scissors Mini Game:")

while True:
    Player_input = input("Pick your choice: Rock - Paper - Scissors. Please select E to exit program: ").lower()

    if Player_input == "e":
        print("Scores:")
        print("Computer score:", Comp_w, "wins.")
        print("Player score:", Player_W, "wins.")
        print("Goodbye!")
        break

    if Player_input not in options:
        continue

    random_number = random.randint(0, 2)
    comp_choice = options[random_number]
    print("Computer Choice =", comp_choice + ".")

    if Player_input == "rock" and comp_choice == "scissors":
        print("You are the winner!")
        Player_W += 1

    elif Player_input == "paper" and comp_choice == "rock":
        print("You are the winner!")
        Player_W += 1

    elif Player_input == "scissors" and comp_choice == "paper":
        print("You are the winner!")
        Player_W += 1

    else:
        print("Computer is the winner!")
        Comp_w += 1

    print("Scores:")
    print("Computer score:", Comp_w, "wins.")
    print("Player score:", Player_W, "wins.")
