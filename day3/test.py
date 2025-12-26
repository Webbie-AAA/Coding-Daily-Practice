import pytest
from main import rock_paper_scissors, user_play


def test_rock_paper_scissors_draw():
    # Arrange
    user_choice = 0
    computer_choice = 0
    # Assert
    assert rock_paper_scissors(
        user_choice, computer_choice) == "\nThe computer chose: " + str(computer_choice) + "\nIt's a draw"


def test_rock_paper_scissors_rock_beats_scissors():
    # Arrange
    user_choice = 0
    computer_choice = 2
    # Act
    result = rock_paper_scissors(user_choice, computer_choice)
    # Assert
    assert result == "\nThe computer chose: " + \
        str(computer_choice) + "\nYou win"


def test_rock_paper_scissors_paper_beats_rock():
    # Arrange
    user_choice = 1
    computer_choice = 0
    # Act
    result = rock_paper_scissors(user_choice, computer_choice)
    # Assert
    assert result == "\nThe computer chose: " + \
        str(computer_choice) + "\nYou win"


def test_rock_paper_scissors_scissors_beats_paper():
    # Arrange
    user_choice = 2
    computer_choice = 1
    # Act
    result = rock_paper_scissors(user_choice, computer_choice)
    # Assert
    assert result == "\nThe computer chose: " + \
        str(computer_choice) + "\nYou win"


def test_rock_paper_scissors_scissors_loses_to_paper():
    # Arrange
    user_choice = 1
    computer_choice = 2
    # Act
    result = rock_paper_scissors(user_choice, computer_choice)
    # Assert
    assert result == "\nThe computer chose: " + \
        str(computer_choice) + "\nYou loose"


def test_user_choice_input_error():
    with pytest.raises(ValueError):
        user_play(4)
