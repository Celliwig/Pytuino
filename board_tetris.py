#!/usr/bin/env python3
"""
Pytuino Tetris Board

Tetris board implemented as a 2 dimensional lists

Based on: https://tetris.wiki/Tetris_Guideline
"""

###############################################################################
class TetrominoSingle:
###############################################################################
    """
    Class representing a single Tetris piece (tetromino) state
    """

    def __init__(self, piece):
        """
        Initialise the basic struture of the tetromino

            piece
                2 dimensional list representing the piece
        """
        self._piece = piece
        self._rows = len(piece)
        self._columns = len(piece[0])

    def __str__(self):
        rtn = ""
        for row in self._piece:
            if len(rtn) > 0:
                rtn += "\n"
            for cell in row:
                if cell == 0:
                    rtn += "  "
                else:
                    rtn += str(cell)+str(cell)
        return rtn

###############################################################################
class TetrominoComposite:
###############################################################################
    """
    Super class of a tetromino which holds all it's rotations
    """

    def __init__(self, piece, name, colour):
        """
        Initialise the tetromino composite

            piece
                2 dimensional list representing the 1st state of the tetromino
            name
                Name of this particular tetromino
            colour
                Color index to use for this piece
        """
        self._colour_index = colour
        self._name = name
        self._pieces = []

        # Create the various rotations
        num_rows = len(piece)
        num_columns = len(piece[0])

        # 0 degree
        new_piece = []
        for row_index in range(0, num_rows):
            new_row = []
            for column_index in range(0, num_columns):
                cell = piece[row_index][column_index]
                #print(f"row: {row_index}	col: {column_index}	cell: {cell}")
                if cell:
                    new_row.append(colour)
                else:
                    new_row.append(0)
            new_piece.append(new_row)
        self._pieces.append(TetrominoSingle(new_piece))

        # 90 degree
        new_piece = []
        for column_index in range(0, num_columns):
            new_row = []
            for row_index in range(num_rows-1, -1, -1):
                cell = piece[row_index][column_index]
                #print(f"row: {row_index}	col: {column_index}	cell: {cell}")
                if cell:
                    new_row.append(colour)
                else:
                    new_row.append(0)
            new_piece.append(new_row)
        self._pieces.append(TetrominoSingle(new_piece))

        # 180 degree
        new_piece = []
        for row_index in range(num_rows-1, -1, -1):
            new_row = []
            for column_index in range(num_columns-1, -1, -1):
                cell = piece[row_index][column_index]
                #print(f"row: {row_index}	col: {column_index}	cell: {cell}")
                if cell:
                    new_row.append(colour)
                else:
                    new_row.append(0)
            new_piece.append(new_row)
        self._pieces.append(TetrominoSingle(new_piece))

        # 270 degree
        new_piece = []
        for column_index in range(num_columns-1, -1, -1):
            new_row = []
            for row_index in range(0, num_rows):
                cell = piece[row_index][column_index]
                #print(f"row: {row_index}	col: {column_index}	cell: {cell}")
                if cell:
                    new_row.append(colour)
                else:
                    new_row.append(0)
            new_piece.append(new_row)
        self._pieces.append(TetrominoSingle(new_piece))

    def __str__(self):
        rtn = ""
        for piece_index in range(0, len(self._pieces)):
            if len(rtn) > 0:
                rtn += "\n"
            rtn += f"{piece_index}:\n"
            rtn += str(self._pieces[piece_index])
        return rtn

    @staticmethod
    def createI():
        """
        Create the prototype I tetromino (colour: light blue)
        """
        i_piece = []
        i_piece.append([ 1, 1, 1, 1 ])
        return TetrominoComposite(i_piece, "I", 1)

    @staticmethod
    def createJ():
        """
        Create the prototype J tetromino (colour: dark blue)
        """
        j_piece = []
        j_piece.append([ 1, 0, 0 ])
        j_piece.append([ 1, 1, 1 ])
        return TetrominoComposite(j_piece, "J", 2)

    @staticmethod
    def createL():
        """
        Create the prototype L tetromino (colour: orange)
        """
        l_piece = []
        l_piece.append([ 0, 0, 1 ])
        l_piece.append([ 1, 1, 1 ])
        return TetrominoComposite(l_piece, "L", 3)

    @staticmethod
    def createO():
        """
        Create the prototype O tetromino (colour: yellow)
        """
        o_piece = []
        o_piece.append([ 1, 1 ])
        o_piece.append([ 1, 1 ])
        return TetrominoComposite(o_piece, "O", 4)

    @staticmethod
    def createS():
        """
        Create the prototype S tetromino (colour: green)
        """
        s_piece = []
        s_piece.append([ 0, 1, 1 ])
        s_piece.append([ 1, 1, 0 ])
        return TetrominoComposite(s_piece, "S", 5)

    @staticmethod
    def createT():
        """
        Create the prototype T tetromino (colour: red)
        """
        t_piece = []
        t_piece.append([ 0, 1, 0 ])
        t_piece.append([ 1, 1, 1 ])
        return TetrominoComposite(t_piece, "T", 6)

    @staticmethod
    def createZ():
        """
        Create the prototype Z tetromino (colour: magenta)
        """
        z_piece = []
        z_piece.append([ 1, 1, 0 ])
        z_piece.append([ 0, 1, 1 ])
        return TetrominoComposite(z_piece, "Z", 7)

    @staticmethod
    def createTest():
        """
        Create the prototype test tetromino (colour: N/A)
        """
        z_piece = []
        z_piece.append([ 1, 1, 1 ])
        z_piece.append([ 1, 0, 1 ])
        z_piece.append([ 0, 0, 1 ])
        return TetrominoComposite(z_piece, "Test", 1)

###############################################################################
class TetrisBoard:
###############################################################################
    """
    Class implementing the state and methods of a Tetris board
    """

    def __init__(self, columns=10, rows=20, colours=8):
        """
        Initialise the Tetris board
        """
        self._columns = columns
        self._rows = rows
        self._board = []
        self._fill_rows_()
        self._max_colours = colours

    def __str__(self):
        rtn = ""

        rtn += f"Board size: {self._columns}x{self._rows}\n\n"

        for row_index in range(len(self._board)-1, -1, -1):
            row = self._board[row_index]
            # Border
            rtn += "#"
            for cell in row:
                if cell == 0:
                    rtn += ".."
                else:
                    rtn += str(cell)+str(cell)
            # Border
            rtn += "#"
            rtn += "\n"
        # Draw base
        for i in range ((self._columns*2)+2):
            rtn += "#"

        return rtn

    def _add_row_(self):
        """
        Add a row of the correct size to the board
        """
        self._board.append([0] * self._columns)

    def _fill_rows_(self):
        """
        Fills the board with correctly sized rows until it is full (with 2 additional rows to spawn a new tetromino in)
        """
        while len(self._board) < self._rows + 2:
            self._add_row_()

    def _fill_rand_(self):
        """
        Fills the board with random data, used for testing
        """
        import random
        rnd = random.Random()
        for row_index in range(0, self._rows-1):
            row = self._board[row_index]
            for i in range(self._columns):
                row[i] = rnd.randrange(0, self._max_colours)

    def remove_rows(self):
        """
        Removes any full rows, and inserts replacements at the top of the board
        """
        # Scan in reverse order as rows can be removed
        for row_index in range(self._rows-1, -1, -1):
            # Select row
            row = self._board[row_index]

            remove_row = True
            # Checking each cell
            for cell in row:
                # For a space
                if cell == 0:
                    # Which if it exists, we can ignore the row
                    remove_row = False
                    break
            if remove_row:
                # Remove selected row
                self._board.pop(row_index)

        # Added any needed rows
        self._fill_rows_()

# Main
###############################################################################
if __name__ == '__main__':
#    tboard = TetrisBoard()
#    tboard._fill_rand_()
#    print(tboard)
#    tboard.remove_rows()
#    print(tboard)

#    print("Dump: I")
#    print(TetrominoComposite.createI())
#    print("Dump: J")
#    print(TetrominoComposite.createJ())
#    print("Dump: L")
#    print(TetrominoComposite.createL())
#    print("Dump: O")
#    print(TetrominoComposite.createO())
#    print("Dump: S")
#    print(TetrominoComposite.createS())
#    print("Dump: T")
#    print(TetrominoComposite.createT())
#    print("Dump: Z")
#    print(TetrominoComposite.createZ())
    print("Dump: Test")
    print(TetrominoComposite.createTest())