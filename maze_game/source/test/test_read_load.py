import pytest
from source.eti_maze_game import *
import csv
result=""

def test_loadFile():
    
    result = loadFile("XXX.cxv")
    assert result == 'Invalid data file.'

def test_loadCapsFile():
    result =loadFile("MAZE.csv")
    assert result == 'Invalid data file.'
def test_correctFile():
    result = checkFile("maze.csv")
    assert result == 'Number of lines read: 8'

