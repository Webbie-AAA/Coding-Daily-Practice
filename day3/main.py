"""Build a Rock,Paper,Scissors game as a set of small functions
Requirements:
- At least three functions of your own design
- Type hints and doc-strings!
- Logic functions must use return values, don't print inside them
- The game should let a person play Rock,Paper,Scissors against the computer"""

import random


def computer():
    choice = random.randint(0, 2)
    return choice


def user_play():
    player_choice = int(
        input("\nType 0 for Rock, 1 for Paper, and 2 for Scissors:\t"))
    if player_choice in [0, 1, 2]:
        print(f"You chose {player_choice}")
        return rock_paper_scissors(player_choice)
    else:
        print("Invalid input. Please try again")


def rock_paper_scissors(user_choice: int) -> str:
    computer_choice = computer()
    user_choice = user_play()
    if user_choice == computer_choice:
        return "\nThe computer chose: " + str(computer_choice) + "\nIt's a draw"
    elif user_choice == 0 and computer_choice == 2:
        return "\nThe computer chose: " + str(computer_choice) + "\nYou win"
    elif user_choice == 2 and computer_choice == 0:
        return "\nThe computer chose: " + str(computer_choice) + "\nYou loose"
    elif user_choice > computer_choice:
        return "\nThe computer chose: " + str(computer_choice) + "\nYou win"
    elif user_choice < computer_choice:
        return "\nThe computer chose: " + str(computer_choice) + "\nYou loose"


game_play = True
while game_play:
    user_choice = user_play()
    try:
        print(rock_paper_scissors(user_choice))
    except ValueError:
        print("Invalid input. Please choose an int value of either 0,1, or 2.")
        rock_paper_scissors(user_choice)
    play_game = input(
        "\nWould you like to play another round of 'Rock, Paper, Scissors'. If yes type 'y', if not type 'n':\t").lower().strip()
    if play_game == "n":
        game_play = False
