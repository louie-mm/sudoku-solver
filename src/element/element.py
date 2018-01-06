import logging
from src.element import utils

from src.element.element_exception import ElementException, Parameter


class Element:
    def __init__(self, value=utils.cleared):
        utils.validate_input_value(value)
        if value is utils.cleared:
            self.is_immutable = False
            self.possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.value = utils.cleared
        else:
            self.is_immutable = True
            self.possible_values = [value]
            self.value = value

    def next_possible_value(self):
        self.__validate_before_change_element()
        next_value = self.possible_values[0]
        del self.possible_values[0]
        return next_value

    def set_value(self, value):
        self.__validate_before_set_value()
        self.value = value

    def reset(self):
        self.__validate_before_reset()
        self.value = utils.cleared
        self.possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __validate_before_change_element(self):
        if self.is_immutable:
            logging.error('Attempt to try next possible value on immutable element')
            raise ElementException('Attempt to try next possible value on immutable element',
                                   Parameter.ATTEMPT_CHANGE_IMMUTABLE_ELEMENT)
        if len(self.possible_values) is 0:
            logging.warning('Element has no more possible values to try')
            raise ElementException('Element has no more possible values to try',
                                   Parameter.NO_MORE_POSSIBLE_VALUES)

    def __validate_before_set_value(self):
        if self.is_immutable:
            logging.error('Attempt to set value on immutable element')
            raise ElementException('Attempt to set value on immutable element',
                                   Parameter.ATTEMPT_CHANGE_IMMUTABLE_ELEMENT)

    def __validate_before_reset(self):
        if self.is_immutable:
            logging.error('Attempt to try next possible value on immutable element')
            raise ElementException('Attempt to try next possible value on immutable element',
                                   Parameter.ATTEMPT_CHANGE_IMMUTABLE_ELEMENT)
        if len(self.possible_values) is not 0:
            logging.warning('Element has more possible values to try')
            raise ElementException('Element has more possible values to try',
                                   Parameter.CLEARING_WHILE_REMAINING_POSSIBILITIES)
