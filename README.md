# Pytuino
Python implementation of Tetris using only the text console display.

## Introduction
I had an idea for a Tetris project for another platform but wanted to try out a few details first, namely can you run it reasonably over a serial (RS232) link. Obviously such a link can not support a graphical display as such, but could provide a character (TUI) display. So this python version was developed to try out the basics while keeping development time to a minimum.

## Phase I
<img src="Pics/02.png" height="33%" width="33%" align="right">
The first thing to do was to develope the basic game. This website[1] was a great resource for insights in to the game, and made developement easier. The main concern at this point was to produce the basic game using the ncurses module to simplify console handling. To produce the board & tetrominos the box character set[2] was used, this allowed more complex (if still primitive) shapes to be produced. In addition the same character set was used to produce an oversized font for better readability and style.
<br clear="right"/><br/>

## Phase II
In progress.... This stage is to replace the ncurses interface, and create one that drives the serial interface instead, while incorparating the necessary terminal codes to replace the ncurses module funtionality i.e. cursor positioning, colour, etc. 

<p width="100%" align="center"><img src="Pics/GameOver.png" height="33%" width="33%" /></p>

## References:
1. https://tetris.wiki/Tetris_Guideline
2. https://en.wikipedia.org/wiki/Box-drawing_character
