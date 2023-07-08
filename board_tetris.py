#!/usr/bin/env python3
"""
Pytuino Tetris Board

Tetris board implemented as a 2 dimensional lists
"""

class TetrisBoard:
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
        Fills the board with correctly sized rows until it is full
        """
        while len(self._board) < self._rows:
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
###########################################################################################
if __name__ == '__main__':
    tboard = TetrisBoard()
    tboard._fill_rand_()
    print(tboard)
    tboard.remove_rows()
    print(tboard)
