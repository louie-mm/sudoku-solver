from math import floor

import numpy as np

from src.board import utils as utils
from src.element.element import Element


class Board:

    def __init__(self, two_dimensional_array=None):
        # TODO: checks to determine if the input array is valid
        if two_dimensional_array is None:
            two_dimensional_array = [[0 for row in range(9)] for col in range(9)]
        for row in range(9):
            for col in range(9):
                value = two_dimensional_array[row][col]
                two_dimensional_array[row][col] = Element(value)

        self.board = np.array(two_dimensional_array)

    def element(self, row, col):
        utils.validate_row(row)
        utils.validate_col(col)
        return self.board[row - 1, col - 1]

    def row(self, row):
        utils.validate_row(row)
        row_elements = self.board[row - 1, :]
        return [e.value for e in row_elements]

    def col(self, col):
        utils.validate_col(col)
        col_elements = self.board[:, col - 1]
        return [e.value for e in col_elements]

    def ninth(self, row, col):
        utils.validate_ninth(row, col)
        # TODO: Extract to Utils
        ninth_elements = self.board[(3 * row - 3):(3 * row), (3 * col - 3):(3 * col)]
        return [[e.value for e in row] for row in ninth_elements]

    def ninth_by_element(self, row, col):
        utils.validate_row(row)
        utils.validate_col(col)
        # TODO: Extract to Utils
        ninth_row = floor((row - 1)/3) + 1
        ninth_col = floor((col - 1)/3) + 1
        return self.ninth(ninth_row, ninth_col)

    def is_complete(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col].value is 0:
                    return False
        return True

    def print(self):
        solution_to_print = ''
        for row in range(9):
            for col in range(9):
                solution_to_print += str(self.board[row][col].value)
                if col % 3 is 2 and col is not 8:
                    solution_to_print += '|'
            solution_to_print += '\n'
            if row % 3 is 2 and row is not 8:
                solution_to_print += '---+---+---\n'
        print(solution_to_print)
