menu=(' \nMAIN MENU \n=========\
\n[1]  Read and load maze from file \n[2]  \
View maze \n[3]  Play maze game \
 \n[4]  Configure current maze \n \n[0]  Exit Maze\n')

configMenu=(' \nCONFIGURATION MENU \n=================\
\n[1]  Create wall \n[2]  \
Create passageway \n[3]  Create start point \
 \n[4]  Create end point \n \n[0]  Exit to Main Menu\n')

def configurationMenu():
    print(configMenu)
    print()
    option=input('Enter your option:')
    print()
    if option =='0':
        input('')
    mainMenu()
def mainMenu():
    #create a function for main menu to allow for repetition 
    print(menu)
    option=input('Enter your option:')
    print()

    if option=='1':
        print('Option 1: Read and load maze from file')
        print()
        name=str(input('Enter the name of the data file:'))
        input('')
        print('Number of lines read:')
        mainMenu()
        
    elif option=='2':
        print('Option 2: View Maze')       
        input('')
        mainMenu()

    elif option=='3':
        print('Option 3:Play maze game')
        input('')
        mainMenu()

    elif option=='4':
        print('Option 4: Configure current maze')
        configurationMenu()

        
    elif option=='0':
        print('Bye!')

    else:
        print('Invalid option.')
        input('')
        mainMenu()
        
mainMenu()

        
    
    

