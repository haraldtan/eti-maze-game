import pytest
from maze_game.mazecode import *
import csv
result=""

def test_loadFile():
    result = loadFile("XXX.csv")
    assert result == 'Invalid data file.'

def test_loadCapsFile():
    result =loadFile("maze.cxv")
    assert result == 'Invalid data file.'
    
def test_correctFile():
    result = loadFile("maze.csv")
    assert result == 'Number of lines read: 8'

