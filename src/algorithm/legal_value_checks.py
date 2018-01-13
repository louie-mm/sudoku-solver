def is_legal_element(row_values, col_values, ninth_values, value):
    return is_legal_row(row_values, value) and is_legal_col(col_values, value) and is_legal_ninth(ninth_values, value)


def is_legal_row(row_values, value):
    for el in row_values:
        if el == value:
            return False
    return True


def is_legal_col(col_values, value):
    for el in col_values:
        if el == value:
            return False
    return True


def is_legal_ninth(ninth_values, value):
    for array in ninth_values:
        for el in array:
            if el == value:
                return False
    return True

