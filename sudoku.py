"""The Sudoku solver.
"""

__author__ = 'Ronen Rosenberg, Suri Castro'

class Square:
    """A `Square` consists of 4 attributes.

    `value` is an integer value between 0 and 9, inclusive.  0 means
    empty, otherwise `value` indicates the value currently assigned to
    the corresponding location in the grid.

    `row` is an array of 8 references to all the `Square` neighbors in
    the same row as the this Square.

    `column` is the same as `row` but for neighbors in the same column.

    `block` is the same as `row` but for neighbors in the same block.

    Note: don't edit this class definition.

    """
    pass

def main():

    """Prints the solution to the puzzle in the specified directory."""

    with open('sudoku1.txt') as file:
        puzzle = file.read()
    grid = create_squares(puzzle)
    solve(grid)
    print(to_string(grid))

def create_location(row, col):

    """Returns with the specified row and column as a pair."""

    # TODO You have to write this
    return None

def find_row(here):

    """Returns an array of the eight locations (represented by pairs) in
    the same row as here (represented by a pair).

    """

    # TODO You have to write this
    return None

def find_column(here):

    """Returns an array of the eight locations (represented by pairs) in
    the same column as here (represented by a pair).

    """

    # TODO You have to write this
    return None

def find_block(here):

    """Returns an array of the eight locations (represented by pairs) in
    the same 3x3 block as here (represented by a pair).

    """

    # TODO You have to write this
    return None

def create_squares(diagram=None):

    """Returns a 9x9 array of instances of `Square` objects.  Recall that
    each `Square` has 4 attributes.  The attributes are `value`,
    `row`, `column`, and `block`.  The first attribute is the value
    assigned to the associated position in the grid.  The other three
    attributes are references to all the 3*8 neighbors in the same
    row, in the same column, and in the same block as this location.

    If argument `diagram` is None, then all the values are set to 0.
    Otherwise, the values are set according to the diagram (empty
    squares are represented with value 0).  The optional argument
    `diagram` is a string with numbers to be filled in the grid, or
    dots to represent empty squares, or optional newlines to enhance
    readability when printed.

    """

    # TODO You have to write this
    return None

def to_string(grid):

    """Returns a string representing grid, showing the numbers (or . for
    square with value 0).

    """

    # TODO You have to write this
    return None

def find_valid_numbers(square):

    """Returns a boolean array of length 10.  For each digit, the
    corresponding entry in the array is True if that number does not
    appear elsewhere in the Square's row, column, or block.

    """

    # TODO You have to write this
    return None

def solve(grid):

    """Returns true if grid can be solved. If so, grid is modified to fill
    in that solution.

    """

    # TODO You have to write this
    # Here's an outline of the algorithm:
    # for each square
    #     if its value is 0
    #         for each valid number that could be filled in
    #             if you can solve the rest of the grid
    #                 return True
    #         nothing worked: set value back to 0 and return false
    # no squares left to fill in: return true
    return True

if __name__ == '__main__': main()