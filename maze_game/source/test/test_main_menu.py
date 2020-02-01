import pytest
from source.eti_maze_game import *

def test_menu_selectionLetter():
    value = selectedOption("a")
    assert value == 'Invalid option. Please try again.'

def test_menu_selectionCharacter():
    value = selectedOption("@")
    assert value == 'Invalid option. Please try again.'

def test_menu_selection7():
    value = selectedOption("7")
    assert value == 'Invalid option. Please try again.'

def test_menu_selectionWord():
    value = selectedOption("one")
    assert value == 'Invalid option. Please try again.'

def test_menu_selectionTwoNumbers():
    value = selectedOption("2 2")
    assert value == 'Invalid option. Please try again.'

def test_menu_selectionNegative():
    value = selectedOption("-3")
    assert value == 'Invalid option. Please try again.'

def test_menu_selection1():
    value = selectedOption("1")
    assert value == "Option [1] Read and load maze from file"

def test_menu_selection2():
    value = selectedOption("2")
    assert value == "Option [2] View Maze"

def test_menu_selection3():
    value = selectedOption("3")
    assert value == "Option [3] Play maze game"

def test_menu_selection4():
    value = selectedOption("4")
    assert value == "Option [4] Configure current maze"

def test_menu_selection0():
    value = selectedOption("0")
    assert value == "Exit"