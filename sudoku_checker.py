
def num_in_row(board, row_number, col):
    """ returns a list of values that are on the same row"""
    return list({board[row_number][i] for i in range(len(board)) if col != i } - set([0]))

def num_in_column(board, column_number, row):
    """ returns a list of values that are on the same column"""
    return list({board[i][column_number] for i in range(len(board)) if row != i} - set([0]))


def main():
    # the board to be checked
    board = [[8, 9, 3, 5, 1, 2, 6, 7, 4],
            [4, 1, 7, 6, 3, 8, 2, 9, 5],
            [2, 5, 6, 4, 7, 9, 3, 8, 1],
            [5, 6, 2, 7, 8, 3, 1, 4, 9],
            [1, 7, 4, 9, 5, 6, 8, 3, 2],
            [9, 3, 8, 1, 2, 4, 5, 6, 7],
            [7, 8, 9, 2, 6, 5, 4, 1, 3],
            [6, 4, 5, 3, 9, 1, 7, 2, 8],
            [3, 2, 1, 8, 4, 7, 9, 5, 6] ]
    n = 9
    root_n = 3
    # checks if there's inconsistencies in the horizonatal and vertical components
    for j in range(n):
        for i in range(n):
            current_num = board[j][i]
            x = num_in_column(board, i, j)
            y = num_in_row(board, j, i)
            if current_num in x or current_num in y:
                print("False")

    # check if there's inconsistencies in the boxes of the sudoku board
    for j in range(n): # iterating through the points
        for i in range(n):
            box_x, box_y = int(i/root_n)*root_n, int(j/root_n)*root_n
            for ni in range(root_n): # iterating through the box
                for nj in range(root_n): 
                    coor_x, coor_y = box_x+ni, box_y+nj
                    if coor_x != i or coor_y != j:
                        if board[j][i] == board[coor_y][coor_x]:
                            print("box false,", i, j, coor_x, coor_y)

if __name__ == "__main__":
    main()
