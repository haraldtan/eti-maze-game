import pytest
from src.eti_maze_game import eti_maze_game

def test_mainMenu():
    input_value = 2

    # go about using input() like you normally would:
    i = input("Enter your option:")
    assert i == "Mark"
