menu=(' \nMAIN MENU \n==========\
\n[1]  Read and load maze from file \n[2]  \
View maze \n[3]  Play maze game \
 \n[4]  Configure current maze \n \n[0]  Exit Maze\n')


def mainMenu():
    #create a function for main menu to allow for repetition 
    print(menu)
    option=input('Enter your option:')
    print()

    if option=='1':
        print('Option 1: Read and load maze from file')
        print()
        input('')
        mainMenu()
        
    elif option=='2':
        print('Option 2: View maze')       
        input('')
        mainMenu()

    elif option=='3':
        print('Option 3:Play maze game')
        input('')
        mainMenu()

    elif option=='4':
        print('Option 4: Configure current maze')
        input('')
        mainMenu()
        
    elif option=='0':
        print('Bye!')

    else:
        print('Invalid option.')
        input('')
        mainMenu()
        
mainMenu()

        
    
    

