import math
import random
import time

def make_board(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def reccursive_sudoku_solver(board, n):
    """
        recursive function that starts from the top row and fills the rows left to right with possible values
        this function will print the board if a solution is found
        This function essensially looks at all possible states and will back-track if it enters an invalid state
    """
    for j in range(n): 
        for i in range(n):
            if board[j][i] == 0:
                possible_num = return_available_num(board, i, j) #get curerently available values
                if possible_num != []: # if there are available numbers
                    for num in possible_num: # try filling in the number into the slot
                        board[j][i] = num
                        reccursive_sudoku_solver(board, n) # go to the next state
                        board[j][i] = 0 # if the recursive function "returns", a solution was not found so back-track
                return
    # exit condition of the recursive sudoku is if all entries are filled
    print_board(board)

def heuristic_sudoku_solver(board, n):
    for y in range(n):
        for x in range(n):
            if board[y][x] == 0:
                num_list = return_available_num(board, x, y)
                if len(num_list) == 1:
                    board[y][x] = num_list[0]
    reccursive_sudoku_solver(board, n)
    
def Knuth_DLX_solver():
    """
    

    """

def print_board(board):
    for row in board: print(row)
    print("*" * 20)

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

def xy_to_index(x, y, n):
    return y*n + x

def index_to_xy(index, n):
    return (index%n, index//n)

def num_in_rows(board, row_number):
    return list({board[row_number][i] for i in range(len(board))} - set([0]))

def num_in_column(board, column_number):
    return list({board[i][column_number] for i in range(len(board))} - set([0]))

def create_sudoku_board(n, ran = False):
    """
    returns the sudoku board of size x by y, and this will only work if the sizes are legit sudoku board size
    the "ran" variable stands for random and indicates if it should return a randomized board or the default board
    """
    root_n = int(math.sqrt(n))
    if (ran == True) and (root_n**2 == n): # make a random board
        board = make_board(n) # fill board with all zero 
        for block_row_index in range(root_n):
            num_list = list(range(1,n+1))
            if block_row_index == 0:
                random.shuffle(num_list) #shuffles 1~9
                for i in range(root_n):
                    for j in range(root_n):
                        board[j][i] = num_list[j*root_n+i]
            else:
                available_num = set(range(1,n+1))
                for y_val in range(root_n):
                    if y_val != root_n-2:
                        row_num = set(num_in_rows(board, y_val))
                        used_nums = random.sample(available_num - row_num, 3)
                        print(used_nums)
                        for ind_val, num_val in enumerate(used_nums):
                            board[y_val][block_row_index*root_n + ind_val] = num_val
                        available_num = available_num-row_num
                    else:
                        
                        last_row = set(num_in_rows(board, y_val+1))
                        values_for_row = set(available_num.intersection(last_row))
                        print(values_for_row)
                        available_num = available_num - values_for_row
                        print("set", available_num)
                        if len(values_for_row) != root_n:
                            x = root_n - len(values_for_row)
                            print("x is", x)
                            values_for_row.union(set(random.sample(available_num, x)))
                        for ind_val, num_val in enumerate(values_for_row):
                                board[y_val][block_row_index*root_n+ind_val] = num_val
                        
                        
                
            print_board(board)


    else: # use a defined board, a "hard" sudoku board from the internet
        board = [[0, 0, 0, 7, 0, 9, 0, 0, 0],
                [5, 7, 0, 0, 0, 0, 6, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 3],
                [4, 0, 0, 9, 3, 0, 0, 2, 8],
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [7, 3, 0, 0, 4, 2, 0, 0, 5],
                [2, 0, 0, 0, 0, 0, 0, 5, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 9], 
                [0, 0, 0, 4, 0, 3, 0, 0, 0]]
    return board

def main():
    if True:
        board = create_sudoku_board(9, ran = True)
        #reccursive_sudoku_solver(board, 9)
        #heuristic_sudoku_solver(board, 9)

if __name__ == "__main__":
    main()    