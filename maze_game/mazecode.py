import sys
import time
import csv
# Variable to store maze.csv
mazeList = []
x=True

menu=(' \nMAIN MENU \n=========\
\n[1]  Read and load maze from file \n[2]  \
View maze \n[3]  Play maze game \
 \n[4]  Configure current maze \n \n[0]  Exit Maze\n')

configMenu=(' \nCONFIGURATION MENU \n==================\
\n[1]  Create wall \n[2]  \
Create passageway \n[3]  Create start point \
 \n[4]  Create end point \n \n[0]  Exit to Main Menu\n')

#Display the main menu
def mainMenu():
    print(menu)

# Display the configuration menu
def displayConfigurationMenu():
    print(configMenu)

def emptyMaze(mazeList):
    return len(mazeList) == 0

def loadFile(name):
    try :
        f = open(name)
        csv_reader = csv.reader(f,delimiter=',')
        lines = 0
        for row in csv_reader:
            mazeList.append(row)
            lines += 1
        records=("Number of lines read: " + str(lines))
        print(records)
        return records
    except IOError:
        print("Invalid data file.")
        return "Invalid data file."

def checkFile(maze):
    if not emptyMaze(maze):
        return "Maze loaded."
    else:
        print("No maze loaded.")
        return "No maze loaded."

def selectedOption(option, var=''):
    if option == "1":
        if var=="skip":
            return "Option [1] Read and load maze from file"
        print('Option [1] Read and load maze from file\n')
        file = input("Enter the name of the data file: ")
        mazeList.clear()
        loadFile(file)

    elif option == "2":
        if var =="skip":
            return "Option [2] View Maze"
        print("Option [2] View Maze\n")
        status = checkFile(mazeList)
        if status == "Maze loaded.":
            for row in mazeList:
                print(row)        
    
    elif option == "3":
        if var== "skip":
            return "Option [3] Play maze game"
        print("Option [3] Play maze game\n")
        status = checkFile(mazeList)
        if status == "Maze loaded.":
            for row in mazeList:
                print(row)                 
    
    elif option == "4":
        if var =="skip":
            return "Option [4] Configure current maze"
        print('Option [4] Configure current maze\n')
        status = checkFile(mazeList)
        if status == "Maze loaded.":
            for row in mazeList:
                print(row)   
        displayConfigurationMenu()
        config_option = input("Enter your option: ")   

    elif option == "0":
        print("Exit")
        return False
    else:
        print ("Invalid option. Please try again.")
        return "Invalid option. Please try again."
    
if __name__ == "__main__":
    while x != False:
        mainMenu()
        x = selectedOption(input("Enter your option: "))
