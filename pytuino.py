#!/usr/bin/env python3
"""
Pytuino

A text based Tetris implementation
"""

import argparse
import time

from board_tetris import TetrisBoard, Tetromino

import curses
from iface_curses import PytuinoIface

###############################################################################
class Pytuino:
###############################################################################
    """
    Main wrapper of the game
    """

    # Version number
    version=0.1

    def __init__(self, debug=False):
        # Store debug parameter
        self._debug = debug

        # Initialise interface
        self._iface = PytuinoIface()

        # Board store
        self._board = None

    def _printd(self, txt, end="\n"):
        """ Print txt if debug flag set """
        if self._debug:
            print(txt, end=end)

    def close(self):
        """ Close down interface """
        self._iface.close()

    def run(self):
        """ Main routine """

        # Generate new board
        self._board = TetrisBoard()
        if not self._board.iface_check(self._iface):
            raise Exception("Pytuino: screen too small")

        # Generate random fill
        #self._board._fill_rand_()

        # Loop until 'Q' is pressed
        while True:
            # Get the next tetromino if needed
            if self._board.get_current_tetromino() is None:
                self._board.get_next_tetromino()
                self._board.tetromino_start()

            # Redraw screen
            self._board.draw_board(self._iface)
            self._iface.redraw()

            # Check for key press
            key = self._iface.get_key()

            # Tetromino rotate
            if key == ord('z') or key == ord('Z'):
                self._board.tetromino_rotate(Tetromino.DIR_ANTICLOCKWISE)
            if key == ord('x') or key == ord('X'):
                self._board.tetromino_rotate(Tetromino.DIR_CLOCKWISE)

            # Tetromino move
            if key == PytuinoIface.KEY_DOWN:
                self._board.tetromino_move(Tetromino.DIR_DOWN)
            if key == PytuinoIface.KEY_LEFT:
                self._board.tetromino_move(Tetromino.DIR_LEFT)
            if key == PytuinoIface.KEY_RIGHT:
                self._board.tetromino_move(Tetromino.DIR_RIGHT)


            # Check for quit key
            if key == ord('Q'):
                break

            # Sleep for a bit
            time.sleep(0.01)

# Main
###############################################################################
if __name__ == '__main__':
    # Build option parser
    parser = argparse.ArgumentParser(
        usage="%(prog)s [action]",
        description="Pytuino - Text based Tetris implementation"
    )
    parser.add_argument(
        "-d", "--debug", help="Print debug information.",
        action="store_true"
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version = f"{parser.prog} version {Pytuino.version}"
    )
    args = parser.parse_args()

    pto = None
    err = None
    try:
        pto = Pytuino(debug=args.debug)
        pto.run()
    except Exception as e:
        err = e
    finally:
        if not pto is None:
            pto.close()

            # Print info on exit
            print(f"Screen size: {pto._iface._columns}x{pto._iface._rows}")
            print(f"Number of colours: {pto._iface._max_colours}")
        if not err is None:
            raise err

