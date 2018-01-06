from src.algorithm import utils


class DepthFirstSearch:
    def __init__(self, board):
        self.row = 1
        self.col = 1
        self.moving_deeper = True
        self.board = board

    def search(self):
        self.setup()
        while not self.board.is_complete():
            element = self.board.element(self.row, self.col)
            if element.is_immutable:
                self.handle_immutable_element(element)
            elif not element.possible_values:
                self.handle_element_without_possible_values(element)
            else:
                self.handle_mutable_element_with_possibilities(element)
        return self.board

    def setup(self):
        self.row = 1
        self.col = 1
        self.moving_deeper = True

    def handle_immutable_element(self, element):
        utils.check_element_is_immutable(element)
        if self.moving_deeper:
            self.set_next_position()
        else:
            self.set_previous_position()

    def handle_element_without_possible_values(self, element):
        utils.check_element_has_no_possible_values(element)
        element.reset()
        self.set_previous_position()

    def handle_mutable_element_with_possibilities(self, element):
        utils.check_element_is_mutable_and_has_possible_values(element)
        element.value = 0
        element = self.find_valid_value_for_element(element)
        if element.value is 0:  # Means that no possible values were found
            element.reset()
            self.set_previous_position()

    def find_valid_value_for_element(self, element):
        while element.possible_values:
            value = element.next_possible_value()
            if self.is_valid_value(value):
                element.set_value(value)
                self.set_next_position()
                break
        return element

    def is_valid_value(self, value):
        utils.validate_input_value(value)
        row_values = self.board.row(self.row)
        col_values = self.board.col(self.col)
        ninth_values = self.board.ninth_by_element(self.row, self.col)

        return utils.validate_row(row_values, value) \
            and utils.validate_col(col_values, value)\
            and utils.validate_ninth(ninth_values, value)

    def set_next_position(self):
        row, col = utils.next_position(self.row, self.col)
        self.row = row
        self.col = col
        self.moving_deeper = True

    def set_previous_position(self):
        row, col = utils.previous_position(self.row, self.col)
        self.row = row
        self.col = col
        self.moving_deeper = False
