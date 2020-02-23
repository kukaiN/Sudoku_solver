import math
import random
import matplotlib.pyplot as plt
import numpy as np

def make_board(n):
    """Makes a n x n board that is filled with zeros"""
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
        if sol_num < limit: # counts if the board have multiple answers, i.e. is it unique?
            if sol_num < 1:
                solved_board = copy_board(board, n)
                if print_bool: print_board(solved_board)
            sol_num+=1
        else: find = False

def heuristic_sudoku_solver(board, n, root_n):
    """
    tries to fill some values that definitly fits in that position
    then goes into the recursive sudoku solver.
    """
    for _ in range(3): 
        for y in range(n):
            for x in range(n):
                if board[y][x] == 0:
                    num_list = return_available_num(board, x, y, n, root_n)
                    if len(num_list) == 1: # if the value that goes in this position is unique
                        board[y][x] = num_list[0]
    reccursive_sudoku_solver(board, n, root_n)
    
def Knuth_DLX_solver():
    """
    not implimented yet, working on it
    """
    pass

def print_board(board):
    """ prints the sudoku board in the terminal and is visualized nicely """
    for row in board: print(row)
    print("*" * 20)

def board_to_image(board, n):
    """
    uses numpy and matplotlib to output a board state.  This uses a colormap underneath,
    it's just that im using 0s to make the underlying grid shape and the 0s are mapped to the color white
    then the values of the sudoku are placed in their right position and the plot is outputted
    """
    temp_board = np.array(board)
    fig, ax = plt.subplots()

    # The colormap doesn't go away and there's no "white" colormap, 
    # so Im using an 2d array filled with zeros and the zeros are being mapped to the color white.
    ax.imshow(np.zeros((n,n)), cmap="Greys")

    # The ticks are shifted by 0.5 so that when the grid is placed, it's not on top of the numbers
    ax.set_xticks(np.arange(0.5, n, 1))
    ax.set_yticks(np.arange(0.5, n, 1))

    # The tick_param is there to remove the labels and the tick marks 
    ax.tick_params(axis = "both", which="both",left=False, bottom=False, labelbottom=False, labelleft=False)
    
    for y in range(n): # placing the values on the plot in a grid shape
        for x in range(n):
            val = " " if  temp_board[y][x] == 0 else temp_board[y][x]
            ax.text(y, x,val, ha="center", va="center", color="k")
    fig.tight_layout()
    plt.grid(True)
    plt.show()

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

def num_in_row(board, row_number):
    """ returns a list of values that are on the same row"""
    return list({board[row_number][i] for i in range(len(board))} - set([0]))

def num_in_column(board, column_number):
    """ returns a list of values that are on the same column"""
    return list({board[i][column_number] for i in range(len(board))} - set([0]))

def fill_block(board, block_row, block_column, root_n, sequence):
    """
    given the coordinates of the sub-block of a sudoku board, it will try to fill that board with valid numbers
    only used to fill the top left corner block
    """
    if (block_column < root_n) and (block_row < root_n) and (len(sequence) == root_n**2):
        for j in range(root_n):
            for i in range(root_n):
                board[block_row*root_n + j][block_column*root_n + i] = sequence[j*root_n + i]
        return board
    else: print("error filling block")

def checker(brd, rt_n): 
    """ 
    check the top blocks of the sudoku board for inconsistencies
    not used in anyother parts of the code, was used for debugging purposes
    """
    num_set = set(range(1,rt_n**2+1)) # set of numbers
    for i in range(rt_n): # check row, no need to check column
        if len(num_set - set(num_in_row(brd, i))) != 0: print('something wrong with row', i)
        else: print("row",i, "is ok")
    for i in range(rt_n): # check block
        temp_set = {brd[y][i*rt_n+x] for y in range(rt_n) for x in range(rt_n)}
        if len(num_set - temp_set) != 0: print("block number",i , "is WRONG******")
        else: print("block", i, "is ok")

def fill_top_block(board, root_n, n):
    """ fills the top blocks of the sudoku board with valid random values"""
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
            available_num-=set(used_nums) # update the leftover numbers 
    return board

def transpose_matrix(board, n):
    """ self-explanitory, does a list comprehension to tanspose the matrix"""
    return [[board[x][y] for x in range(n)] for y in range(n)]

def copy_board(board, n):
    """ self-explanitory, does a list comprehension to copy board"""
    return [[board[j][i] for i in range(n)] for j in range(n)]

def make_unique_solution_board(board, n, root_n, difficulty):
    """
    This function will take a solved sudoku board and remove random positions and will perserve the uniqueness of a solution
    The uniqueness of a solution is conserved by the following:
    1.) remove a small batch of numbers from the grid
    2.) use the recursive sudoku solver to check if the solution is unique
    3.) a.) If theres only one solutions, the removed values doesnt change the solution, so they can be removed.
        b.) If there's more than one solution, the one or more of the values we took out was critical to the uniqueness, 
            so put back the values and restart from one 
        keep doing this process until a desired amount of numbers is removed
    """
    global find, limit, sol_num
    # initializing variables
    available_set = set(range(n**2)) 
    counter, leftover_numbers, loop_counter = math.floor((n**2)*0.15), n**2, math.floor((n**2)*0.25)
    print("finish making a random board if the board have", 17 + 4*difficulty, "or less filled cells, or one step before solutions diverges from unique solution")
    while leftover_numbers > 4*difficulty + 17: #17 is the minimal number currently known for a 9x9 board, so it can be replaced for other sized sudoku boards
        if loop_counter < 0: break # breaks from the loop if the procedure lingers
        else: loop_counter-=1
        fake_board = copy_board(board, n)   
        if counter < len(available_set):
            maybe_remove = random.sample(available_set, counter) # the batch of positions to be removed from the board
            for index in maybe_remove: # remove values stored in these positions
                fake_board[index//n][index%n] = 0
            sol_num, limit, find = 0, 3, True
            reccursive_sudoku_solver(fake_board, n, root_n) #solves the board
            if sol_num == 1: # if solutions is unique, then update the board 
                board = copy_board(fake_board, n)
            if sol_num == 1 or counter == 1: # modify the set that stores the positions that we can remove
                leftover_numbers-=counter
                available_set-=set(maybe_remove)
        if counter > 1: counter -=1
    print_board(board)
    print(sum(1 if board[y][x] != 0 else 0 for x in range(n) for y in range(n)), "out of", n**2, "is filled with values.")
    return board

def create_sudoku_board(root_n, n, difficulty, ran = False):
    """
    returns the sudoku board of size x by y, and this will only work if the sizes are legit sudoku board size
    the "ran" variable stands for random and indicates if it should return a randomized board or the default board
    """
    if (ran == True) and n > 1: # make a random board
        board = make_board(n) # fill board with all zero 
        fill_block(board, 0, 0 , root_n, random.sample(list(range(1,n+1)), n))#shuffles 1~n and fill the top-left block
        board = transpose_matrix(fill_top_block(board, root_n, n), n)
        board = transpose_matrix(fill_top_block(board, root_n, n), n)
        global solved_board, find, limit, sol_num, print_bool
        find, sol_num, limit, print_bool = True, 0, 1, False
        reccursive_sudoku_solver(board, n, root_n) # fill rest of the entries with valid random values
        board = make_unique_solution_board(solved_board, n, root_n, difficulty)
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
    global find, sol_num, limit, solved_board, print_bool
    solved_board = None
    root_n = 3
    # making a filled sudoku board and removing values to get a empty board to be solved
    board = create_sudoku_board(root_n, root_n**2, random.randint(1,6), ran = True)
    board_to_image(board, root_n**2) # show the empty sudoku board
    # modifying global variables, because we're now in the solving stage
    find, sol_num, limit, solved_board, print_bool = True, 0, 100, None, True
    reccursive_sudoku_solver(board, root_n**2, root_n)
    #heuristic_sudoku_solver(board, 9, root_n)

if __name__ == "__main__":
    main()    

    