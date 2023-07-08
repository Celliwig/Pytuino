#!/usr/bin/env python3
"""
Pytuino

A text based Tetris implementation
"""

import argparse

import board_tetris

import curses
from iface_curses import PytuinoIface

class Pytuino:
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

    def _printd(self, txt, end="\n"):
        """ Print txt if debug flag set """
        if self._debug:
            print(txt, end=end)

    def close(self):
        """ Close down interface """
        self._iface.close()

    def run(self):
        """ Main routine """

        import math
        import time

        hello_str = "Hello World"
        quit_str = "Press Q to quit"
        # Current position
        cur_column = 0
        cur_row = 0
        # Next position will add these values
        add_column = 1
        add_row = 1

        while True:
            self._iface.clear_screen()

            # Truncate sring when it's tail is off screen
            tmp_len = self._iface._columns - cur_column
            if tmp_len > len(hello_str):
                tmp_len = len(hello_str)
            self._iface.print_str(hello_str[0:tmp_len], cols=cur_column, rows=cur_row, attr=curses.A_BOLD, clr=curses.color_pair(8))

            # Update co-ordinates
            if add_column == 1:
                if cur_column == (self._iface._columns - 1):
                    add_column = -1
            else:
                if cur_column == 0:
                    add_column = 1
            if add_row == 1:
                if cur_row == (self._iface._rows - 1):
                    add_row = -1
            else:
                if cur_row == 0:
                    add_row = 1
            cur_column += add_column
            cur_row += add_row

            self._iface.print_str(quit_str, cols=math.floor((self._iface._columns-len(quit_str))/2), rows=(self._iface._rows-1), attr=curses.A_BOLD, clr=curses.color_pair(1))

            self._iface.redraw()

            # Check for quit key
            key = self._iface.get_key()
            if key == 'Q':
                break

            time.sleep(0.05)

# Main
###########################################################################################
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
        if not err is None:
            raise err

        # Print info on exit
        print(f"Screen size: {pto._iface._columns}x{pto._iface._rows}")
        print(f"Number of colours: {pto._iface._max_colours}")
