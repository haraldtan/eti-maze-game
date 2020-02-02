import pytest
from maze_game.mazecode import *
import csv
result = ""
mazeList =["X","X","X","X","X","X","X","X","X","O","O","O","X","O","A",
           "X","X","O","X","O","X","O","X","X","X","O","X"
           ,"O","X","X","O","X","X","O","X","O","O","O","X","X","X","B"
           ,"X","X","X","X","X","X",]

def test_MazeLoaded():
    result = checkFile(mazeList)
    assert result == "Maze loaded."
    
def test_MazeEmpty():
    mazeList.clear()
    result =checkFile(mazeList)
    assert result =="No maze loaded."
