import logging

from src.algorithm.algorithm_exception import AlgorithmException, Parameter


def validate_input_value(value):
    if value is None or value < 1 or value > 9:
        logging.error('Input value ' + str(value) + ' is out of bounds')
        raise AlgorithmException('Input value ' + str(value) + ' is out of bounds',
                                 Parameter.INVALID_VALUE)


def validate_element_is_immutable(element):
    if not element.is_immutable:
        logging.error('Unexpected mutable element. Was expecting immutable element')
        raise AlgorithmException('Unexpected mutable elements',
                                 Parameter.UNEXPECTED_ELEMENT_TYPE)


def validate_element_has_no_possible_values(element):
    if element.possible_values:
        logging.error('Element still has remaining values. Was expecting no remaining values')
        raise AlgorithmException('Unexpected remaining values',
                                 Parameter.UNEXPECTED_ELEMENT_TYPE)


def validate_element_is_mutable_and_has_possible_values(element):
    if element.is_immutable:
        logging.error('Unexpected immutable element. Was expecting mutable element')
        raise AlgorithmException('Unexpected mutable elements',
                                 Parameter.UNEXPECTED_ELEMENT_TYPE)
    if not element.possible_values:
        logging.error('Expecting possible values. Element has no more remaining possible values')
        raise AlgorithmException('Unexpected empty possible values',
                                 Parameter.UNEXPECTED_ELEMENT_TYPE)
