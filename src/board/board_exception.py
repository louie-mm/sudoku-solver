from enum import Enum


class BoardException(Exception):

    def __init__(self, error_arguments, reason):
        super(BoardException, self).__init__("Sudoku Exception raised: " + str(error_arguments))
        self.reason = reason


class Parameter(Enum):
    ROW = 1
    COL = 2
    INVALID_BOARD = 3
