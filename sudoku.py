# import libraries here. Use the following ones only.
import time, sys, random

# add your implementation of the required functions here
def print_board(sudoku):
    for i in range(9):
        print(sudoku[i][0:3],'|',sudoku[i][3:6],'|',sudoku[i][6:9])
        if i==5 or i==2:
            print('-'*51)


# This function checks for any empty position in the sudoku (state of the game)
def check_for_empty_position(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == ' ':
                return (i, j)  # row, col

    return None

# This function checks if a given position in the sudoku is empty
def selected_position_is_empty(sudoku, row, col):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[row][col] == ' ':
                return True  # row, col

# This function checks if a chosen number is valid i.e satifies the 3 sudoku conditions 
def is_valid(sudoku, num, pos):
    # Checks if the chosen number is valid in the given row
    for i in range(len(sudoku[0])):
        if str(sudoku[pos[0]][i]) == str(num) and str(pos[1]) != str(i):
            return False

    # Checks if the chosen number is valid in the given column
    for i in range(len(sudoku)):
        if str(sudoku[i][pos[1]]) == str(num) and str(pos[0]) != str(i):
            return False


    # Checks if the chosen number is valid in the 3x3 grid or square
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if str(sudoku[i][j]) == str(num) and (str(i),str(j)) != str(pos):
                return False

    return True

            
if __name__ == '__main__':
    
    # Don't change the layout of the following two sudoku examples
    sudoku1 = [
        ['1', ' ', '6', ' ', '7', '8', ' ', '3', ' '],
        [' ', '5', '7', '3', '4', '9', ' ', '6', '2'],
        ['2', '9', '3', '6', ' ', '5', ' ', ' ', '7'],
        [' ', ' ', ' ', '9', ' ', '1', '6', ' ', '4'],
        ['4', '6', '1', ' ', ' ', ' ', '2', '8', '9'],
        ['5', '8', ' ', ' ', '6', '4', '3', ' ', ' '],
        ['7', '3', '4', '1', '9', '6', '5', ' ', '8'],
        ['6', '1', '8', '7', ' ', '2', '4', '9', '3'],
        [' ', ' ', ' ', ' ', '8', ' ', ' ', '1', ' '],
    ]
    sudoku2 = [
        ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '3', '6', ' ', ' ', ' ', ' ', ' '],
        [' ', '7', ' ', ' ', '9', ' ', '2', ' ', ' '],
        [' ', '5', ' ', ' ', ' ', '7', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '4', '5', '7', ' ', ' '],
        [' ', ' ', ' ', '1', ' ', ' ', ' ', '3', ' '],
        [' ', ' ', '1', ' ', ' ', ' ', ' ', '6', '8'],
        [' ', ' ', '8', '5', ' ', ' ', ' ', '1', ' '],
        [' ', '9', ' ', ' ', ' ', ' ', '4', ' ', ' '],
    ]

    
    option = 2

    if option == 1:
        sudoku = sudoku1
    elif option == 2:
        sudoku = sudoku2
    else:
        raise ValueError('Invalid choice!')

    # add code here to solve the sudoku
    #This function automatically solves the sudoku using back-tracking
    def computer_play(sudoku):
        find = check_for_empty_position(sudoku)
        if not find:
            return True
        else:
            row, col = find
        for i in range(1,10):
            if is_valid(sudoku, i, (row, col)):
                sudoku[row][col] = i
                if computer_play(sudoku):
                    return True
                sudoku[row][col] = ' '
        return False




    def human_play(sudoku):
        outcome = True
        move = 0
        print('Welcome to the Sudoku Game')
        print('   ')
        start = time.time()
        while outcome:
            print_board(sudoku)
            helper = input('Press h for a suggestion. Press Enter or any other key to continue: ')
            if helper == 'h':
                possible_numbers = []
                check_empty = check_for_empty_position(sudoku)# checks the state of the game
                if check_empty:
                    for i in range(1,10):
                        if is_valid(sudoku, i, check_empty):
                            possible_numbers.append(i)
                    suggestion = random.choice(possible_numbers)# suggests a posible value for a position
                print(suggestion, 'is a possible number in position ', check_empty)

            
            row_check = input("Enter a row number: ")
            col_check = input("Enter a col number: ")
            guess_check = input("Enter a valid number ")
            
            condition = False
            if row_check=='' or col_check=='' or guess_check=='':

                print('Please enter integer values only ')
            else:
                try:
                    row_val = int(row_check)
                    col_val = int(col_check)
                    guess = int(guess_check)
                    
                    check_position = selected_position_is_empty(sudoku, row_val, col_val)#checks if selected position is empty
                    
                    if check_position:
                        row, col = row_val, col_val
                        if is_valid(sudoku, guess, (row,col)):#checks if value inputed in selected position is valid
                            
                                sudoku[row][col] = guess #fills selected position with the inputed value
                                move+=1
                                state = sudoku
                               
                                check_empty = check_for_empty_position(sudoku) #checks state of the game for empty position
                                if check_empty:
                                    pass
                                else:
                                    #game successfully completed

                                    game_time = (time.time()-start)/60 #calculates game time in minutes
                                    print('Bravo !!! you did it ')
                                    print('Game Time: ', round(game_time, 2), 'minutes' )
                                    print('Correct Moves: ',move)
                                    restart = input('Do you want to restart the game ? y/n: ')#allows user to restart or end game
                                    if restart == 'y':
                                        #setting move to 0
                                        move=0
                                        #setting sudoku to initial state
                                        sudoku = [
                                                ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                [' ', ' ', '3', '6', ' ', ' ', ' ', ' ', ' '],
                                                [' ', '7', ' ', ' ', '9', ' ', '2', ' ', ' '],
                                                [' ', '5', ' ', ' ', ' ', '7', ' ', ' ', ' '],
                                                [' ', ' ', ' ', ' ', '4', '5', '7', ' ', ' '],
                                                [' ', ' ', ' ', '1', ' ', ' ', ' ', '3', ' '],
                                                [' ', ' ', '1', ' ', ' ', ' ', ' ', '6', '8'],
                                                [' ', ' ', '8', '5', ' ', ' ', ' ', '1', ' '],
                                                [' ', '9', ' ', ' ', ' ', ' ', '4', ' ', ' '],
                                                ]
                                    
                                        
                                    else:   
                                        condition = True
                                        sys.exit()
                

                        else:
                            end = time.time()
                            game_time = (end-start)/60#calculates game time in minutes
                            print('You entered an invalid number,  GAME OVER !!!')
                            print('Game Time: ', round(game_time, 2), 'minutes' )
                            print('Correct Moves: ',move)
                            try_again = input('Do you want to try again? y/n: ') #allow player to try again or end game
                            if try_again == 'y':
                                #setting move to 0
                                move = 0
                                #setting sudoku to initial state
                                sudoku = [
                                        ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                        [' ', ' ', '3', '6', ' ', ' ', ' ', ' ', ' '],
                                        [' ', '7', ' ', ' ', '9', ' ', '2', ' ', ' '],
                                        [' ', '5', ' ', ' ', ' ', '7', ' ', ' ', ' '],
                                        [' ', ' ', ' ', ' ', '4', '5', '7', ' ', ' '],
                                        [' ', ' ', ' ', '1', ' ', ' ', ' ', '3', ' '],
                                        [' ', ' ', '1', ' ', ' ', ' ', ' ', '6', '8'],
                                        [' ', ' ', '8', '5', ' ', ' ', ' ', '1', ' '],
                                        [' ', '9', ' ', ' ', ' ', ' ', '4', ' ', ' '],
                                        ]
                            else:
                                condition = True
                                sys.exit()
                                
                    else:
                        game_time = (time.time()-start)/60#calculates game time in minutes
                        print('Invalid position or position contains a value...GAME OVER ')#since move not withdrawable
                        print('Game Time: ', round(game_time, 2), 'minutes' )
                        print('Correct Moves: ',move)
                        try_again = input('Do you want to try again? y/n: ')#allow player to try again or end game
                        if try_again == 'y':
                            #setting move to 0
                            move = 0
                            #setting sudoku to initial state
                            sudoku = [
                                    ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', '3', '6', ' ', ' ', ' ', ' ', ' '],
                                    [' ', '7', ' ', ' ', '9', ' ', '2', ' ', ' '],
                                    [' ', '5', ' ', ' ', ' ', '7', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', '4', '5', '7', ' ', ' '],
                                    [' ', ' ', ' ', '1', ' ', ' ', ' ', '3', ' '],
                                    [' ', ' ', '1', ' ', ' ', ' ', ' ', '6', '8'],
                                    [' ', ' ', '8', '5', ' ', ' ', ' ', '1', ' '],
                                    [' ', '9', ' ', ' ', ' ', ' ', '4', ' ', ' '],
                                    ]
                        else:
                            condition = True
                            sys.exit()
                            
                        
                        
                        
                except:
                    if condition:
                        raise
                    
                        
                    print('Invalid input value entered Please enter integer values only ')

        human_play(sudoku)

    print_board(sudoku)#prints initial state of sudoku
    print('We are solving the sudoku Please wait....')
    computer_play(sudoku)#solves sudoku automatically 
    #human_play(sudoku)
    print_board(sudoku)#prints the solved sudoku




    
