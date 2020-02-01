import pytest
from source.eti_maze_game import mainMenu
from source.base import set_keyboard_input, get_display_output

def test_mainMenu_loadMaze():
    set_keyboard_input([1, ''])
    mainMenu()
    output = get_display_output()
    assert output == [" \nMAIN MENU \n=========\
\n[1]  Read and load maze from file \n[2]  \
View maze \n[3]  Play maze game \
 \n[4]  Configure current maze \n \n[0]  Exit Maze\n", 
                        'Enter your option:', "Option [1] Read and load maze from file", "Enter the name of the data file:"]

def test_mainMenu_viewMaze():
    set_keyboard_input([2])
    mainMenu()
    output = get_display_output()
    assert output == [" \nMAIN MENU \n=========\
\n[1]  Read and load maze from file \n[2]  \
View maze \n[3]  Play maze game \
 \n[4]  Configure current maze \n \n[0]  Exit Maze\n", 
                        'Enter your option:', "Option [2] View Maze"]

def test_mainMenu_playMaze():
    set_keyboard_input([3])
    mainMenu()
    output = get_display_output()
    assert output == [" \nMAIN MENU \n=========\
\n[1]  Read and load maze from file \n[2]  \
View maze \n[3]  Play maze game \
 \n[4]  Configure current maze \n \n[0]  Exit Maze\n", 
                        'Enter your option:', "Option [3] Play maze game"]

def test_mainMenu_configureMaze():
    set_keyboard_input([4])
    mainMenu()
    output = get_display_output()
    assert output == [" \nMAIN MENU \n=========\
\n[1]  Read and load maze from file \n[2]  \
View maze \n[3]  Play maze game \
 \n[4]  Configure current maze \n \n[0]  Exit Maze\n", 
                        'Enter your option:', "Option [4] Configure current maze", 
                        " \nCONFIGURATION MENU \n==================\
\n[1]  Create wall \n[2]  \
Create passageway \n[3]  Create start point \
 \n[4]  Create end point \n \n[0]  Exit to Main Menu\n", "Enter your option:"]

def test_mainMenu_invalidInput():
    set_keyboard_input([5])
    mainMenu()
    output = get_display_output()
    assert output == [" \nMAIN MENU \n=========\
\n[1]  Read and load maze from file \n[2]  \
View maze \n[3]  Play maze game \
 \n[4]  Configure current maze \n \n[0]  Exit Maze\n", 
                        'Enter your option:', "Invalid option. Please try again."]