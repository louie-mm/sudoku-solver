import unittest

import numpy as np
from numpy import testing as np_test

from src.board.board import Board
from src.board.board_exception import BoardException

# TODO: There must be a nicer way to set this up
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


class WhenSelectingElement(unittest.TestCase):

    def test_return_correct_element(self):
        self.assertEqual(sudoku.element(1, 2).value, 6)

    # TODO: Extract similar tests to a method to reduce repetition
    def test_throws_BoardException_when_out_of_bounds(self):
        with self.assertRaises(BoardException):
            sudoku.element(0, 4)
        with self.assertRaises(BoardException):
            sudoku.element(10, 4)
        with self.assertRaises(BoardException):
            sudoku.element(None, 4)
        with self.assertRaises(BoardException):
            sudoku.element(4, 0)
        with self.assertRaises(BoardException):
            sudoku.element(4, 10)
        with self.assertRaises(BoardException):
            sudoku.element(4, None)


class WhenSelectingRow(unittest.TestCase):
    expected = np.array([5, 3, 7, 0, 9, 0, 0, 0, 0])

    def test_returns_correct_row(self):
        actual = sudoku.row(2)
        np_test.assert_array_equal(actual, self.expected)

    def test_throws_BoardException_when_out_of_bounds(self):
        with self.assertRaises(BoardException):
            sudoku.row(0)
        with self.assertRaises(BoardException):
            sudoku.row(10)
        with self.assertRaises(BoardException):
            sudoku.row(None)


class WhenSelectingCol(unittest.TestCase):
    expected = np.array([0, 0, 0, 3, 0, 4, 1, 2, 8])

    def test_returns_correct_col(self):
        actual = sudoku.col(8)

        np_test.assert_array_equal(actual, self.expected)

    def test_throws_BoardException_when_out_of_bounds(self):
        with self.assertRaises(BoardException):
            sudoku.col(0)
        with self.assertRaises(BoardException):
            sudoku.col(10)
        with self.assertRaises(BoardException):
            sudoku.col(None)


class WhenSelectingNinth(unittest.TestCase):
    expected = np.array([[0, 9, 0], [0, 0, 0], [7, 1, 3]])

    def test_returns_correct_ninth(self):
        actual = sudoku.ninth(2, 1)

        np_test.assert_array_equal(actual, self.expected)

    def test_throws_BoardException_when_out_of_bounds(self):
        with self.assertRaises(BoardException):
            sudoku.ninth(0, 2)
        with self.assertRaises(BoardException):
            sudoku.ninth(4, 2)
        with self.assertRaises(BoardException):
            sudoku.ninth(None, 2)
        with self.assertRaises(BoardException):
            sudoku.ninth(2, 0)
        with self.assertRaises(BoardException):
            sudoku.ninth(2, 4)
        with self.assertRaises(BoardException):
            sudoku.ninth(2, None)


class WhenSelectingNinthByElement(unittest.TestCase):
    expected = np.array([[2, 3, 8], [0, 0, 0], [0, 4, 0]])

    def test_returns_correct_ninth(self):
        actual = sudoku.ninth_by_element(5, 9)
        np_test.assert_array_equal(actual, self.expected)

    def test_throws_BoardException_when_out_of_bounds(self):
        with self.assertRaises(BoardException):
            sudoku.ninth_by_element(0, 4)
        with self.assertRaises(BoardException):
            sudoku.ninth_by_element(10, 4)
        with self.assertRaises(BoardException):
            sudoku.ninth_by_element(None, 4)
        with self.assertRaises(BoardException):
            sudoku.ninth_by_element(4, 0)
        with self.assertRaises(BoardException):
            sudoku.ninth_by_element(4, 10)
        with self.assertRaises(BoardException):
            sudoku.ninth_by_element(4, None)


if __name__ == '__main__':
    loader = unittest.TestLoader()
