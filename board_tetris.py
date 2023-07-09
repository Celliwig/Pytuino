#!/usr/bin/env python3
"""
Pytuino Tetris Board

Tetris board implemented as a 2 dimensional lists

Based on: https://tetris.wiki/Tetris_Guideline
"""

import math
import random

###############################################################################
class TetrominoSingle:
###############################################################################
    """
    Class representing a single Tetris piece (tetromino) state
    """

    def __init__(self, blocks):
        """
        Initialise the basic struture of the tetromino

            blocks
                2 dimensional list representing the tetromino blocks
        """
        self._blocks = blocks
        self._rows = len(blocks)
        self._columns = len(blocks[0])

    def __str__(self):
        rtn = ""
        for row in self._blocks:
            if len(rtn) > 0:
                rtn += "\n"
            for cell in row:
                if cell == 0:
                    rtn += "  "
                else:
                    rtn += str(cell)+str(cell)
        return rtn

    def get_blocks(self):
        return self._blocks
    def get_columns(self):
        return self._columns
    def get_rows(self):
        return self._rows

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
        i_piece.append([ 0, 1, 0, 0 ])
        i_piece.append([ 0, 1, 0, 0 ])
        i_piece.append([ 0, 1, 0, 0 ])
        i_piece.append([ 0, 1, 0, 0 ])
        return TetrominoComposite(i_piece, "I", 1)

    @staticmethod
    def createJ():
        """
        Create the prototype J tetromino (colour: dark blue)
        """
        j_piece = []
        j_piece.append([ 1, 0, 0 ])
        j_piece.append([ 1, 1, 1 ])
        j_piece.append([ 0, 0, 0 ])
        return TetrominoComposite(j_piece, "J", 2)

    @staticmethod
    def createL():
        """
        Create the prototype L tetromino (colour: orange)
        """
        l_piece = []
        l_piece.append([ 0, 0, 1 ])
        l_piece.append([ 1, 1, 1 ])
        l_piece.append([ 0, 0, 0 ])
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
        s_piece.append([ 0, 0, 0 ])
        return TetrominoComposite(s_piece, "S", 5)

    @staticmethod
    def createT():
        """
        Create the prototype T tetromino (colour: red)
        """
        t_piece = []
        t_piece.append([ 0, 1, 0 ])
        t_piece.append([ 1, 1, 1 ])
        t_piece.append([ 0, 0, 0 ])
        return TetrominoComposite(t_piece, "T", 6)

    @staticmethod
    def createZ():
        """
        Create the prototype Z tetromino (colour: magenta)
        """
        z_piece = []
        z_piece.append([ 1, 1, 0 ])
        z_piece.append([ 0, 1, 1 ])
        z_piece.append([ 0, 0, 0 ])
        return TetrominoComposite(z_piece, "Z", 7)

    @staticmethod
    def createTest():
        """
        Create the prototype test tetromino (colour: N/A)
        """
        tst_piece = []
        tst_piece.append([ 1, 1, 1 ])
        tst_piece.append([ 1, 0, 1 ])
        tst_piece.append([ 0, 0, 1 ])
        return TetrominoComposite(tst_piece, "Test", 1)

###############################################################################
class Tetromino:
###############################################################################
    """
    Class representing a single Tetromino
    """

    DIR_ANTICLOCKWISE = 0
    DIR_CLOCKWISE = 1
    DIR_DOWN = 2
    DIR_LEFT = 3
    DIR_RIGHT = 4
    DIR_UP = 5

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
        self._position_column = None
        self._position_row = None

    def __str__(self):
        rtn = ""
        rtn += f"Tetromino: {self._composite._name}\n"
        rtn += f"Rotational State: {self._rotational_state}\n"
        rtn += f"Column: {self._position_column}	Row: {self._position_row}\n\n"
        rtn += str(self._composite._pieces[self._rotational_state])
        return rtn

    def get_state(self):
        """ Return the current block positions for this tetromino """
        return self._composite._pieces[self._rotational_state]

    def get_posX(self):
        return self._position_column

    def get_posY(self):
        return self._position_row

    def rotate(self, direction, test=False):
        """
        Rotate (change state) the current tetromino

            test
                If set, only return the updated rotational state don't save
        """
        updated_state = self._rotational_state

        # Update state
        if direction == Tetromino.DIR_ANTICLOCKWISE:
            updated_state -= 1
        if direction == Tetromino.DIR_CLOCKWISE:
            updated_state += 1

        if updated_state < 0:
            updated_state = 3
        if updated_state > 3:
            updated_state = 0

        # Update current state
        if not test:
            self._rotational_state = updated_state

        return self._composite._pieces[updated_state]

    def set_position(self, column, row):
        """ Set the position of the tetromino """
        # Update the current position on the board
        self._position_column = column
        self._position_row = row

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
        # Need a random number generator for various actions (including initialisation)
        self._rnd = random.Random()

        self._columns = columns
        self._rows = rows
        self._board = []
        self._fill_rows_()
        self._max_colours = colours

        # Tetromino 'bag'
        self._tetromino_bag = []
        self.fill_tetromino_bag()
        # Current tetromino
        self._tetromino = None

        # Current score
        self._score = 0

        # Layout variables
        # Tetromino block size factors
        self._renderer_tetromino_block_height = 1
        self._renderer_tetromino_block_width = 1
        # Tetris board head offset
        self._renderer_board_column_offset_left = 0
        self._renderer_board_column_offset_right = 0
        self._renderer_board_row_offset_top = 0
        self._renderer_board_row_offset_bottom = 0
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
        for row_index in range(0, self._rows-1):
            row = self._board[row_index]
            for i in range(self._columns):
                row[i] = self._rnd.randrange(0, self._max_colours)

    def check_tetromino_position(self, tetromino=None, tetromino_state=None, position_x=None, position_y=None):
        """
        Check whether the given tetromino can exist at the given position
        """
        if tetromino is None:
            tetromino = self._tetromino
        if tetromino_state is None:
            tetromino_state = tetromino.get_state()
        if position_x is None:
            position_x = tetromino.get_posX()
        if position_y is None:
            position_y = tetromino.get_posY()

        # Check whether the tetromino is out of bounds
        tmp_y = position_y + (tetromino_state.get_rows() - 1)
        for blocks in tetromino_state.get_blocks():
            tmp_x = position_x
            for cell in blocks:
                if cell:
                    if tmp_x < 0 or tmp_y < 0 or tmp_x >= self._columns or tmp_y >= self._rows:
                        return False
                tmp_x += 1
            tmp_y -= 1

        return True

    def get_current_tetromino(self, remove=True):
        """ Return the active tetromino """
        return self._tetromino

    def get_next_tetromino(self, remove=True):
        """
        Gets the next tetromino from the bag
        Optionally removes it and sets it as the current tetromino if there is none selected
        Additionally refills the bag if it's empty
        """
        # Get next tetromino
        if remove and self._tetromino is None:
            rtn = self._tetromino_bag.pop(0)
            self._tetromino = rtn
        else:
            rtn = self._tetromino_bag[0]

        # Refill bag if empty
        if len(self._tetromino_bag) == 0:
            fill_tetromino_bag()

        return rtn

    def fill_tetromino_bag(self):
        """
        Fill the tetromoni bag with a single Tetromino piece of every type, then randomise the order (Random Generator)
        """

        # Add all the different types of Tetromino
        self._tetromino_bag.append(Tetromino(Tetromino.TETROMINO_I))
        self._tetromino_bag.append(Tetromino(Tetromino.TETROMINO_J))
        self._tetromino_bag.append(Tetromino(Tetromino.TETROMINO_L))
        self._tetromino_bag.append(Tetromino(Tetromino.TETROMINO_O))
        self._tetromino_bag.append(Tetromino(Tetromino.TETROMINO_S))
        self._tetromino_bag.append(Tetromino(Tetromino.TETROMINO_T))
        self._tetromino_bag.append(Tetromino(Tetromino.TETROMINO_Z))

        # Randomise the list
        self._rnd.shuffle(self._tetromino_bag)

#    def remove_rows(self):
#        """
#        Removes any full rows, and inserts replacements at the top of the board
#        """
#        # Scan in reverse order as rows can be removed
#        for row_index in range(self._rows-1, -1, -1):
#            # Select row
#            row = self._board[row_index]
#
#            remove_row = True
#            # Checking each cell
#            for cell in row:
#                # For a space
#                if cell == 0:
#                    # Which if it exists, we can ignore the row
#                    remove_row = False
#                    break
#            if remove_row:
#                # Remove selected row
#                self._board.pop(row_index)
#
#        # Added any needed rows
#        self._fill_rows_()

    def tetromino_move(self, direction):
        """
        Move the current tetromino in the given direction
        """
        tmp_x = self._tetromino.get_posX()
        tmp_y = self._tetromino.get_posY()

        if direction == Tetromino.DIR_LEFT:
            tmp_x -= 1
        if direction == Tetromino.DIR_RIGHT:
            tmp_x += 1
        if direction == Tetromino.DIR_DOWN:
            tmp_y -= 1
        if direction == Tetromino.DIR_UP:
            tmp_y += 1

        if self.check_tetromino_position(position_x=tmp_x, position_y=tmp_y):
            self._tetromino.set_position(tmp_x, tmp_y)

    def tetromino_rotate(self, direction):
        """
        Rotate the current tetromino in the given direction
        """
        if self.check_tetromino_position(tetromino_state=self._tetromino.rotate(direction, test=True)):
            self._tetromino.rotate(direction)

    def tetromino_start(self):
        """
        Place a newly selected tetromino in it's starting position
        """
        if not self._tetromino is None:
            self._tetromino.set_position(5, 5)

# Interface related methods
###############################################################################
    def iface_check(self, iface, tetro_blk_width=1, tetro_blk_height=1):
        """
        Check whether interface is large enough for the board
        """

        # Stop oversized parameters
        if tetro_blk_width > 3 or tetro_blk_height > 2:
            return False

        # Needed columns is the number of board columns plus 2 for the border
        needed_columns = (self._columns * tetro_blk_width) + 2
        # Needed rows is the number of board rows +2 for new tetromino placement plus 1 for border
        needed_rows = ((self._rows + 2) * tetro_blk_height) + 1

        # Just return if there is not enough space
        if iface._columns < needed_columns:
             return False
        if iface._rows < needed_rows:
             return False

        # Try to workout a sensible layout based on the size of the screen
        # Tetromino block size factors
        self._renderer_tetromino_block_height = tetro_blk_height
        self._renderer_tetromino_block_width = tetro_blk_width
        # Tetris board offset
        self._renderer_board_column_offset_left = math.floor(iface._columns/2)-math.floor(((self._columns*tetro_blk_width)+2)/2)
        self._renderer_board_column_offset_right = self._renderer_board_column_offset_left+(self._columns*tetro_blk_width)
        self._renderer_board_row_offset_top = math.floor((iface._rows-needed_rows)/2) + (2 * tetro_blk_height)
        self._renderer_board_row_offset_bottom = self._renderer_board_row_offset_top+(self._rows*tetro_blk_height)

        # Try enlarging the tetromino block width
        self.iface_check(iface, tetro_blk_width+1, tetro_blk_height)
        if tetro_blk_width == 3:
            self.iface_check(iface, tetro_blk_width, tetro_blk_height+1)

        # Score
        if self._renderer_board_column_offset_left >= 12:
            self._renderer_score_show = True
            self._renderer_score_offset_column = iface._columns-math.floor(self._renderer_board_column_offset_left/2)
            self._renderer_score_offset_row = math.floor(iface._rows/2)
        # Next tetromino
        self._renderer_ntetro_show = False
        self._renderer_ntetro_offset_column = 0
        self._renderer_ntetro_offset_row = 0
        self._renderer_ntetro_num = 1

        return True

    def draw_board(self, iface):
        """ Render the game (includng score, etc) to the screen """
        # Clear screen
        iface.clear_screen()

        # Draw board with border
        row_count = 0
        for row_index in range(self._rows-1, -1, -1):
            for repeat_row in range(0, self._renderer_tetromino_block_height):
                iface.print_str(u'\u2551', cols=self._renderer_board_column_offset_left, rows=self._renderer_board_row_offset_top + row_count, attr=iface.TXT_BOLD, clr=iface.color_pair(8))
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
        iface.print_str(u'\u255A', cols=self._renderer_board_column_offset_left, rows=self._renderer_board_row_offset_top + row_count, attr=iface.TXT_BOLD, clr=iface.color_pair(8))
        for repeat_column in range(0, self._columns * self._renderer_tetromino_block_width):
            iface.print_str(u'\u2550', attr=iface.TXT_BOLD, clr=iface.color_pair(8))
        iface.print_str(u'\u255D', attr=iface.TXT_BOLD, clr=iface.color_pair(8))

        # Show score
        if self._renderer_score_show:
            score_txt = "Score:"
            iface.print_str(score_txt, cols=self._renderer_score_offset_column-math.floor(len(score_txt)/2), rows=self._renderer_score_offset_row, attr=iface.TXT_BOLD, clr=iface.color_pair(255))
            iface.print_str(f"{self._score:012}", cols=self._renderer_score_offset_column-6, rows=self._renderer_score_offset_row+1, attr=iface.TXT_BOLD, clr=iface.color_pair(255))

        # Draw current tetromino
        if not self._tetromino is None and not (self._tetromino.get_posX() is None or self._tetromino.get_posY() is None):
            # Get the block configuration to draw
            tetromino_state = self._tetromino.get_state()

            # Calculate tetromino position
            tetromino_position_x = self._renderer_board_column_offset_left + 1 + (self._renderer_tetromino_block_width * self._tetromino.get_posX())
            tetromino_position_y = self._renderer_board_row_offset_bottom - (self._renderer_tetromino_block_height * (self._tetromino.get_posY() + tetromino_state.get_rows()))

            # Draw Tetromino
            for blocks in tetromino_state.get_blocks():
                # Set cursor position
                for repeat_row in range(0, self._renderer_tetromino_block_height):
                    iface.set_position(tetromino_position_x, tetromino_position_y)
                    for cell in blocks:
                        if cell > 0:
                            cell_txt = u'\u2592' * self._renderer_tetromino_block_width
                            iface.print_str(cell_txt, attr=iface.TXT_NORMAL, clr=iface.color_pair(cell))
                        else:
                            iface.skip_ch(self._renderer_tetromino_block_width)
                    tetromino_position_y += 1

# Main
###############################################################################
if __name__ == '__main__':
    tboard = TetrisBoard()
    for tetromino in tboard._tetromino_bag:
        print(tetromino)
    print(tboard._tetromino)

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

#    tet = Tetromino(Tetromino.TETROMINO_TEST)
#    print(tet)

