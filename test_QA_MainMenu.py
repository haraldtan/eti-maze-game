import pytest
from maze_game.mazecode import *

def test_selectedOptionInvalid():
    value = selectedOption("5")
    assert value == 'Invalid option. Please try again.'

def test_selectedOptionAlphabet():
    value = selectedOption("a")
    assert value == 'Invalid option. Please try again.'

def test_menu_selectionSpace1():
    value = selectedOption(" 1","skip")
    assert value == "Option [1] Read and load maze from file"

def test_menu_nogameLoaded():
    value = selectedOption("3", "skip")
    assert value == "Maze not loaded."

def test_menu_selection1():
    value = selectedOption("1","skip")
    assert value == "Option [1] Read and load maze from file"

def test_menu_selection2():
    value = selectedOption("2","skip")
    assert value == "Option [2] View Maze"

def test_menu_selection3():
    value = selectedOption("3","skip")
    assert value == "Option [3] Play maze game"

def test_menu_selection4():
    value = selectedOption("4","skip")
    assert value == "Option [4] Configure current maze"

def test_menu_selection0():
    value = selectedOption("0","skip")
    assert value == False
