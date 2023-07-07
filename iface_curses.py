#!/usr/bin/env python3
"""
Pytuino interface (ncurses)

Pytuino has a number of interface options, this uses the curses module
"""

import curses


class PytuinoIface:
    """
    Provides a curses based interface to the display/keyboard
    """

    def __init__(self):
        """
        Initialise curses interface handling
        """
        # Initialise curses screen
        self._stdscreen = curses.initscr()
        # Turn off key echo
        curses.noecho()
        # Turn on cbreak mode (get keys when pressed, rather than after 'enter' pressed)
        curses.cbreak()
        # Enable conversion of special key (cursor keys, etc) keycodes to curses equivalent
        self._stdscreen.keypad(True)
        # Make cursor invisible
        curses.curs_set(0)

        # Store screen size
        self._columns = curses.COLS
        self._rows = curses.LINES

    def close(self):
        """
        Returns the terminal to the original settings
        """
        curses.curs_set(1)
        self._stdscreen.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def get_key(self):
        """
        Return a key(code) if any are pressed (non blocking)
        """
        return self._stdscreen.getket()

    def print_str(self, txt, cols=None, rows=None, attr=None):
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
        """
        if cols is None and rows is None:
            if attr is None:
                self._stdscreen.addstr(txt)
            else:
                self._stdscreen.addstr(txt, attr)
        else:
            if attr is None:
                self._stdscreen.addstr(rows, cols, txt)
            else:
                self._stdscreen.addstr(rows, cols, txt, attr)

    def redraw(self):
        """
        Update the screen with any changes
        """
        return self._stdscreen.refresh()

# Main
###########################################################################################
if __name__ == '__main__':
    import time

    try:
        ptoi = PytuinoIface()

        ptoi.print_str("Hello World", attr=(curses.A_BOLD|curses.A_BLINK))
        ptoi.print_str("Hello World", cols=20, rows=10)
        ptoi.print_str("Hello World", cols=40, rows=20, attr=(curses.A_BOLD|curses.A_BLINK))
        ptoi.redraw()

        time.sleep(2)

        ptoi.close()
    except Exception as e:
        print(f"Error: {e}")
