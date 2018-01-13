import logging


from src.element.element_exception import ElementException, Parameter

cleared = 0


def validate_input_value(value):
    if value is None or ((value < 1 or value > 9) and value is not cleared):
        logging.error('Input value ' + str(value) + ' is out of bounds')
        raise ElementException('Input value ' + str(value) + ' is out of bounds',
                               Parameter.INPUT_VALUE_OUT_OF_BOUNDS)
