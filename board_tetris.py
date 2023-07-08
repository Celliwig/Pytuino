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
        self._board = [ [0]*columns for i in range(rows)  ]
        self._max_colours = colours

    def __str__(self):
        rtn = ""
        rtn += f"Columns: {self._columns}	Rows: {self._rows}\n\n"

        for row in self._board:
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

# Main
###########################################################################################
if __name__ == '__main__':
    tboard = TetrisBoard()
    print(tboard)
