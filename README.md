# Sudoku_solver
 Just solving a sudoku board using python

 I used recursion to solve sudoku, later found out that its called back-tracking.

### Updates & future plans:
- I plan to implement a dancing link version of this solver.  Donald Knuth's algorithm for solving sudoku using exact cover is very intresting and I plan to update this program once I finish the exact cover chapter of Knuth's TAoCP book 5.

## Table of Contents:
- [Sudoku Generator](#generator)
    - [Visual of the Generator](#visual)
- [Output of the Code](#output)

I didn't use this method, but there are algorithms that makes a filled sudoku in a fast and reliable way, 
notably the method listed below:
- 1.) Generate a permuted list of 1-9 and placing them on the first row
- 2.) shift the first row by three and place it on the second row
- 3.) shift the second row by three and place it on the third row 
- 4.) shift by 1 for the 4th row, then shift by 3 for 5th and 6th row
- 5.) do step 4 with 7th, 8th, and 9th row
- 6.) using some rules, permute the block row and or column

<a id = "generator"></a>  
## My sudoku generator
I didn't use this method because the number of possible sudoku board is limited, although the number of possible output state is large. I wanted to make a pure random sudoku generator that can output all possible states with unique solutions with non-zero probability, so I made a generator using the recursive solver to generate a complete board.
My method of generating a sudoku board is to fill the top 3 blocks with valid random values, then transpose the matrix and fill the "new" top row with valid random values. then you have a block of rows and a column of rows that are somewhat independent of eachother, then use the recursive solver to fill in the rest.  The recursive solver chooses randomly from the possible numbers that can be entered in that cell, so the randomness of the output is not damaged.


<a id = "visual"></a> 
## Visual interpertation of what my algorithm is doing:
| 1.) fill the top 3 blocks |2.) transpose the matrix | 3.) & 4.) fill the top three board and transpose it back|
|---------------------------|---------------------------|---------------------------|
| ![board1](Figure_1.png)   |   ![board2](Figure_2.png) |   ![board3](Figure_3.png) |

After the recursive solver makes a filled randomized sudoku board, start making batches of random positions and check the uniqueness of the solution if they're removed.  if the uniqueness is preserved, remove the values in those positions, if there's a divergence in the number of solutions, then use a new random batch and start over.  Exit the removing stage if enough entries are removed.  By checking if the number of solutions, we can observe which cell values are vital to perserving the uniqueness of the solution.


<a id = "output"></a> 
## Outputs:
|Random empty board state:|Solved board state: |
|--------------------------|-----------------------|
|![empty_state](Figure_4.png) | ![solved_state](Figure_5.png)|