import logging


from src.element.element_exception import ElementException, Parameter

cleared = 0


def validate_input_value(value):
    if value is None or ((value < 1 or value > 9) and value is not cleared):
        logging.error('Input value ' + str(value) + ' is out of bounds')
        raise ElementException('Input value ' + str(value) + ' is out of bounds',
                               Parameter.INPUT_VALUE_OUT_OF_BOUNDS)


def validate_before_change_element(element):
    if element.is_immutable:
        logging.error('Attempt to try next possible value on immutable element')
        raise ElementException('Attempt to try next possible value on immutable element',
                               Parameter.ATTEMPT_CHANGE_IMMUTABLE_ELEMENT)
    if len(element.possible_values) is 0:
        logging.warning('Element has no more possible values to try')
        raise ElementException('Element has no more possible values to try',
                               Parameter.NO_MORE_POSSIBLE_VALUES)


def validate_before_set_value(element):
    if element.is_immutable:
        logging.error('Attempt to set value on immutable element')
        raise ElementException('Attempt to set value on immutable element',
                               Parameter.ATTEMPT_CHANGE_IMMUTABLE_ELEMENT)


def validate_before_reset(element):
    if element.is_immutable:
        logging.error('Attempt to try next possible value on immutable element')
        raise ElementException('Attempt to try next possible value on immutable element',
                               Parameter.ATTEMPT_CHANGE_IMMUTABLE_ELEMENT)
    if len(element.possible_values) is not 0:
        logging.warning('Element has more possible values to try')
        raise ElementException('Element has more possible values to try',
                               Parameter.CLEARING_WHILE_REMAINING_POSSIBILITIES)