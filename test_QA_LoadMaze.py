import pytest
from maze_game.mazecode import *
import csv
result = ""

def test_MazeEmpty():
    result = loadFile("")
    mazeList.clear()
    result =checkFile(mazeList)
    assert result =="No maze loaded."

def test_MazeLoaded():
    result = loadFile("maze.csv")
    result = checkFile(mazeList)
    assert result == "Maze loaded."