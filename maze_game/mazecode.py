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
def display_menu(check):
    if check == True:
        print(menu)
        return "Menu Displayed"

# Display the configuration menu
def displayConfigurationMenu():
    print(configMenu)
    return "Configuration Menu Displayed"

def isEmpty(mazeList):
    return len(mazeList) == 0

def loadFile(filename):
    try :
        f = open(filename)
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
    if not isEmpty(maze):
        loaded = "Maze loaded."
        return (loaded)
    else:
        loaded = "No maze loaded."
        print (loaded)
        return (loaded)

def selectedConfigOption(option):
    if option == "1":
        return "Configuration Option 1 is selected"

    elif option == "2":
        return "Configuration Option 2 is selected"
        
    elif option == "3":
        return "Configuration Option 3 is selected"

    elif option == "4":
        return "Configuration Option 4 is selected"
        
    elif option == "0":
        return False
    else:
        print ("Invalid option")
        return "Invalid Configuration Option"

def selectedOption(option, var=''):
    if option == "1":
        if var=="skip":
            return "Option [1] Read and load maze from file"
        print('Option [1] Read and load maze from file\n')
        mazeList.clear()
        file = input("Enter the name of the data file: ")
        loadFile(file)
        return "Option [1] Read and load maze from file"

    elif option == "2":
        if var =="skip":
            return "Option [2] View Maze"
        print("Option [2] View Maze\n")
        status = checkFile(mazeList)
        if status == "Maze loaded.":
            for row in mazeList:
                print(row)        
        return "Option [2] View Maze"
    
    elif option == "3":
        if var== "skip":
            return "Option [3] Play maze game"
        print("Option [3] Play maze game\n")
        status = checkFile(mazeList)
        if status == "Maze loaded.":
            for row in mazeList:
                print(row)                         
        return "Option [3] Play maze game"
    
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
    
        return "Option [4] Configure current maze"

    elif option == "0":
        print("Exit")
        return False
    else:
        print ("Invalid option. Please try again.")
        return "Invalid option. Please try again."
    
if __name__ == "__main__":
    while x != False:
        display_menu(True)
        x = selectedOption(input ("Enter your option: "))
