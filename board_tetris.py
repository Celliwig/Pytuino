#!/usr/bin/env python3
"""
Pytuino Tetris Board

Tetris board implemented as a 2 dimensional lists

Based on: https://tetris.wiki/Tetris_Guideline
"""

import math

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
class Tetromino:
###############################################################################
    """
    Class representing a single Tetromino
    """

    TETROMINO_I = 1
    TETROMINO_J = 2
    TETROMINO_L = 3
    TETROMINO_O = 4
    TETROMINO_S = 5
    TETROMINO_T = 6
    TETROMINO_Z = 7
    TETROMINO_TEST = 8

    def __init__(self, type):
        """
        Initialise the tetromino

            type
                The type of the tetromino
        """
        self._type = type

        self._composite = None
        # Initialise from TetrominoComposite static method
        if type == Tetromino.TETROMINO_I:
            self._composite = TetrominoComposite.createI()
        elif type == Tetromino.TETROMINO_J:
            self._composite = TetrominoComposite.createJ()
        elif type == Tetromino.TETROMINO_L:
            self._composite = TetrominoComposite.createL()
        elif type == Tetromino.TETROMINO_O:
            self._composite = TetrominoComposite.createO()
        elif type == Tetromino.TETROMINO_S:
            self._composite = TetrominoComposite.createS()
        elif type == Tetromino.TETROMINO_T:
            self._composite = TetrominoComposite.createT()
        elif type == Tetromino.TETROMINO_Z:
            self._composite = TetrominoComposite.createZ()
        elif type == Tetromino.TETROMINO_TEST:
            self._composite = TetrominoComposite.createTest()

        # Tetromino rotational state
        self._rotational_state = 0
        # Tetromino rotational state (previous)
        self._rotational_state_prev = 0

        # Current position on the board
        self._position_column = -1
        self._position_row = -1

    def __str__(self):
        rtn = ""
        rtn += f"Tetromino: {self._composite._name}\n"
        rtn += f"Rotational State: {self._rotational_state}\n"
        rtn += f"Column: {self._position_column}	Row: {self._position_row}\n\n"
        rtn += str(self._composite._pieces[self._rotational_state])
        return rtn

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

        # Layout variables
        # Tetromino block size factors
        self._renderer_tetromino_block_height = 1
        self._renderer_tetromino_block_width = 1
        # Tetris board offset
        self._renderer_board_offset_column = 0
        self._renderer_board_offset_row = 0
        # Score
        self._renderer_score_show = False
        self._renderer_score_offset_column = 0
        self._renderer_score_offset_row = 0
        # Next tetromino
        self._renderer_ntetro_show = False
        self._renderer_ntetro_offset_column = 0
        self._renderer_ntetro_offset_row = 0
        self._renderer_ntetro_num = 1

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

# Interface related methods
###############################################################################
    def iface_check(self, iface, tetro_blk_width=1, tetro_blk_height=1, make_do=True):
        """
        Check whether interface is large enough for the board
        """

        too_small = False

        # Check if interface is too small to render just the board
        if make_do:
            # Needed columns is the number of board columns plus 2 for the border
            needed_columns = (self._columns * tetro_blk_width) + 2
            # Needed rows is the number of board rows +2 for new tetromino placement plus 1 for border
            needed_rows = ((self._rows + 2) * tetro_blk_height) + 1

            if iface._columns < needed_columns:
                too_small = True
            if iface._rows < needed_rows:
                too_small = True
            if too_small:
                return False
            else:
                # Tetromino block size factors
                self._renderer_tetromino_block_height = tetro_blk_height
                self._renderer_tetromino_block_width = tetro_blk_width
                # Tetris board offset
                self._renderer_board_offset_column = math.floor((iface._columns-needed_columns)/2)
                self._renderer_board_offset_row = math.floor((iface._rows-needed_rows)/2) + (2 * tetro_blk_height)
                # Score
                self._renderer_score_show = False
                self._renderer_score_offset_column = 0
                self._renderer_score_offset_row = 0
                # Next tetromino
                self._renderer_ntetro_show = False
                self._renderer_ntetro_offset_column = 0
                self._renderer_ntetro_offset_row = 0
                self._renderer_ntetro_num = 1

        # Try to workout a sensible layout based on the size of the screen
        return True

    def draw_board(self, iface):
        """ Render the game (includng score, etc) to the screen """
        # Clear screen
        iface.clear_screen()

        # Draw board with border
        row_count = 0
        for row_index in range(self._rows-1, -1, -1):
            for repeat_row in range(0, self._renderer_tetromino_block_height):
                iface.print_str(u'\u2551', cols=self._renderer_board_offset_column, rows=self._renderer_board_offset_row + row_count, attr=iface.TXT_BOLD, clr=iface.color_pair(8))
                row = self._board[row_index]
                for cell in row:
                    if cell > 0:
                        cell_txt = u'\u2592' * self._renderer_tetromino_block_width
                        iface.print_str(cell_txt, attr=iface.TXT_NORMAL, clr=iface.color_pair(cell))
                    else:
                        cell_txt = " " * self._renderer_tetromino_block_width
                        iface.print_str(cell_txt, attr=iface.TXT_BOLD, clr=iface.color_pair(cell))
                iface.print_str(u'\u2551', attr=iface.TXT_BOLD, clr=iface.color_pair(8))
                row_count += 1
        # Draw bottom
        iface.print_str(u'\u255A', cols=self._renderer_board_offset_column, rows=self._renderer_board_offset_row + row_count, attr=iface.TXT_BOLD, clr=iface.color_pair(8))
        for repeat_column in range(0, self._columns * self._renderer_tetromino_block_width):
            iface.print_str(u'\u2550', attr=iface.TXT_BOLD, clr=iface.color_pair(8))
        iface.print_str(u'\u255D', attr=iface.TXT_BOLD, clr=iface.color_pair(8))

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
#    print("Dump: Test")
#    print(TetrominoComposite.createTest())


    tet = Tetromino(Tetromino.TETROMINO_TEST)
    print(tet)
