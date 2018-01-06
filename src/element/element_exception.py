from enum import Enum


class ElementException(Exception):

    def __init__(self, error_arguments, reason):
        super(ElementException, self).__init__("Element Exception raised: " + str(error_arguments))
        self.reason = reason


class Parameter(Enum):
    ATTEMPT_CHANGE_IMMUTABLE_ELEMENT = 1,
    NO_MORE_POSSIBLE_VALUES = 2
    INPUT_VALUE_OUT_OF_BOUNDS = 3,
    CLEARING_WHILE_REMAINING_POSSIBILITIES = 4,
    ATTEMPT_TO_SET_VALUE_NOT_IN_POSSIBLE_VALUES = 5
