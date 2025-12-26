"""Build a Rock,Paper,Scissors game as a set of small functions
Requirements:
- At least three functions of your own design
- Type hints and doc-strings!
- Logic functions must use return values, don't print inside them
- The game should let a person play Rock,Paper,Scissors against the computer"""

import random


def computer():
    return random.randint(0, 2)


def user_play(player_choice):
    if player_choice in [0, 1, 2]:
        print(f"You chose {player_choice}")
        return player_choice
    else:
        raise ValueError("Invalid input. Type an integer in [0,1,2]")


def rock_paper_scissors(user_choice: int, computer_choice: int) -> str:
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


if __name__ == "__main__":
    game_play = True
    while game_play:
        user_choice = int(
            input("\nType 0 for Rock, 1 for Paper, and 2 for Scissors:\t"))
        computer_choice = computer()
        try:
            print(rock_paper_scissors(user_choice, computer_choice))
        except ValueError:
            print("Invalid input. Please choose an int value of either 0,1, or 2.")
            rock_paper_scissors(user_choice)
        play_game = input(
            "\nWould you like to play another round of 'Rock, Paper, Scissors'. If yes type 'y', if not type 'n':\t").lower().strip()
        if play_game == "n":
            game_play = False

    # You must always kee "game logic" separate from input and output.
    # Separate the parts that depend on randomness from use inputs so that it's testable (logic separate from input separate from output)
    # You must not let functions mix concerns so each function must be isolated
    # Logic specific functions must NOT ask for inputs and print
    # Logic never talks directly to input and output
    # Keep functions small and testable
    # Separation of concerns
