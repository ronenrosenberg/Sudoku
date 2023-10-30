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

    '''def __init__(self, value, row, column, block):
        self.value = value
        self.row = row
        self.column = column
        self.block = block'''

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

    #generates array where all val are None lmao
    array = [[None for col in range(9)] for row in range(9)]
    
    #generates a structure for data to fit into
    for i in range(9):
        for j in range(9):
            array[i][j] = Square()
            array[i][j].value = 0
            array[i][j].row = [0 for i in range(8)]
            array[i][j].column = [0 for i in range(8)]
            array[i][j].block = [0 for i in range(8)]

    #remove newline shit
    if diagram != None:
        diagram = diagram.replace("\n","")
        diagram = diagram.replace(".","0")
        
    for i in range(9):
        for j in range(9):
            #we make these so the code is neater - lists of locations of pertinent surround squares
            tempcol = find_column((i,j))
            temprow = find_row((i,j))
            tempblock = find_block((i,j))

            for k in range(8): #and this lets the code read the .row[x] stuff
                #initialize 
                array[i][j].column[k] = array[tempcol[k][0]][tempcol[k][1]]
                array[i][j].row[k] = array[temprow[k][0]][temprow[k][1]]
                array[i][j].block[k] = array[tempblock[k][0]][tempblock[k][1]]
    

    if diagram != None:
        diagram_index = 0
        for i in range(9):
            for j in range(9):
                array[i][j].value = int(diagram[diagram_index])# so the value is an int
                diagram_index += 1

    return array

def to_string(grid):

    """Returns a string representing grid, showing the numbers (or . for
    square with value 0).

    """

    # TODO You have to write this

    str_grid = ''
    for i in range(9):
        for j in range(9):
            if grid[i][j].value == 0:
                str_grid += '.'
            else:
                str_grid += str(grid[i][j].value)
        str_grid += '\n'

    return str_grid

def find_valid_numbers(square):

    """Returns a boolean array of length 10.  For each digit, the
    corresponding entry in the array is True if that number does not
    appear elsewhere in the Square's row, column, or block.

    """
    array = [False]

    for i in range(1, 10):
        bool = True
        for surrounding_squares in square.row:
            if surrounding_squares.value == i:
                bool = False
        for surrounding_squares in square.column:
            if surrounding_squares.value == i:
                bool = False
        for surrounding_squares in square.block:
            if surrounding_squares.value == i:
                bool = False
        array.append(bool)

    return array



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
    
    #for each square
    for i in range(9):
        for j in range(9):
            #if its value is 0
            if grid[i][j].value == 0:
                
                #get valid nums
                valid_nums = []
                for k in range(10):
                    if find_valid_numbers(grid[i][j])[k] != 0:
                        valid_nums.append(k)
                        
                #for each valid number that can be filled in 
                for k in valid_nums:
                    grid[i][j].value = k
                    #if you can solve the rest of the grid
                    if solve(grid):
                        return True
                
                #nothing worked: set value back to 0 and return false
                grid[i][j] = 0
                return False
    
    #if no squares left to fill in, return True     
    is_zero = False
    for i in range(9):
        for j in range(9):
            if grid[i][j].value == 0:
                is_zero = True
    if not is_zero:
        return True
            
                        


                        


                

if __name__ == '__main__': main()