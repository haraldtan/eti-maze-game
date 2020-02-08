import pytest
from maze_game.mazecode import *
import csv
result =''
maze = mazeList

def test_moveQ():
    result= playMaze('Q')
    assert result=="Invalid Movement. Please Try again"

def test_move1():
    result= playMaze('1')
    assert result=="Invalid Movement. Please Try again"

def test_moveRA():
    result= playMaze('')
    assert result=="Invalid Movement. Please Try again"
    
def test_moveD():
    result= playMaze('D')
    assert result=="Invalid Movement. Please Try again"

def test_moveA():
    result= playMaze('D')
    assert result=="Invalid Movement. Please Try again"
    
def test_moveDValid():
    result= playMaze('D')
    assert result=="Move Successful!"
    
def test_moveSValid():
    result= playMaze('S')
    assert result=="Move Successful!"
    
def test_moveAValid():
    result= playMaze('A')
    assert result=="Move Successful!"
    
def test_moveWValid():
    result= playMaze('W')
    assert result=="Move Successful!"
    
def test_moveM():
    result= playMaze('M')
    assert result== False

