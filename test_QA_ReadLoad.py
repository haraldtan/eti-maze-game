import pytest
from maze_game.mazecode import *
import csv
result = ""

def test_loadIncorrectFile():
    result = loadFile("mase.csv")
    assert result == 'Invalid data file.'

def test_loadIncorrectFileExt():
    result = loadFile("mase.jpg")
    assert result == 'Invalid data file.'

def test_loadIncorrectInput():
    result = loadFile("Hello")
    assert result == 'Invalid data file.'

def test_EmptyInput():
    result = loadFile("")
    assert result == 'Invalid data file.'
    
def test_correctFile():
    result = loadFile("maze.csv")
    assert result == 'Number of lines read: 8'
