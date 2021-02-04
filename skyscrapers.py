"""
This module deals with skyscrapers game.
My github repository: https://github.com/juliaaz/skyscrapers
"""
def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    file = open(path, 'r' )
    contents = file.read().split('\n')
    contents = contents[:-1]
    return contents

def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    input_line = input_line[1:-1]
    digits = list(map(int, list(input_line)))
    # sort_cons = []
    for i in range(pivot-1):
        if digits[i] > digits[pivot-1]:
            return False
            # sort_cons.append(digits[i+1])
    return True
# print(left_to_right_check("412453*", 4))

def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    line_board = ''.join(board)
    if ('?' in line_board) or (' ' in line_board):
        return False
    return True
# print(check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***']))

def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    unique = True
    rows = board[1:-1]
    for row in rows:
        row = row[1:-1]
        char_seen=[]
        for i in row:
            if i in char_seen:
                unique = False
            char_seen.append(i)
    return unique
# print(check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    visible = True
    rows = board[1:-1]
    for row in rows:
        if row[0] == '*' and row[-1] != '*':
            pivot_row = int(row[-1])
            row = row[::-1]

        if row[0] != '*' and row[-1] == '*':
            pivot_row = int(row[0])

        else:
            pivot_row = None

        num_hint = 0
        if pivot_row is not None:
            for index in range(1, len(row) - 1):
                if left_to_right_check(row, index):
                    num_hint += 1
            if pivot_row != num_hint:
                visible = False
    return visible
# print(check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """

    list_of_digits = []
    for index in range(0, len(board)):
        digit = ''
        for num in range(len(board)):
            digit = digit + board[num][index]
        list_of_digits.append(digit)
    return check_horizontal_visibility(list_of_digits) and check_uniqueness_in_rows(list_of_digits)

# print(check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))

def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    board = read_input(input_path)
    result = check_columns(board) and\
        check_uniqueness_in_rows(board) and\
            check_horizontal_visibility(board) and\
                check_not_finished_board(board)
    return result

if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))
