"""
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.
The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)
"""

from algorithms.matrix.sudoku_validator import valid_solution_hashtable,valid_solution


a=[[5, 3, 4, 6, 7, 8, 9, 1, 2],
   [6, 7, 2, 1, 9, 5, 3, 4, 8],
   [1, 9, 8, 3, 4, 2, 5, 6, 7],
   [8, 5, 9, 7, 6, 1, 4, 2, 3],
   [4, 2, 6, 8, 5, 3, 7, 9, 1],
   [7, 1, 3, 9, 2, 4, 8, 5, 6],
   [9, 6, 1, 5, 3, 7, 2, 8, 4],
   [2, 8, 7, 4, 1, 9, 6, 3, 5],
   [3, 4, 5, 2, 8, 6, 1, 7, 9]]

b=[[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 0, 3, 4, 9],
[1, 0, 0, 3, 4, 2, 5, 6, 0],
[8, 5, 9, 7, 6, 1, 0, 2, 0],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 0, 1, 5, 3, 7, 2, 1, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 0, 0, 4, 8, 1, 1, 7, 9]]

print(valid_solution(a))


print(valid_solution(b))