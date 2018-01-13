import logging
from src.element import validator

from src.element.element_exception import ElementException, Parameter


class Element:
    def __init__(self, value=validator.cleared):
        validator.validate_input_value(value)
        if value is validator.cleared:
            self.is_immutable = False
            self.possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.value = validator.cleared
        else:
            self.is_immutable = True
            self.possible_values = [value]
            self.value = value

    def next_possible_value(self):
        validator.validate_before_change_element(self)
        next_value = self.possible_values[0]
        del self.possible_values[0]
        return next_value

    def set_value(self, value):
        validator.validate_before_set_value(self)
        self.value = value

    def reset(self):
        validator.validate_before_reset(self)
        self.value = validator.cleared
        self.possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
