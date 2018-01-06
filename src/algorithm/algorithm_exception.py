from enum import Enum


class AlgorithmException(Exception):

    def __init__(self, error_arguments, reason):
        super(AlgorithmException, self).__init__("Algorithm Exception raised: " + str(error_arguments))
        self.reason = reason


class Parameter(Enum):
    INVALID_VALUE = 1
    UNEXPECTED_ELEMENT_TYPE = 2
