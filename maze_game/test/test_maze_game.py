import pytest
from source import eti_maze_game

def test_mainMenu():
    output = eti_maze_game.mainMenu()
    assert output == 'Option [1] Read and load maze from file'
