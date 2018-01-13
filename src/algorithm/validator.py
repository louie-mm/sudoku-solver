import logging

from src.algorithm.algorithm_exception import AlgorithmException, Parameter


def next_position(row, col):
    col += 1
    if col is 10:
        col = 1
        row += 1
    return row, col


def previous_position(row, col):
    col -= 1
    if col is 0:
        col = 9
        row -= 1
    return row, col


def validate_input_value(value):
    if value is None or value < 1 or value > 9:
        logging.error('Input value ' + str(value) + ' is out of bounds')
        raise AlgorithmException('Input value ' + str(value) + ' is out of bounds',
                                 Parameter.INVALID_VALUE)


def validate_row(row_values, value):
    for el in row_values:
        if el == value:
            return False
    return True


def validate_col(col_values, value):
    for el in col_values:
        if el == value:
            return False
    return True


def validate_ninth(ninth_values, value):
    for array in ninth_values:
        for el in array:
            if el == value:
                return False
    return True


def check_element_is_immutable(element):
    if not element.is_immutable:
        logging.error('Unexpected mutable element. Was expecting immutable element')
        raise AlgorithmException('Unexpected mutable elements',
                                 Parameter.UNEXPECTED_ELEMENT_TYPE)


def check_element_has_no_possible_values(element):
    if element.possible_values:
        logging.error('Element still has remaining values. Was expecting no remaining values')
        raise AlgorithmException('Unexpected remaining values',
                                 Parameter.UNEXPECTED_ELEMENT_TYPE)


def check_element_is_mutable_and_has_possible_values(element):
    if element.is_immutable:
        logging.error('Unexpected immutable element. Was expecting mutable element')
        raise AlgorithmException('Unexpected mutable elements',
                                 Parameter.UNEXPECTED_ELEMENT_TYPE)
    if not element.possible_values:
        logging.error('Expecting possible values. Element has no more remaining possible values')
        raise AlgorithmException('Unexpected empty possible values',
                                 Parameter.UNEXPECTED_ELEMENT_TYPE)
