import pytest
from maze_game.mazecode import *

def test_selectedOptionAlphabet():
    value = selectedOption("a")
    assert value == 'Invalid option. Please try again.'

def test_selectedOptionCharacter():
    value = selectedOption("@")
    assert value == 'Invalid option. Please try again.'

def test_selectedOptionInvalid():
    value = selectedOption("7")
    assert value == 'Invalid option. Please try again.'

def test_selectedOptionWord():
    value = selectedOption("one")
    assert value == 'Invalid option. Please try again.'

def test_selectedOptionNumbers():
    value = selectedOption("2 2")
    assert value == 'Invalid option. Please try again.'

def test_selectedOptionNegative():
    value = selectedOption("-3")
    assert value == 'Invalid option. Please try again.'

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
