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
    def __init__(self, value, row, column, block):
        self.value = value
        self.row = row
        self.column = column
        self.block = block

def main():

    """Prints the solution to the puzzle in the specified directory."""

    with open('sudoku1.txt') as file:
        puzzle = file.read()
    grid = create_squares(puzzle)
    print(puzzle)
    solve(grid)
    print(to_string(grid))

def create_location(row, col):

    """Returns with the specified row and column as a pair."""

    return (row, col)

def find_row(here):

    """Returns an array of the eight locations (represented by pairs) in
    the same row as here (represented by a pair).

    """

    array = [(here[0],i) for i in range(9)]
    array.remove(here)
    return array


def find_column(here):

    """Returns an array of the eight locations (represented by pairs) in
    the same column as here (represented by a pair).

    """
    #generate list of all locations in column
    array = [(i,here[1]) for i in range(9)]
    #remove location of "here"
    array.remove(here)

    return array

def find_block(here):

    """Returns an array of the eight locations (represented by pairs) in
    the same 3x3 block as here (represented by a pair).
    """
    
    array = []
    #extract x and y
    (x, y) = (here)
    #do math to find the location of the upper left square of whatever block we're in
    blockx, blocky = int(3*(x//3.0)), int(3*(y//3.0))
    #generate an array that contains all of the locations in the block
    for i in range(blockx, blockx+3):
        for j in range(blocky, blocky+3):
            array.append((i,j))

    #remove the location of "here"
    array.remove(here)

    return array


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
    #removes newline shit
    diagram = diagram.strip()
    #generates array where all val are 0
    array = [[Square(0, find_row((i, j)), find_column((i, j)), find_block((i, j))) for i in range(9)] for j in range(9)]
    if diagram == None: return array
    """
    i = 0
    j = 0
    for val in range(len(diagram)):
        if val != None:
            array[i][j] = val
        if i == 8:
            i = 0
            j += 1
        i += 1
    return array
    """
    for i in range(9):
        for j in range(9):
            pass
    

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
