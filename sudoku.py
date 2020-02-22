import math
import random
import time

def make_board(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def reccursive_sudoku_solver(board, n, root_n):
    """
        recursive function that starts from the top row and fills the rows left to right with possible values
        this function will print the board if a solution is found
        This function essensially looks at all possible states and will back-track if it enters an invalid state
    """
    global find
    if find:
        for j in range(n): 
            for i in range(n):
                if board[j][i] == 0:
                    possible_num = return_available_num(board, i, j, n, root_n) #get curerently available values
                    if possible_num != []: # if there are available numbers
                        random.shuffle(possible_num)
                        for num in possible_num: # try filling in the number into the slot
                            board[j][i] = num
                            reccursive_sudoku_solver(board, n, root_n) # go to the next state
                            board[j][i] = 0 # if the recursive function "returns", a solution was not found so back-track
                    return
        # exit condition of the recursive sudoku is if all entries are filled
        global sol_num, limit, solved_board, print_bool
        if sol_num < limit:
            sol_num+=1
            if print_bool and sol_num < 1: 
                solved_board = board
                print_board(board)
        else: find = False

def heuristic_sudoku_solver(board, n, root_n):
    for y in range(n):
        for x in range(n):
            if board[y][x] == 0:
                num_list = return_available_num(board, x, y, n, root_n)
                if len(num_list) == 1:
                    board[y][x] = num_list[0]
    reccursive_sudoku_solver(board, n, root_n)
    
def Knuth_DLX_solver():
    """
    

    """

def print_board(board):
    for row in board: print(row)
    print("*" * 20)

def return_available_num(board, x, y, n, root_n):
    """
    makes a list of the values already taken by the column, row and box on the sudoku board
    then using sets, returns the values that can be placed in the (x, y) position
    """
    possible_solutions, found_num = [], []
    if x < n and y < n and board[y][x] == 0:
        found_num+=[board[y][i] for i in range(n)] # horizontal components
        found_num+=[board[i][x] for i in range(n)] # vertical components
        # the value (x, y) is stored twice, but is zero, so it's ok
        block_x, block_y = math.floor(x/root_n), math.floor(y/root_n) # number of the sub-block which x,y is located
        found_num+= [board[root_n*block_y+l][root_n*block_x+k] for k in range(root_n) for l in range(root_n)]
        possible_solutions = list(set(range(1, int(n)+1))-set(found_num))
    return possible_solutions

def xy_to_index(x, y, n):
    return y*n + x

def index_to_xy(index, n):
    return (index%n, index//n)

def num_in_row(board, row_number):
    return list({board[row_number][i] for i in range(len(board))} - set([0]))

def num_in_column(board, column_number):
    return list({board[i][column_number] for i in range(len(board))} - set([0]))

def fill_block(board, block_row, block_column, root_n, sequence):
    if (block_column < root_n) and (block_row < root_n) and (len(sequence) == root_n**2):
        for j in range(root_n):
            for i in range(root_n):
                board[block_row*root_n + j][block_column*root_n + i] = sequence[j*root_n + i]
        return board
    else: print("error filling block")

def checker(brd, rt_n): # check top blocks for inconsistencies
    num_set = set(range(1,rt_n**2+1)) # set of numbers
    for i in range(rt_n):
        if len(num_set - set(num_in_row(brd, i))) != 0: print('something wrong with row', i)
        else: print("row",i, "is ok")
    for i in range(rt_n):
        temp_set = {brd[y][i*rt_n+x] for y in range(rt_n) for x in range(rt_n)}
        if len(num_set - temp_set) != 0: print("block number",i , "is WRONG******")
        else: print("block", i, "is ok")

def fill_top_block(board, root_n, n):
    for block_index in range(1, root_n): # iterate over each block
        available_num = set(range(1,n+1))
        for y_val in range(root_n): #looping through the y values of the block
            row_candidate = available_num-set(num_in_row(board, y_val))
            if y_val == root_n-2: #use up all numbers in the next row
                taken_num = set(num_in_row(board, y_val+1)).intersection(row_candidate) #numbers definitly used for this row    
                used_nums, missing_num = list(taken_num), root_n - len(taken_num)
                used_nums+=list(random.sample((row_candidate)-taken_num, missing_num)) if missing_num != 0 else [] # fill up rows
                row_candidate = used_nums
            used_nums = random.sample(row_candidate, root_n) #scramble numbers to be used for this row
            for ind_val, num_val in enumerate(used_nums): 
                board[y_val][block_index*root_n + ind_val] = num_val #update board values
            available_num = available_num-set(used_nums) # update the leftover numbers 
    return board

def transpose_matrix(board, n):
    return [[board[x][y] for x in range(n)] for y in range(n)]

def make_unique_solution_board(board, n, root_n, difficulty):
    global find, stop, limit, sol_num
    limit = 3
    non_removable_points = {}
    removable_points = set(range(n**2))
    while len(removable_points) > 2*difficulty:
        fake_board = [[board[y][x]] for x in range(n) for y in range(n)] #copy of the board
        counter = 10
        if counter > len(removable_points):
            temp_list = random.sample(removable_points, 10)
            for index in temp_list:
                i, j = index_to_xy(index, n)
                fake_board[j][i] = 0
            find, sol_num = True, 0
            reccursive_sudoku_solver(fake_board, n, root_n)
            if sol_num != 1:
                
            else:
                removable_points = removable_points - set(temp_list)
                board = fake_board
            
            
            if counter > 1:
                counter-=1
        else:
            counter = 1

    return board

def create_sudoku_board(n, ran = False, difficulty):
    """
    returns the sudoku board of size x by y, and this will only work if the sizes are legit sudoku board size
    the "ran" variable stands for random and indicates if it should return a randomized board or the default board
    """
    root_n = int(math.sqrt(n))
    if (ran == True) and (root_n**2 == n) and n > 1: # make a random board
        board = make_board(n) # fill board with all zero 
        fill_block(board, 0, 0 , root_n, random.sample(list(range(1,n+1)), n))#shuffles 1~n and fill the top-left block
        board = transpose_matrix(fill_top_block(board, root_n, n), n)
        board = transpose_matrix(fill_top_block(board, root_n, n), n)
        print_board(board)
        global solved_board, find, limit, sol_num
        find, sol_num, limit = True, 0, 1
        reccursive_sudoku_solver(board, n, root_n) 
        board = make_unique_solution_board(solved_board, root_n, n, difficulty)
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
        global find, sol_num, limit solved_board, print_bool
        print_bool = False
        root_n = 3
        difficulty = [1, 2, 3, 4, 5] # 1 is easy,  5 is hard
        board = create_sudoku_board(root_n**2, ran = True, difficulty[0])
        find, sol_num, limit, solved_board, print_bool = True, 0, 100, None, True
        reccursive_sudoku_solver(board, root_n**2, root_n)
        print("found over ", sol_num)
        #heuristic_sudoku_solver(board, 9, root_n)

if __name__ == "__main__":
    main()    