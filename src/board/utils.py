import logging

from src.board.board_exception import BoardException, Parameter


def validate_row(row):
    if row is None or row < 1 or row > 9:
        logging.error('Row value ' + str(row) + ' is out of bounds')
        raise BoardException(row, Parameter.ROW)


def validate_col(col):
    if col is None or col < 1 or col > 9:
        logging.error('Col value ' + str(col) + ' is out of bounds')
        raise BoardException(col, Parameter.COL)


def validate_ninth(row, col):
    if row is None or row < 1 or row > 3:
        logging.error('Row value for ninth ' + str(row) + ' is out of bounds')
        raise BoardException(row, Parameter.ROW)
    if col is None or col < 1 or col > 3:
        logging.error('Col value for ninth ' + str(col) + ' is out of bounds')
        raise BoardException(col, Parameter.COL)
