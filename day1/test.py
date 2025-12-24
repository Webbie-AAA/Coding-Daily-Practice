import pytest
from main import capitalize_name


def test_capitalize_name_one_name():
    # Act
    name = "chRis"
    # Arrange
    result = capitalize_name(name)
    # Assert
    assert result == "Chris"


def test_capitalize_name_four_names():
    # Act
    name = "maya alice Jane johnson"
    # Arrange
    result = capitalize_name(name)
    # Assert
    assert result == "Maya Alice Jane Johnson"


def test_capitalize_name_no_name():
    # Act
    name = ""
    # Arrange
    result = capitalize_name(name)
    # Assert
    assert result == None
