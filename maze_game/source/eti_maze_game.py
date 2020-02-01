import sys
import time

menu=(' \nMAIN MENU \n=========\
\n[1]  Read and load maze from file \n[2]  \
View maze \n[3]  Play maze game \
 \n[4]  Configure current maze \n \n[0]  Exit Maze\n')

configMenu=(' \nCONFIGURATION MENU \n==================\
\n[1]  Create wall \n[2]  \
Create passageway \n[3]  Create start point \
 \n[4]  Create end point \n \n[0]  Exit to Main Menu\n')

# Configure Maze Menu
def configurationMenu():
    print(configMenu)
    option = input("Enter your option: ")
    if option=='1':
        input()
        configurationMenu()
    elif option=='2':
        input()
        configurationMenu()
    elif option=='3':
        input()
        configurationMenu()
    elif option=='4':
        input()
        configurationMenu()
    elif option =='0':
        print()
        mainMenu()
    else:   
        print('Invalid option. Please try again.')
        input('')
        configurationMenu()

# Display the main menu
def mainMenu():
    print(menu)
    option = str(input('Enter your option:'))
    selectedOption(option)

# Menu options
def selectedOption(value):
    if value == '1':
        loadFile()
        return "Option [1] Read and load maze from file"
    elif value == '2': 
        viewMaze() 
        return "Option [2] View Maze"
    elif value == '3':
        playMaze()
        return "Option [3] Play maze game"
    elif value == '4':
        configurationMenu()
        return "Option [4] Configure current maze"
    elif value == '':
        mainMenu()
    elif value == '0':
        print("Exit")
        return "Exit"
        sys.exit()
    else:
        print('Invalid option. Please try again.')
        return 'Invalid option. Please try again.'

# Option 1 (Load Maze File)
def loadFile():
    print('Option [1] Read and load maze from file')
    name=str(input('Enter the name of the data file:'))
    checkFile(name)

# Option 2 (View Maze)
def viewMaze():
    print('Option [2] View Maze')

# Option 3 (Play Maze)
def playMaze():
    print('Option [3] Play maze game')

# Option 4 (Configure Maze)
def configureMaze():
    print('Option [4] Configure current maze')
    configurationMenu()

# Load maze .csv file
def checkFile(file):
    print(file)
    # return "Read and load maze"

mainMenu()