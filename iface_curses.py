#!/usr/bin/env python3
"""
Pytuino interface (ncurses)

Pytuino has a number of interface options, this uses the curses module
"""

import curses

###############################################################################
class PytuinoIface:
###############################################################################
    """
    Provides a curses based interface to the display/keyboard
    """

    KEY_DOWN = curses.KEY_DOWN
    KEY_LEFT = curses.KEY_LEFT
    KEY_RIGHT = curses.KEY_RIGHT
    KEY_UP = curses.KEY_UP

    TXT_BOLD = curses.A_BOLD
    TXT_NORMAL = curses.A_NORMAL
    TXT_REVERSE = curses.A_REVERSE

    COLOUR_BLACK = curses.COLOR_BLACK
    COLOUR_RED = curses.COLOR_RED
    COLOUR_GREEN = curses.COLOR_GREEN
    COLOUR_YELLOW = curses.COLOR_YELLOW
    COLOUR_BLUE = curses.COLOR_BLUE
    COLOUR_MAGENTA = curses.COLOR_MAGENTA
    COLOUR_CYAN = curses.COLOR_CYAN
    COLOUR_WHITE = curses.COLOR_WHITE
    COLOUR_ORANGE = curses.COLOR_WHITE + 1
    COLOUR_PINK = curses.COLOR_WHITE + 2

    def __init__(self):
        """
        Initialise curses interface handling
        """
        # Initialise curses screen
        self._stdscreen = curses.initscr()
        # Initialise colour
        self._stdscreen_has_color = False
        if curses.has_colors():
            curses.start_color()
            self._stdscreen_has_color = True
        # Turn off key echo
        curses.noecho()
        # Turn on cbreak mode (get keys when pressed, rather than after 'enter' pressed)
        curses.cbreak()
        # Set keyboard reading routines as non-blocking
        self._stdscreen.nodelay(True)
        # Enable conversion of special key (cursor keys, etc) keycodes to curses equivalent
        self._stdscreen.keypad(True)
        # Make cursor invisible
        curses.curs_set(0)

        # Add colours
        curses.init_color(PytuinoIface.COLOUR_YELLOW, 1000, 1000, 0)
        curses.init_color(PytuinoIface.COLOUR_ORANGE, 1000, 500, 0)
        curses.init_color(PytuinoIface.COLOUR_PINK, 1000, 300, 580)
        # Initialise colour pairs
        curses.init_pair(1, PytuinoIface.COLOUR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, PytuinoIface.COLOUR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(3, PytuinoIface.COLOUR_ORANGE, curses.COLOR_BLACK)
        curses.init_pair(4, PytuinoIface.COLOUR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(5, PytuinoIface.COLOUR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(6, PytuinoIface.COLOUR_RED, curses.COLOR_BLACK)
        curses.init_pair(7, PytuinoIface.COLOUR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(8, PytuinoIface.COLOUR_PINK, curses.COLOR_BLACK)

        curses.init_pair(255, PytuinoIface.COLOUR_WHITE, curses.COLOR_BLACK)

        # Store screen size
        self._columns = curses.COLS
        self._rows = curses.LINES

        # Store max colours
        self._max_colours = curses.COLORS

    def close(self):
        """
        Returns the terminal to the original settings
        """
        curses.curs_set(1)
        self._stdscreen.keypad(False)
        self._stdscreen.nodelay(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def clear_screen(self):
        """
        Clear the screen
        """
        self._stdscreen.erase()

    def color_pair(self, colour_index):
        """Wrapper of curses color_pair"""
        return curses.color_pair(colour_index)

    def get_key(self):
        """
        Return a key(code) if any are pressed (non blocking)
        """
        try:
            return self._stdscreen.getch()
        except Exception:
            return ""

    def init_pair(self, index, foreground, background):
        """
        Create colour pairs which are later refenced when inserting text

        index
            Index of colour pair ro create
        foreground
            Foreground colour
        background
            Background colour
        """
        curses.init_pair(index, foreground, background)

    def print_str(self, txt, cols=None, rows=None, attr=None, clr=None):
        """
        Print a string on screen

        txt
            String to display
        cols
            Column offset
        rows
            Row offset
        attr
            Attributes to use
        clr
            Colour attributes
        """
        if cols is None and rows is None:
            if attr is None and (clr is None or self._stdscreen_has_color is False):
                self._stdscreen.addstr(txt)
            else:
                attr_combined = 0
                if not attr is None:
                    attr_combined |= attr
                if not clr is None and self._stdscreen_has_color is True:
                    attr_combined |= clr
                self._stdscreen.addstr(txt, attr_combined)
        else:
            if attr is None and (clr is None or self._stdscreen_has_color is False):
                self._stdscreen.addstr(rows, cols, txt)
            else:
                attr_combined = 0
                if not attr is None:
                    attr_combined |= attr
                if not clr is None and self._stdscreen_has_color is True:
                    attr_combined |= clr
                self._stdscreen.addstr(rows, cols, txt, attr_combined)

    def redraw(self):
        """
        Update the screen with any changes
        """
        return self._stdscreen.refresh()

    def set_position(self, cols, rows):
        """
        Move cursor to given position
        """
        self._stdscreen.move(rows, cols)

# Main
###############################################################################
if __name__ == '__main__':
    import math
    import time

    ptoi = None
    err = None
    try:
        ptoi = PytuinoIface()

        ptoi.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        ptoi.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
        ptoi.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

        hello_str = "Hello World"
        quit_str = "Press Q to quit"
        # Current position
        cur_column = 0
        cur_row = 0
        # Next position will add these values
        add_column = 1
        add_row = 1

        while True:
            ptoi.clear_screen()

            # Truncate sring when it's tail is off screen
            tmp_len = ptoi._columns - cur_column
            if tmp_len > len(hello_str):
                tmp_len = len(hello_str)
            ptoi.print_str(hello_str[0:tmp_len], cols=cur_column, rows=cur_row, attr=curses.A_BOLD, clr=curses.color_pair(2))

            # Update co-ordinates
            if add_column == 1:
                if cur_column == (ptoi._columns - 1):
                    add_column = -1
            else:
                if cur_column == 0:
                    add_column = 1
            if add_row == 1:
                if cur_row == (ptoi._rows - 1):
                    add_row = -1
            else:
                if cur_row == 0:
                    add_row = 1
            cur_column += add_column
            cur_row += add_row

            ptoi.print_str(quit_str, cols=math.floor((ptoi._columns-len(quit_str))/2), rows=(ptoi._rows-1), attr=curses.A_BOLD, clr=curses.color_pair(1))

            ptoi.redraw()

            # Check for quit key
            key = ptoi.get_key()
            if key == 'Q':
                break

            time.sleep(0.05)

    except Exception as e:
        err = e
    finally:
        if not ptoi is None:
            ptoi.close()
        if not err is None:
            print(f"Last co-ordinates: {cur_column}x{cur_row}")
            raise err

        # Print info on exit
        print(f"Screen size: {ptoi._columns}x{ptoi._rows}")
        print(f"Number of colours: {curses.COLORS}")

