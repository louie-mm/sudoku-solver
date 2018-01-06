import logging
from src.algorithm.algorithm import DepthFirstSearch

from src.board.board import Board

# TODO: Move this to cmd input
logging.basicConfig(level=logging.DEBUG)

board = [[0, 6, 0, 3, 0, 0, 8, 0, 4],
         [5, 3, 7, 0, 9, 0, 0, 0, 0],
         [0, 4, 0, 0, 0, 6, 3, 0, 7],
         [0, 9, 0, 0, 5, 1, 2, 3, 8],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [7, 1, 3, 6, 2, 0, 0, 4, 0],
         [3, 0, 6, 4, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 6, 0, 5, 2, 3],
         [1, 0, 2, 0, 0, 9, 0, 8, 0]]
sudoku = Board(board)


sudoku.print()
print('\n\n')
dfs = DepthFirstSearch(sudoku)
solved_board = dfs.search()
solved_board.print()
