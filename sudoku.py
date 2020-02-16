import math
import random

def main():
    if True:#input("make a new board?") == "yes":
        board = create_sudoku__board(9,9)

def solve_sudoku():
    if 

def print_board(board, x, y):
    """"function that prints the sudoku board neatly"""
    for i in range(y):
        print(board[i])

def return_available_num(board, x, y):
    """
    makes a list of the values already taken by the column, row and box on the sudoku board
    then using sets, returns the values that can be placed in the (x, y) position
    """
    possible_solutions = []
    xy_range = len(board) # size of board
    if x < xy_range and y < xy_range and board[y][x] == 0:
        found_num, possible_num = [], set(range(1, int(xy_range)+1))
        for i in range(xy_range):# look at the horizontal and vertical component of the board
            found_num.append(board[y][i])# the value in (x, y) is stored twice but the value is zero so it's ok
            found_num.append(board[i][x])
        block_size = int(math.sqrt(xy_range))# size of the sub-block
        block_x, block_y = math.floor(x/block_size), math.floor(y/block_size) # number of the sub-block which x,y is located
        for k in range(block_size): # x values
            for l in range(block_size): # y values
                found_num.append(board[block_size*block_y+l][block_size*block_x+k])
        possible_solutions = list(set(possible_num)-set(found_num))
    return possible_solutions

def create_sudoku__board(x, y, ran = False):
    """
    returns the sudoku board of size x by y, and this will only work if the sizes are legit sudoku board size
    the "ran" variable stands for random and indicates if it should return a randomized board or the default board
    """
    if (ran == True) and (x == y) and (int(math.sqrt(x))**2 == x): # make a random board
        board = [[0 for _ in range(x)] for _ in range(y)] # fill board with all zero
        for i in range(x):
                for j in range(y):
                    if random.random() < 0.15: # enter a valid entry into a cell with 15%
                        possible_list = return_available_num(board, i, j)
                        if possible_list != []: #checks if we can place a random value in that cell
                            board[j][i] = random.choice(possible_list) 
    else:
        if ran:
            board = [[0 for _ in range(9)] for _ in range(9)]
            for i in range(9):
                for j in range(9):
                    if random.random() < 0.15: # enter a valid entry into a cell with 15%
                        possible_list = return_available_num(board, i, j)
                        if possible_list != []: #checks if we can place a random value in that cell
                            board[j][i] = random.choice(possible_list)
        else: # make the returned board the default board
            board = [[0, 0, 0, 0, 8, 0, 0, 2, 9],
                    [1, 2, 8, 0, 0, 0, 0, 0, 0],
                    [0, 5, 7, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [3, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    return board

if __name__ == "__main__":
    main()    