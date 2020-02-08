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
        print("Option [2] View Maze\n\n========================================\n")
        status = checkFile(mazeList)
        if status == "Maze loaded.":
            for row in mazeList:
                print(row)        
    
    elif option == "3":
        if var== "skip":
            return "Option [3] Play maze game"
        print("Option [3] Play maze game\n")
        status = checkFile(mazeList)
        continu = True
        if status == "Maze loaded.":
            print("========================================\n")
            for row in mazeList:
                print(row)
            
        while continu != False:
            
        
            if status == "Maze loaded.":
                  
                
                                
                print ("\nPress 'W' for UP, 'A' for LEFT, 'S' for DOWN, 'D' for RIGHT, 'M' for MENU")
                choice = input("Select your Move: ")
                movement = playMaze(choice)
                continu = movement
            
            else:
                break
            
    
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
    



    
def playMaze(move):
    print("========================================")

    rowN = -1
    columnN = 0
    colStart = 0
    rowStart = 0
    colEnd = 0
    rowEnd = 0
        
    for item in mazeList:
        print(item)
        rowN += 1
        for value in item:
            if value == "A":
                colStart = columnN
                rowStart = rowN
            elif value == "B":
                colEnd = columnN
                rowEnd = rowN   
            columnN += 1
        columnN = 0

    print("\nLocation of Start (A) = (Row " + str(rowStart) + ", Column " + str(colStart) + ")")
    print("Location of End (B) = (Row " + str(rowEnd) + ", Column " + str(colEnd) + ")")

    

    if move == "W" or move == "w":
        upRow = rowStart - 1
        upCol = colStart
        if upRow > -1:
            upPos = mazeList[upRow][upCol]
            if upPos == "O":
                print("Move Successful!")
                return "Move Successful!"
                for item in mazeList:
                    mazeList[upRow][upCol] = "A"
                    mazeList[rowStart][colStart] = "O"
                    print(item)
                rowStart = upRow
                colStart = upCol
            elif upPos == "B":
                print("Congratulations! You have escaped from the maze!")
                print("Exiting to main menu")
                return False
                
            else:
                print("Invalid Movement. Please Try again")
                return"Invalid Movement. Please Try again"
        else:
            print("Invalid Movement. Please Try again")
            return"Invalid Movement. Please Try again"

    elif move == "A" or move == "a":
        leftRow = rowStart
        leftCol = colStart - 1
        if leftCol > -1:
            leftPos = mazeList[leftRow][leftCol]
            if leftPos == "O":
                print("Move Successful!")
                return "Move Successful!"
                for item in mazeList:
                    mazeList[leftRow][leftCol] = "A"
                    mazeList[rowStart][colStart] = "O"
                    print(item)
                rowStart = leftRow
                colStart = leftCol
            elif leftPos == "B":
                print("Congratulations! You have escaped from the maze!")
                print("Exiting to main menu")
                return False
                
            else:
                print("Invalid Movement. Please Try again")
                return"Invalid Movement. Please Try again"
        else:
            print("Invalid Movement. Please Try again")
            return"Invalid Movement. Please Try again"
                

    if move == "S" or move == "s":
        downRow = rowStart + 1
        downCol = colStart
        if rowStart < 8:
            downPos = mazeList[downRow][downCol]
            if downPos == "O":
                print("Move Successful!")
                return "Move Successful!"
                for item in mazeList:
                    mazeList[downRow][downCol] = "A"
                    mazeList[rowStart][colStart] = "O"
                    print(item)
                rowStart = downRow
                colStart = downCol
            elif downPos == "B":
                print("Congratulations! You have escaped from the maze!")
                print("Exiting to main menu")
                return False
                
            else:
                print("Invalid Movement. Please Try again")
                return"Invalid Movement. Please Try again"
        else:
            print("Invalid Movement. Please Try again")
            return"Invalid Movement. Please Try again"

    elif move == "D" or move == "d":
        rightRow = rowStart
        rightCol = colStart + 1
        if rightCol < 8:
            rightPos = mazeList[rightRow][rightCol]
            if rightPos == "O":
                print("Move Successful!")
                return "Move Successful!"
                for item in mazeList:
                    mazeList[rightRow][rightCol] = "A"
                    mazeList[rowStart][colStart] = "O"
                    print(item)
                rowStart = rightRow
                colStart = rightCol
            elif rightPos == "B":
                print("Congratulations! You have escaped from the maze!")
                print("Exiting to main menu")
                return False                
            else:
                print("Invalid Movement. Please Try again")
                return"Invalid Movement. Please Try again"
        else:
            print("Invalid Movement. Please Try again")
            return"Invalid Movement. Please Try again"
                
        
    elif move == "M" or move == "m":
        return False
        
    else:
        print("Invalid Movement. Please Try again")
        return"Invalid Movement. Please Try again"
        



    
if __name__ == "__main__":
    while x != False:
        mainMenu()
        x = selectedOption(input("Enter your option: "))
    
