import pytest
from main import latest_time_compiler


def test_latest_time_compiler_syntax():
    """Tests formatting of the digital clock"""
    # Arrange
    user_input = [0, 0, 0, 0]
    # Act
    result = latest_time_compiler(user_input)
    # Assert
    assert result == "00:00"


def test_latest_time_compiler_midnight():
    """"Tests that 00 for the hour is chosen over any other combination of numbers"""
   # Arrange
    user_input = [0, 0, 1, 2]
    # Act
    result = latest_time_compiler(user_input)
    # Assert
    assert result == "00:21"


def test_latest_time_compiler_first_num():
    """Test that the first number on the digital clock must be a 0,1,2"""
    # Arrange
    user_input = [1, 2, 3, 4]
    # Act
    result = latest_time_compiler(user_input)
    # Assert
    assert result == "21:43"


def test_latest_time_compiler_maximum_minute():
    """Tests that for the minute clock it doesn't exceed 59"""
    # Arrange
    user_input = [1, 9, 5, 6]
    # Act
    result = latest_time_compiler(user_input)
    # Assert
    assert result == "19:56"


def tests_latest_time_compiler_unreasonable_numbers():
    """Tests that the inputs can be compiled to actual digital time"""
    user_input = [1, 9, 9, 9]
    # Act
    result = latest_time_compiler(user_input)
    # Assert
    assert result == "ValueError, invalid input"


# def tests_latest_time_compiler_length_of_input():
#     """Tests that the inputs are length 4"""
#     user_input = [1, 2, 3, 4, 5]
#     # Act
#     result = len(user_input)
#     # Assert
#     raise ValueError("")
