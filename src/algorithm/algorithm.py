from src.algorithm import validator, legal_value_checks as checks


class DepthFirstSearch:
    def __init__(self, board):
        self.row = 1
        self.col = 1
        self.moving_forward = True
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
                self.handle_mutable_element_with_possible_values(element)
        return self.board

    def setup(self):
        self.row = 1
        self.col = 1
        self.moving_forward = True

    def handle_immutable_element(self, element):
        validator.validate_element_is_immutable(element)
        if self.moving_forward:
            self.next_position()
        else:
            self.previous_position()

    def handle_element_without_possible_values(self, element):
        validator.validate_element_has_no_possible_values(element)
        element.reset()
        self.previous_position()

    def handle_mutable_element_with_possible_values(self, element):
        validator.validate_element_is_mutable_and_has_possible_values(element)
        element.value = 0
        element = self.find_legal_value_for_element(element)
        if element.value is 0:  # Means that no possible values were found
            element.reset()
            self.previous_position()

    def find_legal_value_for_element(self, element):
        while element.possible_values:
            value = element.next_possible_value()
            if self.is_legal_value(value):
                element.set_value(value)
                self.next_position()
                break
        return element

    def is_legal_value(self, value):
        validator.validate_input_value(value)
        row_values = self.board.row(self.row)
        col_values = self.board.col(self.col)
        ninth_values = self.board.ninth_by_element(self.row, self.col)
        return checks.is_legal_element(row_values, col_values, ninth_values, value)

    def next_position(self):
        row, col = next_position(self.row, self.col)
        self.row = row
        self.col = col
        self.moving_forward = True

    def previous_position(self):
        row, col = previous_position(self.row, self.col)
        self.row = row
        self.col = col
        self.moving_forward = False


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